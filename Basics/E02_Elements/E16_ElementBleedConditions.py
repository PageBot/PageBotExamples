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
#     E16_ElementBleedConditions.py
#
#     Position elements by their bleed sides with conditions
#

from pagebot import getContext
from pagebot.conditions import *
from pagebot.constants import EXPORT
from pagebot.document import Document
from pagebot.elements import newRect
from pagebot.toolbox.color import color
from pagebot.toolbox.units import p, pt
from pagebot.toolbox.transformer import path2FileName

W = H = pt(500)
PADDING = p(8)
BLEED = p(1)
FILENAME = path2FileName(__file__)

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    w = PADDING + BLEED # Square fills bleed and padding
    doc = Document(w=W, h=H, context=context)
    doc.view.padding = p(6) # View padding around the page.
    page = doc[1] # Get the single page from te document.
    page.padding = PADDING
    page.showPadding = True
    page.showFrame = True
    page.showCropMarks = True
    page.bleed = BLEED
    newRect(parent=page, w=w, h=w, fill=color('red'),
            conditions=[Left2BleedLeft(), Bottom2BleedBottom()])
    newRect(parent=page, w=w, h=w, fill=color('green'),
            conditions=[Center2Center(), Top2BleedTop()])
    newRect(parent=page, w=w, h=w, fill=color('blue'),
            conditions=[Right2BleedRight(), Top2BleedTop()])
    newRect(parent=page, w=w, h=w, fill=color('orange'),
            conditions=[Left2BleedLeft(), Middle2Middle()])
    newRect(parent=page, w=w, h=w, fill=color('yellow'),
            conditions=[Left2BleedLeft(), Top2BleedTop()])
    newRect(parent=page, w=w, h=w, fill=color('purple'),
            conditions=[Bottom2BleedBottom(), Right2BleedRight()])
    newRect(parent=page, w=w, h=w, fill=color('violet'),
            conditions=[Right2BleedRight(), Middle2Middle()])
    newRect(parent=page, w=w, h=w, fill=color('cyan'),
            conditions=[Center2Center(), Bottom2BleedBottom()])
    newRect(parent=page, w=w, h=w, fill=color('black'),
            conditions=[Center2Center(), Middle2Middle()])
    page.solve()
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
