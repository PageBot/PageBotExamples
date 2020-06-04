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
#     E00_BabelRun.py
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

def babelRun(contextName):
    context = getContext(contextName)
    context.newPage(W, H) # Make a new A4 page.

    # Define font, fontSize and color of the square
    textColor = color(1, 0, 0)

    style1 = dict(font='PageBot-Regular', fontSize=pt(20), tracking=-em(0.02),
            leading=em(1), textFill=0)

    style2 = dict(font='PageBot-Bold', fontSize=pt(12), tracking=-em(0.1),
            leading=em(1.2), textFill=0.5)


    # Have the context create a BabelString with the style.
    w = pt(400)
    h = pt(200)
    bs = context.newString(bs=10*'ABCD', style=style1, w=w, h=h)
    bs2 = context.newString(bs=10*'EFGH', style=style2, w=w, h=h)
    bs += bs2

    x = 0 # Left side of the frame
    y = H / 2 # Bottom position

    context.drawString(bs, (x, y))
    r = 2
    x = pt(x)
    y = pt(y)
    r = pt(r)
    context.marker(x, y, r=r, fontSize=pt(10))
    context.fill(None)
    context.stroke((0, 1, ))
    context.rect(x, y + bs.h - bs.th, bs.tw, bs.th)
    context.stroke((1, 0, ))
    context.rect(x, y, bs.w, bs.h)


    print('\n')
    print(' * ', type(bs))
    print(bs)
    print(bs.cs)

    for run in bs.runs:
        print(run, run.style, run._cr)

    for i, line in enumerate(bs.lines):
        print(line, line.cLine)
        context.marker(x + w, y-line.y, r=r, fontSize=pt(6), prefix='#%d' % i)


    context.saveImage('_export/00_BabelRun-%s.pdf' % contextName)

for contextName in ('DrawBot', 'Flat'):
    babelRun(contextName)
