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
#     E17_ElasticText.py
#
#     Create a Document of a given size
#     Draw 3 columns with the same text on the same width
#     The text box height are elastic, depending on the
#     content and the typographic parameters. Caclulating
#     their hieghts, allows other elements to float up.
#
from pagebot import getContext
from pagebot.constants import A4, LEFT, TOP, BOTTOM, XHEIGHT, EXPORT
from pagebot.conditions import *
from pagebot.elements import *
from pagebot.document import Document
from pagebot.toolbox.color import color, noColor
from pagebot.toolbox.units import pt, em
from pagebot.toolbox.loremipsum import loremIpsum
from pagebot.toolbox.transformer import path2FileName

FONT_NAME = 'PageBot-Regular'
FILENAME = path2FileName(__file__)
W = H = pt(800)
padding = pt(50)
gutter = pt(18)
fontSize = pt(14)
rectColor = color(1, 0, 0)

def makeText(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    doc = Document(w=W, h=H, title=exportPath, autoPages=1, context=context)
    view = doc.view # Get the current view of the document.
    view.padding = pt(30) # Aboid showing of crop marks, etc.
    view.showCropMarks = True
    view.showRegistrationMarks = True
    view.showFrame = True
    view.showPadding = True
    view.showNameInfo = True # Showing page info and title on top of the page.
    page = doc[1] # Get page on pageNumber, first in row (this is only one now).
    page.padding = padding
    cw = (page.pw - 2*gutter)/3 # Calculate the column with for 3 cols.
    txt = loremIpsum(words=80)

    # Make Text elements, directly from attributes, instead of style dictionary
    # or BabelString.
    newText(txt,
        parent=page, padding=4, w=cw, yAlign=XHEIGHT, font=FONT_NAME, fontSize=fontSize,
        conditions=[Left2Left(), Top2Top()], # Conditions for the layout.
        xAlign=LEFT, leading=em(1.3), textFill=0, strokeWidth=pt(0.5), showOrigin=True,
        fill=color(0.9), stroke=noColor, mb=gutter, # Margin bottom makes gap with rectangle.
    )
    newText(txt,
        parent=page, padding=4, w=cw, yAlign=XHEIGHT, font=FONT_NAME, fontSize=fontSize*1.25,
        conditions=[Center2Center(), Top2Top()], xAlign=LEFT, showOrigin=True,
        leading=em(1.2), textFill=0, strokeWidth=pt(0.5), fill=color(0.9), stroke=noColor,
        mb=gutter,
    )
    newText(txt,
        parent=page, padding=4, w=cw, yAlign=XHEIGHT, font=FONT_NAME, fontSize=fontSize*1.5,
        conditions=[Right2Right(), Top2Top()], xAlign=LEFT, showOrigin=True,
        leading=em(1.1), textFill=0, strokeWidth=pt(0.5), fill=color(0.9), stroke=noColor,
        mb=gutter,
    )
    newRect(parent=page, w=cw, h=pt(24), fill=rectColor, stroke=noColor, conditions=[Left2Left(), Float2Top()])
    newRect(parent=page, w=cw, h=pt(24), fill=rectColor, stroke=noColor, conditions=[Center2Center(), Float2Top()])
    newRect(parent=page, w=cw, h=pt(24), fill=rectColor, stroke=noColor, conditions=[Right2Right(), Float2Top()])
    doc.solve() # Make the Text elements position on their conditional places.
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    makeText(contextName)
