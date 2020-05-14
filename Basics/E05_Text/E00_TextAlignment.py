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
#     E00_TextAlignment.py
#
#	  Create a page in A3 landscape
#	  Show "Hkpx" on all alignment combination horizontal/vertical
#     Show origins of the text boxes
#     Add shadow to the text boxes
#     Show alignment lines
#     Show labels with alignment names.
#
from pagebot import getContext
context = getContext('DrawBot')
#context = getContext('Flat')

from pagebot.constants import *
from pagebot.elements import newText, newRect, newLine
from pagebot.document import Document
from pagebot.conditions import *
from pagebot.toolbox.color import color, blackColor, noColor
from pagebot.toolbox.units import pt, em, mm
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.gradient import Shadow

W, H = mm(600, 250) # Customize paper size

LABEL_FONT_NAME = 'PageBot-Book'
FONT_NAME = 'PageBot-Bold'
#FONT_NAME = 'PageBot-Regular'
#FONT_NAME = 'PageBot-Book'
#FONT_NAME = 'PageBot-Light'
#FONT_NAME = 'Roboto-Regular' # Gives wrong values for vertical box position
#FONT_NAME = 'Georgia' # Gives wrong value for /p descender positions

fontSize = pt(64)
textColor = blackColor
bgColor = color(0.9) # Background color of the text box
padding = mm(60) # Outside measures to accommodate alignment of the text boxes
shadow = Shadow(offset=pt(3, -3), blur=pt(3), color=0.2)

# Export in _export folder that does not commit in Git. Force to export PDF.
# The _export folder is automatically created by Document.

def textAlign(context):
    EXPORT_PATH = '_export/E00_TextAlignment-%s-%s.pdf' % (FONT_NAME, context.name)
    print('Generating:', EXPORT_PATH)
    # Make a new document with one text box. Default is to make one page.

    doc = Document(w=W, h=H, title=EXPORT_PATH, autoPages=1, context=context)
    view = doc.view # Get the current view of the document.
    view.showPadding = True # Show the page padding
    page = doc[1] # Get page on pageNumber, first in row (this is only one now).
    page.padding = padding
    XALIGNS = (LEFT, CENTER, RIGHT)
    YALIGNS = (TOP, ASCENDER, CAPHEIGHT, XHEIGHT, MIDDLE_CAP, MIDDLE_X, BASELINE, DESCENDER, BOTTOM)
    rowCnt = len(XALIGNS)-1
    colCnt = len(YALIGNS)-1

    # FIXME: Probably a view problem: why is one of the boxes without frame?

    for ix, yAlign in enumerate(YALIGNS): # Flipped, yAligns show horizontal
            for iy, xAlign in enumerate(XALIGNS):

                    style = dict(font=FONT_NAME, fontSize=fontSize, leading=em(1),
                            textFill=textColor, xAlign=xAlign) # xAlignment is part of the BabelString.
                    # Add width to the string, as target width value for the box.
                    bs = context.newString('Hkpx', style)

                    x = padding + ix*page.pw/colCnt
                    y = padding + iy*page.ph/rowCnt
                    t = newText(bs, parent=page, x=x, y=y,
                            fill=bgColor, # Show background to mark the real position of the box.
                            yAlign=yAlign, # Vertical alignment is part of the Text element box.
                            showOrigin=True, shadow=shadow, stroke=None, strokeWidth=5)
                    # Ajust the style for label
                    style['font'] = LABEL_FONT_NAME
                    style['fontSize'] = fontSize/8
                    style['textFill'] = color(0.4)
                    style['tracking'] = em(0.04) # Some correction for small label

                    # Position capHeight of the the label on distance bs1.leading from
                    # the bottom position of element t.
                    bs = context.newString(' %s | %s ' % (xAlign, yAlign), style)
                    newText(bs, parent=page, x=x, y=t.bottom - bs.leading, yAlign=CAPHEIGHT,
                            showOrigin=False)

            if 0 < ix < colCnt:
                    # Show the line for the middle columns of texts only
                    newLine(x=padding + ix*page.pw/colCnt, y=padding, w=0, h=page.ph, parent=page,
                            stroke=(0, 0, 0.5), strokeWidth=0.5)

    # Show the line for the middle row of texts, where vertical alignments is.
    newLine(x=padding, y=padding+page.ph/2, w=page.pw, h=0, parent=page,
            stroke=(0, 0, 0.5), strokeWidth=0.5)

    style = dict(font=LABEL_FONT_NAME, fontSize=fontSize*0.8, leading=em(1),
            textFill=textColor, xAlign=LEFT, yAlign=BASELINE) # xAlign is part of the BabelString.
    newText('PageBot text alignments', style=style, x=padding*2, y=page.h-padding/2,
            parent=page, showOrigin=True)

    page.solve()
    doc.export(EXPORT_PATH)

for contextName in ('DrawBot', 'Flat'):
    context = getContext(contextName)
    textAlign(context)
