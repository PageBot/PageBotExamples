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
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E12_TextAlignment2.py
#
#	  Create a landscape page
#	  Show text box with multiple lines, mixed styles and fixed width,
#     on all alignment combination horizontal/vertical
#     Show origins of the text boxes
#     Show alignment lines
#     Show labels with alignment names.
#
from pagebot import getContext

from pagebot.constants import *
from pagebot.elements import newText, newRect, newLine
from pagebot.document import Document
from pagebot.conditions import *
from pagebot.toolbox.color import color, blackColor
from pagebot.toolbox.units import pt, em, mm
from pagebot.toolbox.loremipsum import loremipsum
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.fonttoolbox.objects.font import findFont

fontSize = pt(28)
colWidth = mm(50)

W, H = mm(600, 250) # Customize paper size
padding = mm(60) # Outside measures to accommodate the crop makrs.
FONT_NAME = 'PageBot-Regular'
LABEL_FONT_NAME = 'PageBot-Book'
textColor = blackColor
bgColor = color(0.9) # Background color of the text box

def makeText(contextName):
    context = getContext(contextName)

    # Export in _export folder that does not commit in Git. Force to export PDF.
    # The _export folder is automatically created.
    exportPath = '_export/00_TextAlignment2-%s.pdf' % contextName
    print('Generating:', exportPath)

    # Make a new document with one text box.
    doc = Document(w=W, h=H, autoPages=1, context=context)
    view = doc.view # Get the current view of the document.
    view.showPadding = True # Show the page padding
    page = doc[1] # Get page on pageNumber, first in row (this is only one now).
    page.padding = padding
    XALIGNS = (LEFT, CENTER, RIGHT)
    YALIGNS = (TOP, ASCENDER, CAPHEIGHT, XHEIGHT, MIDDLE_CAP, MIDDLE_X, BASELINE, DESCENDER, BOTTOM)

    rowCnt = len(XALIGNS)-1
    colCnt = len(YALIGNS)-1

    for ix, yAlign in enumerate(YALIGNS): # Flipped, yAligns show horizontal
        if 0 < ix < colCnt:
            # Show the line for the middle row of texts
            newLine(x=padding + ix*page.pw/colCnt, y=padding, w=0, h=page.ph, parent=page,
                    stroke=(0, 0, 0.5), strokeWidth=0.5)

        for iy, xAlign in enumerate(XALIGNS):
            style1 = dict(font=FONT_NAME, fontSize=fontSize, leading=em(0.8),
                    paragraphBottomSpacing=em(0.15), # Line goes up, larger value is smaller spacing.
                    textFill=textColor, xAlign=xAlign) # xAlignment is part of the BabelString.
            # Add width to the string, as target width value for the box.
            bs = context.newString('Hkpx\n', style1)
            style2 = dict(font=FONT_NAME, fontSize=fontSize/2, leading=em(1),
                    #paragraphTopSpacing=em(0.2), # Line goes up, larger value is smaller spacing.
                    textFill=textColor, xAlign=xAlign) # xAlignment is part of the BabelString.
            bs += context.newString(' Multiple lines of text making it a BabelString box', style2)

            x = padding + ix*page.pw/colCnt
            y = padding + iy*page.ph/rowCnt
            t = newText(bs, parent=page, x=x, y=y, w=colWidth, h=mm(30),
                    fill=bgColor, # Show background to mark the real position of the box.
                    yAlign=yAlign, # Vertical alignment is part of the Text element box.
                    showOrigin=True)
            # Ajust the style for label
            style2['font'] = LABEL_FONT_NAME
            style2['fontSize'] = fontSize/3
            style2['textFill'] = color(0.4)
            style2['tracking'] = em(0.04) # Some correction for small label

            # Label just under the bottom position of the Text element.
            bs = context.newString(' %s | %s ' % (xAlign, yAlign), style2)
            newText(bs, parent=page, x=x, y=t.bottom - pt(40), yAlign=TOP, showOrigin=False)

    # Show the line for the middle row of texts
    newLine(x=padding, y=padding+page.ph/2, w=page.pw, h=0, parent=page,
            stroke=(0, 0, 0.5), strokeWidth=0.5)

    # Example where a title is made directly by the Text element, a plain string and a style.
    style = dict(font=LABEL_FONT_NAME, fontSize=64*0.8, leading=em(1),
            textFill=textColor, xAlign=LEFT, yAlign=BASELINE) # xAlignment is part of the BabelString.
    newText('PageBot text line alignments', style=style, x=padding, y=page.h-padding/2,
            w=page.pw, parent=page)
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    makeText(contextName)
