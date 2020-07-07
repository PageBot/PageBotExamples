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
#     E01_BabelString.py
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
from pagebot.toolbox.units import pt, em

W, H = A4 # Standard paper size from constants.

def babelString(contextName):
    context = getContext(contextName)
    context.newPage(W, H) # Make a new A4 page.

    # Define font, fontSize and color of the square
    fontName = 'PageBot-Regular'
    fontSize = pt(200)
    textColor = color(1, 0, 0)

    # Define the style of the text, alignment is centered on baseline.
    style = dict(font=fontName, fontSize=fontSize,# tracking=-em(0.02),
            leading=em(1), textFill=0) #, xTextAlign=CENTER)
    # Have the context create a BabelString with the style.
    bs = context.newString('Hkpx', style)

    # Draw red square, bottom-left on middle of the page
    # and sides of 50% page width.
    #context.fill(textColor)
    #context.rect(W/2, H/2, W/2, W/2)

    # Draw frame on the text
    #x = W / 2 # Left side of the frame
    #y = H / 2 # Bottom position

    x = W / 2 - bs.tw / 2 # Left side of the frame
    y = H / 2 - bs.th + bs.topLineAscender # Bottom position

    # Draw the string, centered/baseline in middle of the page.
    #context.text(bs, (x, y))
    #context.drawString(bs, (W/2, H/2))
    context.drawString(bs, (x, y))
    r = 2
    x = pt(x)
    y = pt(y)
    r = pt(r)
    context.marker(x, y, r=r, fontSize=pt(10))
    context.fill(None)
    context.stroke((0, 0, 0.5))
    context.rect(x, y, bs.tw, bs.th)


    context.saveImage('_export/00_BabelString-%s.pdf' % contextName)

for contextName in ('DrawBot', 'Flat'):
    babelString(contextName)
