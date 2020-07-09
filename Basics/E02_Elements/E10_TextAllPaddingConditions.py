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
#     E10_TextAllPaddingConditions.py
#
#     Position fixed size text elements by their page side with conditions
#
from pagebot import getContext
from pagebot.conditions import *
from pagebot.constants import *
from pagebot.document import Document
from pagebot.elements import newText
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.color import color, whiteColor, blackColor
from pagebot.toolbox.transformer import path2FileName
from pagebot.toolbox.units import p, pt

BASELINE_GRID = 20
PAD = pt(30)
PADDING = PAD, PAD, PAD, PAD
NUM_LINES = 20
W = H = NUM_LINES * BASELINE_GRID + 2*PAD
FILENAME = path2FileName(__file__)
font = findFont('PageBot-Regular')
fontSize = pt(30)

def getText(doc, s):
    style = dict(font=font, fontSize=fontSize, leading=fontSize,
        textFill=whiteColor, xTextAlign=CENTER)
    tmp = doc.context.newString(s, style=style) # Hack, first one does not find the font.
    return doc.context.newString(s, style=style)

def makePage(doc, page, data, xAlign, yAlign):
    for ix, col in enumerate(data):
        for iy, row in enumerate(col):
            name = 'Hkpx%d%d' % (ix, iy)
            c = [Shrink2TextBounds()] + list(row)
            bgColor = color(ix/3, 0, iy/3, 0.8)
            newText(getText(doc, name), conditions=c,
                xAlign=xAlign, yAlign=yAlign,
                parent=page, fill=bgColor,
                showOrigin=True)
    page.solve()

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    doc = Document(w=W, h=H, baselineGrid=BASELINE_GRID,
        padding=PADDING, baselineGridStart=PAD/2, context=context)
    view = doc.view
    view.showBaselineGrid = True
    view.showPadding = True
    view.showOrigin = True

    page = doc[1] # Get the single page from the document.

    # Make data tables more readable by prefabricated conditons.
    t2t = Top2Top()
    b2b = Bottom2Bottom()
    l2l = Left2Left()
    r2r = Right2Right()
    m2m = Middle2Middle()
    c2c = Center2Center()

    data = (
        ((l2l, t2t), (c2c, t2t), (r2r, t2t)),
        ((l2l, m2m), (c2c, m2m), (r2r, m2m)),
        ((l2l, b2b), (c2c, b2b), (r2r, b2b)),
    )

    for ax in (LEFT, CENTER, RIGHT):
        for ay in (TOP, MIDDLE, BOTTOM):
            makePage(doc, page, data, ax, ay) # Position for element origin at bottom
            page = page.next

    c2l = Center2Left()
    m2t = Middle2Top()
    m2b = Middle2Bottom()
    c2r = Center2Right()

    data = (
        ((c2l, m2t), (c2c, m2t), (c2r, m2t)),
        ((c2l, m2m), (c2c, m2m), (c2r, m2m)),
        ((c2l, m2b), (c2c, m2b), (c2r, m2b)),
    )

    for ax in (LEFT, CENTER, RIGHT):
        for ay in (TOP, MIDDLE, BOTTOM):
            makePage(doc, page, data, ax, ay) # Position for element origin at bottom
            page = page.next

    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
