#! /usr/bin/env python
# -*- coding: utf-8 -*-

#   eLyXer -- convert LyX source files to HTML output.
#
#   Copyright (C) 2009 Alex Fernández
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

# --end--
# Alex 20090427
# eLyXer arrays in formulae

from gen.container import *
from util.trace import Trace
from util.clone import *
from conf.config import *
from maths.formula import *
from maths.command import *


class FormulaEquation(CommandBit):
  "A simple numbered equation."

  piece = 'equation'

  def parsebit(self, pos):
    "Parse the array"
    self.output = ContentsOutput()
    inner = WholeFormula()
    inner.parsebit(pos)
    self.add(inner)

class FormulaCell(FormulaCommand):
  "An array cell inside a row"

  def __init__(self, alignment):
    FormulaCommand.__init__(self)
    self.alignment = alignment
    self.output = TaggedOutput().settag('td class="formula-' + alignment +'"', True)

  def parsebit(self, pos):
    formula = WholeFormula()
    if not formula.detect(pos):
      Trace.error('Unexpected end of array cell at ' + pos.identifier())
      pos.skip(pos.current())
      return
    formula.parsebit(pos)
    self.add(formula)

class FormulaRow(FormulaCommand):
  "An array row inside an array"

  cellseparator = FormulaConfig.array['cellseparator']

  def __init__(self, alignments):
    FormulaCommand.__init__(self)
    self.alignments = alignments
    self.output = TaggedOutput().settag('tr', True)

  def parsebit(self, pos):
    "Parse a whole row"
    index = 0
    pos.pushending(FormulaRow.cellseparator, optional=True)
    while not pos.finished():
      alignment = self.alignments[index % len(self.alignments)]
      cell = FormulaCell(alignment)
      cell.parsebit(pos)
      self.add(cell)
      index += 1
      pos.checkskip(FormulaRow.cellseparator)
    return
    for cell in self.iteratecells(pos):
      cell.parsebit(pos)
      self.add(cell)

  def iteratecells(self, pos):
    "Iterate over all cells, finish when count ends"
    for index, alignment in enumerate(self.alignments):
      if self.anybutlast(index):
        pos.pushending(cellseparator)
      yield FormulaCell(alignment)
      if self.anybutlast(index):
        if not pos.checkfor(cellseparator):
          Trace.error('No cell separator ' + cellseparator)
        else:
          self.original += pos.popending(cellseparator)

  def anybutlast(self, index):
    "Return true for all cells but the last"
    return index < len(self.alignments) - 1

class MultiRowFormula(CommandBit):
  "A formula with multiple rows."

  def parserows(self, pos):
    "Parse all rows, finish when no more row ends"
    for row in self.iteraterows(pos):
      row.parsebit(pos)
      self.add(row)

  def iteraterows(self, pos):
    "Iterate over all rows, end when no more row ends"
    rowseparator = FormulaConfig.array['rowseparator']
    while True:
      pos.pushending(rowseparator, True)
      yield FormulaRow(self.alignments)
      if pos.checkfor(rowseparator):
        self.original += pos.popending(rowseparator)
      else:
        return

class FormulaArray(MultiRowFormula):
  "An array within a formula"

  piece = 'array'

  def parsebit(self, pos):
    "Parse the array"
    self.output = TaggedOutput().settag('table class="formula"', True)
    self.parsealignments(pos)
    self.parserows(pos)

  def parsealignments(self, pos):
    "Parse the different alignments"
    # vertical
    self.valign = 'c'
    literal = self.parsesquareliteral(pos)
    if literal:
      self.valign = literal
    # horizontal
    literal = self.parseliteral(pos)
    self.alignments = []
    for l in literal:
      self.alignments.append(l)

class FormulaCases(MultiRowFormula):
  "A cases statement"

  piece = 'cases'

  def parsebit(self, pos):
    "Parse the cases"
    self.output = TaggedOutput().settag('table class="cases"', True)
    self.alignments = ['l', 'l']
    self.parserows(pos)

class EquationEnvironment(MultiRowFormula):
  "A \\begin{}...\\end equation environment with rows and cells."

  def parsebit(self, pos):
    "Parse the whole environment."
    self.output = TaggedOutput().settag('table class="environment"', True)
    environment = self.piece.replace('*', '')
    if environment in FormulaConfig.environments:
      self.alignments = FormulaConfig.environments[environment]
    else:
      Trace.error('Unknown equation environment ' + self.piece)
      self.alignments = ['l']
    self.parserows(pos)

class BeginCommand(CommandBit):
  "A \\begin{}...\end command and what it entails (array, cases, aligned)"

  commandmap = {FormulaConfig.array['begin']:''}

  innerbits = [FormulaEquation(), FormulaArray(), FormulaCases()]

  def parsebit(self, pos):
    "Parse the begin command"
    literal = self.parseliteral(pos)
    bit = self.findbit(literal)
    ending = FormulaConfig.array['end'] + '{' + literal + '}'
    pos.pushending(ending)
    bit.parsebit(pos)
    self.add(bit)
    self.original += pos.popending(ending)

  def findbit(self, piece):
    "Find the command bit corresponding to the \\begin{piece}"
    for bit in BeginCommand.innerbits:
      if bit.piece == piece:
        newbit = Cloner.clone(bit)
        return newbit
    bit = EquationEnvironment()
    bit.piece = piece
    return bit

FormulaCommand.commandbits += [BeginCommand()]
