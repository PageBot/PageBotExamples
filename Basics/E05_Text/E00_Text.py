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
#     E00_Text.py
#
#	  Create a page in A4 landscape
#	  Setup the document view to show registration marks and cropmarks
#     Show the page frame and padding frame in blue
#     Show the generated PDF file name on top of the page.
#	  Show red “A4” centered on the page as Text element,
#     with its middle capHeight on the middle of page height
#     Draw the background of the Text element in light gray
#
from pagebot import getContext
from pagebot.constants import *
from pagebot.conditions import *
from pagebot.elements import newText, newRect, newLine
from pagebot.document import Document
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt, em

H, W = A4 # Standard portrait, swapped to be used as landscape ratio.
fontSize = pt(300)
padding = pt(40) # Outside measures to accommodate the crop makrs.
FONT_NAME = 'PageBot-Regular'
textColor = color(1, 0, 0) # Red of the “A4”
bgColor = color(0.9) # Background color of the text box

def makeText(context):
    context = getContext(contextName)
    exportPath = '_export/00_Text-%s.pdf' % contextName
    print('Generating:', exportPath)

    doc = Document(w=W, h=H, title=exportPath, context=context)
    page = doc[1] # Get page on pageNumber, first in row (this is only one now).
    page.padding = padding
    view = doc.getView() # Get the current view of the document.
    view.showPadding = True
    view.showCropMarks = True
    view.showRegistrationMarks = True
    view.showFrame = True # Show the frame of the  page as blue line
    view.showNameInfo = True # Showing page info and title on top of the page.
    view.padding = padding # Make space to show crop marks, etc.

    # Create a style dictionary and a BabelString with that style.
    # xAlign is centered on the (x, y) position. For strings without defined
    # width xAlign and xTextAlign a equivalent.
    # yAlign is positioning on middle of the capHeight
    style = dict(font=FONT_NAME, fontSize=fontSize, tracking=-em(0.02),
            textFill=textColor, xTextAlign=CENTER, yAlign=MIDDLE_CAP)
    bs = context.newString('A4', style)

    w = h = None
    #w, h = page.ph, h=page.ph 
    t = newText(bs, parent=page, x=page.w/2, y=page.h/2, w=w, h=h, fill=bgColor,
            xAlign=CENTER, yAlign=MIDDLE, # Used for Text, in case (w, h) is defined.
            showOrigin=True)
    print(contextName, t.w, t.h, bs.w, bs.h, bs.tw, bs.th)

  # Horizontal and vertial lines, to show text position,
    newLine(parent=page, x=0, y=page.h/2, w=page.w, h=0, stroke=(0, 0, 0.8), strokeWidth=0.5)
    newLine(parent=page, x=page.w/2, y=0, w=0, h=page.h, stroke=(0, 0, 0.8), strokeWidth=0.5)

    # Export the document as PDF
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    makeText(contextName)
