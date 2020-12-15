#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#


# -----------------------------------------------------------------------------
#
#     E14_TextLinesAlignment.py
#
#	  Create a page in A3 landscape
#	  Show text running over multiple lines without defined box
#     on all alignment combination horizontal/vertical
#     Show origins of the text lines
#     Show alignment lines
#     Show labels with alignment names.
#
from pagebot import getContext

from pagebot.constants import *
from pagebot.elements import newText, newRect, newLine
from pagebot.document import Document
from pagebot.conditions import *
from pagebot.toolbox.color import color, blackColor, noColor
from pagebot.toolbox.units import pt, em, mm
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.transformer import path2FileName

fontSize = pt(24)
W, H = mm(600, 250) # Customize paper size
padding = mm(60) # Outside measures to accommodate the crop makrs.
FONT_NAME = 'PageBot-Regular'
LABEL_FONT_NAME = 'PageBot-Book'
FILENAME = path2FileName(__file__)
textColor = blackColor
bgColor = color(0.9) # Background color of the text box

def makeText(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    print('Generating:', exportPath)
    context = getContext(contextName)

    # Make a new document with one text box.
    doc = Document(w=W, h=H, title=exportPath, autoPages=1, context=context)
    view = doc.view # Get the current view of the document.
    view.showPadding = True # Show the page padding
    page = doc[1] # Get page on pageNumber, first in row (this is only one now).
    page.padding = padding
    XALIGNS = (LEFT, CENTER, RIGHT)
    YALIGNS = (TOP, ASCENDER, CAPHEIGHT, XHEIGHT, MIDDLE_CAP, MIDDLE_X,
            BASELINE, BASE_BOTTOM, DESCENDER, BOTTOM)

    rowCnt = len(XALIGNS)-1
    colCnt = len(YALIGNS)-1

    for ix, yAlign in enumerate(YALIGNS): # Flipped, yAligns show horizontal
        if 0 < ix < colCnt:
            # Show the line for the middle row of texts
            newLine(x=padding + ix*page.pw/colCnt, y=padding, w=0, h=page.ph, parent=page,
                stroke=(0, 0, 0.5), strokeWidth=0.5)

        for iy, xAlign in enumerate(XALIGNS):
            style = dict(font=FONT_NAME, fontSize=fontSize, leading=em(1),
                textFill=textColor, xAlign=xAlign) # xAlignment is part of the BabelString.
            # Add width to the string, as target width value for the box.
            bs = context.newString('Hkpx\nMultiple lines\nof text in\none string', style)

            x = padding + ix*page.pw/colCnt
            y = padding + iy*page.ph/rowCnt
            t = newText(bs, parent=page, x=x, y=y,
                stroke=noColor, fill=bgColor, # Show background to mark the real position of the box.
                yAlign=yAlign, # Vertical alignment is part of the Text element box.
                showOrigin=True)
            # Ajust the style for label
            style['font'] = LABEL_FONT_NAME
            style['fontSize'] = fontSize/3
            style['textFill'] = color(0.4)
            style['tracking'] = em(0.04) # Some correction for small label
            bs = context.newString(' %s | %s ' % (xAlign.capitalize(), yAlign.capitalize()), style)
            newText(bs, parent=page, x=x, y=t.bottom - pt(4) , yAlign=TOP, showOrigin=False)

    # Show the line for the middle row of texts
    newLine(x=padding, y=padding+page.ph/2, w=page.pw, h=0, parent=page,
            stroke=(0, 0, 0.5), strokeWidth=0.5)

    style = dict(font=LABEL_FONT_NAME, fontSize=64*0.8, leading=em(1),
            textFill=textColor, xAlign=LEFT, yAlign=BASELINE) # xAlignment is part of the BabelString.
    newText('PageBot text alignments', style=style, x=padding, y=page.h-padding/2,
            w=page.pw, parent=page)

    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    makeText(contextName)
