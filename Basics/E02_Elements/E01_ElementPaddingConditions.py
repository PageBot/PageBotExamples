#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     www.pagebot.io
#     Licensed under MIT conditions
#
# -----------------------------------------------------------------------------
#
#     E01_ElementPaddingConditions.py
#
#     Position elements by their page padding position with conditions
#

from pagebot import getContext
from pagebot.constants import EXPORT
from pagebot.conditions import *
from pagebot.document import Document
from pagebot.elements import newRect
from pagebot.toolbox.units import p, pt
from pagebot.toolbox.color import color
from pagebot.toolbox.transformer import path2FileName

W = H = pt(500)
PADDING = p(4)
FILENAME = path2FileName(__file__)

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    w = p(8)
    doc = Document(w=W, h=H, context=context)
    page = doc[1] # Get the single page from te document.
    page.padding = PADDING
    page.showPadding = True
    newRect(parent=page, w=w, h=w, fill=color('red'), conditions=[Left2Left(),
        Bottom2Bottom()])
    newRect(parent=page, w=w, h=w, fill=color('green'),
            conditions=[Center2Center(), Top2Top()])
    newRect(parent=page, w=w, h=w, fill=color('blue'),
            conditions=[Right2Right(), Top2Top()])
    newRect(parent=page, w=w, h=w, fill=color('orange'),
            conditions=[Left2Left(), Middle2Middle()])
    newRect(parent=page, w=w, h=w, fill=color('yellow'),
            conditions=[Left2Left(), Top2Top()])
    newRect(parent=page, w=w, h=w, fill=color('purple'),
            conditions=[Bottom2Bottom(), Right2Right()])
    newRect(parent=page, w=w, h=w, fill=color('violet'),
            conditions=[Middle2Middle(), Right2Right()])
    newRect(parent=page, w=w, h=w, fill=color('cyan'),
            conditions=[Center2Center(), Bottom2Bottom()])
    newRect(parent=page, w=w, h=w, fill=color('black'),
            conditions=[Center2Center(), Middle2Middle()])
    page.solve()
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
