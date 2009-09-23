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
# Alex 20090324
# eLyXer postprocessor code

from gen.container import *
from util.trace import Trace
from gen.structure import *
from ref.label import *
from gen.layout import *
from gen.inset import *
from util.numbering import *
from ref.link import *


class Group(Container):
  "A silly group of containers"

  def __init__(self):
    self.output = ContentsOutput()

  def contents(self, contents):
    self.contents = contents
    return self

  def __unicode__(self):
    return 'Group: ' + unicode(self.contents)

class PostLayout(object):
  "Numerate an indexed layout"

  processedclass = Layout
  unique = NumberingConfig.layouts['unique']
  ordered = NumberingConfig.layouts['ordered']

  def __init__(self):
    self.generator = NumberGenerator.instance

  def postprocess(self, layout, last):
    "Generate a number and place it before the text"
    if self.containsappendix(layout):
      self.activateappendix()
    if layout.type in PostLayout.unique:
      number = self.generator.generateunique(layout.type)
    elif layout.type in PostLayout.ordered:
      level = PostLayout.ordered.index(layout.type)
      number = self.generator.generate(level)
    else:
      return layout
    layout.number = number
    layout.contents.insert(0, Constant(number + u' '))
    return layout

  def containsappendix(self, layout):
    "Find out if there is an appendix somewhere in the layout"
    for element in layout.contents:
      if isinstance(element, Appendix):
        return True
    return False

  def activateappendix(self):
    "Change first number to letter, and chapter to appendix"
    self.generator.number = ['-']

class PostStandard(object):
  "Convert any standard spans in root to divs"

  processedclass = StandardLayout

  def postprocess(self, standard, last):
    "Switch to div"
    standard.output = TaggedOutput().settag('div class="Standard"', True)
    return standard

class Postprocessor(object):
  "Postprocess a container keeping some context"

  stages = [PostLayout, PostStandard]
  unconditional = []

  def __init__(self):
    self.unconditional = StageList(Postprocessor.unconditional)
    self.stages = StageDict(Postprocessor.stages)
    self.last = None

  def postprocess(self, container):
    "Postprocess the root container and its contents"
    container.postprocessor = self
    self.postprocessrecursive(container.contents)
    container = self.postprocessroot(container)
    return container

  def postprocessroot(self, original):
    "Postprocess an element taking into account the last one"
    element = original
    element = self.stages.postprocess(element, self.last)
    element = self.unconditional.postprocess(element, self.last)
    self.last = original
    return element

  def postprocessrecursive(self, contents):
    "Postprocess the container contents recursively"
    if len(contents) == 0:
      return
    postprocessor = Postprocessor()
    for index, element in enumerate(contents):
      if isinstance(element, Container):
        contents[index] = postprocessor.postprocess(element)

class StageList(object):
  "A list of stages, always applied"

  def __init__(self, classes):
    self.stages = self.instantiate(classes)

  def instantiate(self, classes):
    "Instantiate an element from each class"
    stages = [x.__new__(x) for x in classes]
    for element in stages:
      element.__init__()
      element.stages = self
    return stages

  def postprocess(self, element, last):
    "Postprocess an element using the relevant stages"
    for stage in self.stages:
      element = stage.postprocess(element, last)
    return element

class StageDict(StageList):
  "A dictionary of stages corresponding to classes"

  def __init__(self, classes):
    "Instantiate an element from each class and store as a dictionary"
    instances = self.instantiate(classes)
    self.stagedict = dict([(x.processedclass, x) for x in instances])

  def postprocess(self, element, last):
    "Postprocess an element using the relevant stage"
    "(if its class is in the dictionary)"
    if not element.__class__ in self.stagedict:
      return element
    stage = self.stagedict[element.__class__]
    return stage.postprocess(element, last)

