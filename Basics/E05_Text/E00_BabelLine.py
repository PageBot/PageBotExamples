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

H, W = A4 # Standard paper size from constants.
loremIpsum = loremipsum()[:800]

def babelLine(contextName):
    context = getContext(contextName)
    context.newPage(W, H) # Make a new A4 page.

    # Define font, fontSize and color of the square
    fontName = 'PageBot-Regular'
    fontSize = pt(20)
    textColor = color(1, 0, 0)

    # Define the style of the text, alignment is centered on baseline.
    style = dict(font=fontName, fontSize=fontSize, tracking=-em(0.02),
            leading=em(1), textFill=0) #, xTextAlign=CENTER)

    # Have the context create a BabelString with the style.
    bs = context.newString(loremIpsum, style)
    bs.w = pt(400)
    bs.h = pt(400)
    print(bs.cs)

    # Draw red square, bottom-left on middle of the page
    # and sides of 50% page width.
    #context.fill(textColor)
    #context.rect(W/2, H/2, W/2, W/2)

    # Draw frame on the text
    #x = W / 2 # Left side of the frame
    #y = H / 2 # Bottom position

    x = 0 # Left side of the frame
    y = H / 2 # Bottom position

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
    context.stroke((0, 1, ))
    context.rect(x, y, bs.tw, bs.th)
    context.stroke((1, 0, ))
    context.rect(x, y, bs.w, bs.h)

    for i, line in enumerate(bs.lines):
        print(i)
        context.marker(x, y-line.y, r=r, fontSize=pt(6), prefix='#%d' % i)

    context.saveImage('_export/00_BabelLine-%s.pdf' % contextName)

for contextName in ('DrawBot', 'Flat'):
    babelLine(contextName)
