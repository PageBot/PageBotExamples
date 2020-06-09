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
#     E00_BabelLine.py
#
#     For demo, run this in DrawBot, with PageBot installed.
#
#     Some examples showing the working of BabelString with context
#     without the making of Document and Text elements.
#
import traceback

from pagebot import getContext
from pagebot.constants import *
from pagebot.toolbox.color import color
from pagebot.toolbox.loremipsum import loremipsum
from pagebot.toolbox.units import pt, em
from pagebot.elements import newText, newRect, newLine
from pagebot.document import Document

H, W = A4 # Standard paper size from constants.
loremIpsum = loremipsum()

def babelLine(contextName):
    context = getContext(contextName)
    exportPath = '_export/00_BabelLine-%s.pdf' % contextName
    padding = pt(40) # Outside measures to accommodate the crop makrs.
    bgColor = color(0.9) # Background color of the text box
    black = color(0)

    doc = Document(w=W, h=H, title='00_BabelLine', context=context)
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
    fontName = 'PageBot-Regular'
    fontSize = pt(24)
    textColor = color(1, 0, 0)

    # Define the style of the text, alignment is centered on baseline.
    style = dict(font=fontName, fontSize=fontSize, tracking=-em(0.02),
            leading=em(1), textFill=0) #, xTextAlign=CENTER)

    # Have the context create a BabelString with the style.
    bs = context.newString(loremIpsum, style=style)
    #print(bs.h)

    x = pt(20)
    y = pt(H / 2)


    # This doesn't give the same results.
    #context.drawString(bs, (x, y))
    context.drawText(bs, (x, y))

    r = 2
    x = x
    y = y
    w = 600
    h = 200
    r = pt(r)
    context.marker(x, y, r=r, fontSize=pt(10))
    context.fill(None)
    context.stroke((0, 1, ))
    context.rect(x, y, w, h)

    t = newText(bs, parent=page, x=x, y=y, w=w, h=h, fill=bgColor,
            #xAlign=CENTER, yAlign=MIDDLE, # Used for Text, in case (w, h) is defined.
            showOrigin=True)

    r = newRect(parent=page, x=x, y=y, w=w, h=h, style=dict(stroke=black))
    #r = newRect(parent=page, x=x, y=y, w=w, h=h, stroke=black)


    #context.stroke((1, 0, ))
    #context.rect(x, y, bs.w, bs.h)

    #for i, line in enumerate(bs.lines):
    #    context.marker(x, y-line.y, r=r, fontSize=pt(6), prefix='#%d' % i)

    #context.saveImage('_export/00_BabelLine-%s.pdf' % contextName)
    doc.export(exportPath)



for contextName in ('DrawBot', 'Flat'):
    babelLine(contextName)
