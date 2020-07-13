#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2017 Thom Janssen <https://github.com/thomgb>
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E02_ElementSideConditions.py
#
#     Position elements by their page sides with conditions
#
# Document is the main instance holding all information about
# the document togethers (pages, styles, etc.)
from pagebot import getContext
from pagebot.constants import EXPORT
from pagebot.document import Document
from pagebot.elements import newRect
from pagebot.toolbox.units import p, pt
from pagebot.toolbox.color import color
from pagebot.conditions import *
from pagebot.toolbox.transformer import path2FileName

W = H = pt(500)
PADDING = w = p(10) # Make square will the page padding
FILENAME = path2FileName(__file__)

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    doc = Document(w=W, h=H, context=context)
    page = doc[1] # Get the single page from te document.
    page.padding = PADDING

    page.showPadding = True

    newRect(parent=page, w=w, h=w, fill=color('red'), conditions=[Left2SideLeft(), Bottom2SideBottom()])
    newRect(parent=page, w=w, h=w, fill=color('green'), conditions=[Center2Center(), Top2SideTop()])
    newRect(parent=page, w=w, h=w, fill=color('blue'), conditions=[Right2SideRight(), Top2SideTop()])
    newRect(parent=page, w=w, h=w, fill=color('orange'), conditions=[Left2SideLeft(), Middle2Middle()])
    newRect(parent=page, w=w, h=w, fill=color('yellow'), conditions=[Left2SideLeft(), Top2SideTop()])
    newRect(parent=page, w=w, h=w, fill=color('purple'), conditions=[Bottom2SideBottom(), Right2SideRight()])
    newRect(parent=page, w=w, h=w, fill=color('violet'), conditions=[Right2SideRight(), Middle2Middle()])
    newRect(parent=page, w=w, h=w, fill=color('cyan'), conditions=[Center2Center(), Bottom2SideBottom()])
    newRect(parent=page, w=w, h=w, fill=color('black'), conditions=[Center2Center(), Middle2Middle()])

    page.solve() # Solve conditions of the page child elements

    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
