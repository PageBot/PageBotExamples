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
loremIpsum = loremipsum()

def babelLine(contextName):
    context = getContext(contextName)
    context.newPage(W, H) # Make a new A4 page.

    # Define font, fontSize and color of the square
    fontName = 'PageBot-Regular'
    fontSize = pt(24)
    textColor = color(1, 0, 0)

    # Define the style of the text, alignment is centered on baseline.
    style = dict(font=fontName, fontSize=fontSize, tracking=-em(0.02),
            leading=em(1), textFill=0) #, xTextAlign=CENTER)

    # Have the context create a BabelString with the style.
    w = pt(500)
    bs = context.newString(bs=loremIpsum, style=style, w=w)
    #print(bs.h)

    x = 0
    y = H / 2

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
        context.marker(x, y-line.y, r=r, fontSize=pt(6), prefix='#%d' % i)

    context.saveImage('_export/00_BabelLine-%s.pdf' % contextName)

for contextName in ('DrawBot', 'Flat'):
    babelLine(contextName)