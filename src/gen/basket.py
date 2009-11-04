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
# Alex 20091101
# eLyXer output baskets
# http://www.nongnu.org/elyxer/


import os.path
from util.options import *
from util.clone import *
from gen.toc import *


class Basket(object):
  "A basket to place a set of containers. Can write them, store them..."

  def __init__(self):
    "Initialize the basket."
    self.filterheader = False
    self.writer = None

  def setwriter(self, writer):
    self.writer = writer
    return self

  def getfilterheader(self):
    "Get a new basket just flipping the filterheader bit."
    clone = Cloner.clone(self)
    clone.setwriter(self.writer)
    clone.filterheader = True
    return clone

  def isfiltered(self, container):
    "Find out if a given container is filtered."
    if self.filterheader and container.__class__ in [LyxHeader, LyxFooter]:
      return True
    return False

  def finish(self):
    "Mark as finished."
    pass

class WriterBasket(Basket):
  "A writer of containers. Just writes them out to a writer."

  def write(self, container):
    "Write a container to the line writer."
    if self.isfiltered(container):
      return
    self.writer.write(container.gethtml())

class KeeperBasket(Basket):
  "Keeps all containers stored."

  def __init__(self):
    Basket.__init__(self)
    self.contents = []

  def write(self, container):
    "Keep the container."
    self.contents.append(container)

  def flush(self):
    "Flush the contents to the writer."
    for container in self.contents:
      if not self.isfiltered(container):
        self.writer.write(container.gethtml())

class TOCBasket(Basket):
  "A basket to place the TOC of a document."

  def setwriter(self, writer):
    Basket.setwriter(self, writer)
    Options.nocopy = True
    self.indenter = Indenter(writer)
    return self

  def write(self, container):
    "Write the table of contents for a container."
    entry = self.convert(container)
    if not entry:
      return
    self.indenter.indent(entry.depth)
    self.writer.write(entry.gethtml())

  def convert(self, container):
    "Convert a container to a TOC container."
    if container.__class__ in [LyxHeader, LyxFooter]:
      container.depth = 0
      return container
    if not hasattr(container, 'number'):
      return None
    return TOCEntry().create(container)

class SplittingBasket(Basket):
  "A basket used to split the output in different files."

  baskets = []

  def setwriter(self, writer):
    if not hasattr(writer, 'filename') or not writer.filename:
      Trace.error('Cannot use standard output for split output; ' +
          'please supply an output filename.')
      exit()
    self.addbasket(writer)
    self.base, self.extension = os.path.splitext(writer.filename)
    self.tocwriter = TOCBasket()
    return self

  def addbasket(self, writer):
    "Add a new basket."
    self.basket = KeeperBasket()
    self.basket.setwriter(writer)
    self.baskets.append(self.basket)

  def write(self, container):
    "Write a container, possibly splitting the file."
    if self.mustsplit(container):
      self.basket.write(LyxFooter())
      self.basket.flush()
      self.addbasket(LineWriter(self.getfilename(container)))
      self.basket.write(LyxHeader())
    self.basket.write(container)

  def finish(self):
    "Mark as finished."
    self.basket.flush()

  def mustsplit(self, container):
    "Find out if the oputput file has to be split at this entry."
    if self.splitalone(container):
      return True
    if not hasattr(container, 'number'):
      return False
    Trace.debug('Converting: ' + unicode(container))
    entry = self.tocwriter.convert(container)
    if not entry:
      return False
    if hasattr(entry, 'split'):
      return True
    return entry.depth <= Options.splitpart

  def splitalone(self, container):
    "Find out if the container must be split in its own page."
    found = []
    container.locateprocess(
        lambda container: container.__class__ in [PrintNomenclature, PrintIndex],
        lambda contents, index: found.append(contents[index].__class__.__name__))
    if not found:
      return False
    container.depth = 0
    container.split = found[0].lower().replace('print', '')
    return True

  def getfilename(self, container):
    "Get the new file name for a given container."
    if hasattr(container, 'split'):
      partname = '-' + container.split
    else:
      entry = self.tocwriter.convert(container)
      if entry.depth == Options.splitpart:
        partname = '-' + container.number
      else:
        partname = '-' + container.type + '-' + container.number
    return self.base + partname + self.extension
