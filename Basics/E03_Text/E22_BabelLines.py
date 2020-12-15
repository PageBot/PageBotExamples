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
#     E22_BabelLines.py
#

import traceback
from pagebot import getContext
from pagebot.constants import *
from pagebot.document import Document
from pagebot.elements import newText, newRect, newLine
from pagebot.toolbox.color import color
from pagebot.toolbox.loremipsum import loremIpsum
from pagebot.toolbox.transformer import path2FileName
from pagebot.toolbox.units import pt, em

H, W = A4 # Standard paper size from constants.
FILENAME = path2FileName(__file__)

loremIpsum = loremIpsum()

def draw(contextName):
    context = getContext(contextName)
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    padding = pt(40) # Outside measures to accommodate the crop makrs.
    bgColor = color(0.9) # Background color of the text box
    black = color(0)

    doc = Document(w=W, h=H, context=context)
    page = doc[1] # Get page on pageNumber, first in row (this is only one now).
    page.padding = padding
    view = doc.getView() # Get the current view of the document.
    view.showPadding = True
    view.showCropMarks = True
    view.showRegistrationMarks = True
    view.showFrame = True # Show the frame of the  page as blue line
    view.showNameInfo = True # Showing page info and title on top of the page.
    view.padding = padding # Make space to show crop marks, etc.

    #context.newPage(W, H) # Make a new A4 page.

    # Define font, fontSize and color of the square
    # TODO: test for different fonts.
    #fontName = 'PageBot-Regular'
    fontName = 'Roboto-Regular'
    fontSize = pt(24)
    textColor = color(1, 0, 0)

    # Define the style of the text, alignment is centered on baseline.
    style = dict(font=fontName, fontSize=fontSize,# tracking=-em(0.02),
            leading=em(1), textFill=0) #, xTextAlign=CENTER)

    # Have the context create a BabelString with the style.
    bs = context.newString(loremIpsum, style=style)

    x = pt(20)
    y = pt(H / 2)
    r = 2
    x = x
    y = y
    w = 600
    h = 200
    r = pt(r)

    t = newText(bs, parent=page, x=x, y=y, w=w, h=h, fill=bgColor,
            #xAlign=CENTER, yAlign=MIDDLE, # Used for Text, in case (w, h) is defined.
            showOrigin=True)

    r = newRect(parent=page, x=x, y=y, w=w, h=h, style=dict(stroke=black))

    for line in bs.lines:
        yLine = y + h - line.y
        l = newLine(parent=page, x=x, y=yLine, w=w, h=0, style=dict(stroke=(1, 0, 0)))

    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
