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
#     E02_Text.py
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
from pagebot.toolbox.transformer import path2FileName

H, W = pt(A4) # Standard portrait, swapped to be used as landscape ratio.
fontSize = pt(200)
padding = pt(40) # Outside measures to accommodate the crop makrs.
FONT_NAME = 'Roboto-Regular'
textColor = color(1, 0, 0) # Red of the “A4”
bgColor = color(0.9) # Background color of the text box
FILENAME = path2FileName(__file__)

def makeText(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    print('Generating:', exportPath)
    context = getContext(contextName)

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

    # Creates a style dictionary and a BabelString with that style. xAlign is
    # centered on the (x, y) position. For strings without defined width xAlign
    # and xTextAlign a equivalent. yAlign is positioning on middle of the
    # capHeight.
    style = dict(font=FONT_NAME, fontSize=fontSize, tracking=0,#-em(0.02),
            textFill=textColor, xTextAlign=CENTER, yAlign=MIDDLE_CAP, leading=em(1) )
    bs = context.newString('Hpxk', style)

    #w = h = None # If not defined, the textSize will be equal to the contained string.
    #w = h = 400 # If not defined, the textSize will be equal to the contained string.
    #w, h = page.ph, h=page.ph

    x = page.w / 2
    y = page.h / 2

    #t = newText(bs, parent=page, x=x, y=y, fill=bgColor, xAlign=LEFT,
    #        yAlign=BOTTOM, showOrigin=True)
    # xAlign can be LEFT, CENTER and RIGHT.
    # yAlign can be ...
    t = newText(bs, parent=page, x=x, y=y, fill=bgColor, xAlign=CENTER,
            yAlign=BOTTOM, showOrigin=True)
    #print(bs.w, bs.h)
    baseline = bs.lines[0].y
    print(t.h, bs.th, baseline)

    '''
    print('Context:', contextName)
    print('t.w: %0.2f, t.h: %0.2f, bs.w: %s, bs.h: %s, bs.tw: %0.2f, bs.th: %0.2f' % (t.w, t.h, bs.w, bs.h, bs.tw, bs.th))
    print('bs.textSize:', bs.textSize)
    #print('bs.lines[0].runs:', bs.lines[0].runs, bs.lines[0].y) # Standardised between contexts.
    print('bs.topLineCapHeight:', bs.topLineCapHeight)
    print('bs.topLineXHeight:', bs.topLineXHeight)
    print('bs.topLineCapHeight/2:', bs.topLineCapHeight/2)
    print('bs.topLineXHeight/2:', bs.topLineXHeight/2)
    print('bs.topLineAscender:', bs.topLineAscender)
    print('bs.topLineAscender_h:', bs.topLineAscender_h)
    print('bs.bottomLineDescender_p:', bs.bottomLineDescender_p)
    print('bs.bottomLineDescender:', bs.bottomLineDescender)
    '''


    x = x - bs.tw / 2
    y = baseline
    w = t.w

    # Horizontal lines to mark top and bottom of elastic text box
    newLine(parent=page, x=x, y=y, w=w, h=0, stroke=(1, 0, 0),
            strokeWidth=0.5)#, xAlign=CENTER)

    '''
    y = t.top
    newLine(parent=page, x=x, y=y, w=w, h=0, stroke=(0, 1, 0.3),
            strokeWidth=0.5, xAlign=CENTER)
    '''


    '''
    # Vertical lines to mark left and right of elastic text box
    newLine(parent=page, x=t.left, y=t.y, w=0, h=t.h, stroke=(1, 0, 0),
            strokeWidth=0.5, yAlign=MIDDLE)

    newLine(parent=page, x=t.right, y=t.y, w=0, h=t.h, stroke=(0, 1, 0.3),
            strokeWidth=0.5, yAlign=MIDDLE)
    '''

    # Horizontal and vertical lines, to show text center/middle position,
    newLine(parent=page, x=0, y=page.h/2, w=page.w, h=0, stroke=(0, 0, 0.8),
            strokeWidth=0.5)

    newLine(parent=page, x=page.w/2, y=0, w=0, h=page.h, stroke=(0, 0, 0.8),
            strokeWidth=0.5)

    # Export the document as PDF
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    makeText(contextName)
