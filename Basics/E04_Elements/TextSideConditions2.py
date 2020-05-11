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
#     TextSideConditions2.py
#
#     Position fixed size text elements by their page side with conditions
#
# Document is the main instance holding all information about
# the document togethers (pages, styles, etc.)
from pagebot.document import Document
from pagebot.elements import newText
from pagebot.toolbox.units import p, pt
from pagebot.toolbox.color import color, whiteColor
from pagebot.conditions import *
from pagebot.constants import *
from pagebot.fonttoolbox.objects.font import findFont

W = H = pt(500)
font = findFont('PageBot Regular')

doc = Document(w=W, h=H)
t = doc.context.newString('TEXT', style=dict(font=font, fontSize=36, textFill=whiteColor, xTextAlign=CENTER))
PADDING = t.size[0]

page = doc[1] # Get the single page from te document.
page.padding = PADDING

page.showPadding = True

newText(t, parent=page, fill=color('red'), conditions=[Right2Left(), Top2Bottom()])
newText(t, parent=page, fill=color('green'), conditions=[Center2Center(), Bottom2Top()])
newText(t, parent=page, fill=color('blue'), conditions=[Left2Right(), Bottom2Top()])
newText(t, parent=page, fill=color('orange'), conditions=[Right2Left(), Middle2Middle()])
newText(t, parent=page, fill=color('yellow').darker(0.8), conditions=[Right2Left(), Bottom2Top()])
newText(t, parent=page, fill=color('purple'), conditions=[Left2Right(), Top2Bottom()])
newText(t, parent=page, fill=color('violet'), conditions=[Left2Right(), Middle2Middle()])
newText(t, parent=page, fill=color('cyan').darker(0.8), conditions=[Center2Center(), Top2Bottom()])
newText(t, parent=page, fill=color('black'), conditions=[Center2Center(), Middle2Middle()])

page.solve()

# Export in _export folder that does not commit in Git. Force to export PDF.
EXPORT_PATH = '_export/TextSideConditions2.pdf'
doc.export(EXPORT_PATH)


