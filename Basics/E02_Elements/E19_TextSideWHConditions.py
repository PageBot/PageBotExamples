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
#     E19_TextSideWHConditions.py
#
#     Position fixed size text elements by their page side with conditions
#

from pagebot import getContext
from pagebot.conditions import *
from pagebot.constants import *
from pagebot.document import Document
from pagebot.elements import newText
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.color import color, whiteColor
from pagebot.toolbox.units import p, pt
from pagebot.toolbox.transformer import path2FileName

W = H = pt(500)
PADDING = p(4)
w = p(8)
FILENAME = path2FileName(__file__)
font = findFont('PageBot Regular')

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    doc = Document(w=W, h=H)
    page = doc[1] # Get the single page from te document.
    page.padding = PADDING
    page.showPadding = True

    t = doc.context.newString('TEXT', style=dict(font=font, fontSize=36,
        textFill=whiteColor, xTextAlign=CENTER))
    newText(t, parent=page, w=w, h=w, fill=color('red'),
            conditions=[Left2Left(), Bottom2Bottom()])
    newText(t, parent=page, w=w, h=w, fill=color('green'),
            conditions=[Center2Center(), Top2Top()])
    newText(t, parent=page, w=w, h=w, fill=color('blue'),
            conditions=[Right2Right(), Top2Top()])
    newText(t, parent=page, w=w, h=w, fill=color('orange'),
            conditions=[Left2Left(), Middle2Middle()])
    newText(t, parent=page, w=w, h=w, fill=color('yellow').darker(0.8),
            conditions=[Left2Left(), Top2Top()])
    newText(t, parent=page, w=w, h=w, fill=color('purple'),
            conditions=[Bottom2Bottom(), Right2Right()])
    newText(t, parent=page, w=w, h=w, fill=color('violet'),
            conditions=[Middle2Middle(), Right2Right()])
    newText(t, parent=page, w=w, h=w, fill=color('cyan').darker(0.8),
            conditions=[Center2Center(), Bottom2Bottom()])
    newText(t, parent=page, w=w, h=w, fill=color('black'),
            conditions=[Center2Center(), Middle2Middle()])

    page.solve()
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
