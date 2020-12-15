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
#     E00_BabelStringMetrics.py
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
from pagebot.toolbox.loremipsum import loremIpsum
from pagebot.toolbox.units import pt, em

txt = loremIpsum()
print(len(txt))

def babelStringMetrics(contextName):

    context = getContext(contextName)

    # Define font, fontSize and color of the square
    fontName = 'PageBot-Regular'
    fontNameBold = 'PageBot-Bold'
    fontSize = pt(36)
    textColor = color(0, 1, 0)

    # Define the style of the text, alignment is centered on baseline.
    style = dict(font=fontName, fontSize=fontSize, tracking=-em(0.02),
            leading=em(1.2), textFill=0)#, xTextAlign=CENTER)
    # Have the context create a BabelString with the style.
    bs = context.newString(txt, style)
    bs.w = 1000
    bs.add('fsjfsdff')
    style = dict(font=fontNameBold, fontSize=fontSize, tracking=-em(0.02),
            leading=em(1.2), textFill=0)#, xTextAlign=CENTER)
    bs2 = context.newString('sdfsfsdfs', style)
    bs.add(bs2)

    # DrawBot: (7866.86pt, 288pt)
    # Flat(8071.99pt, 277.15pt)
    print(bs.context)
    print(bs)
    print(bs.textSize)
    print(bs.runs)
    print(len(bs.runs))
    print(len(bs))
    print(bs.lines)
    print(len(bs.lines))

    for run in bs.runs:
        print(run)

for contextName in ('DrawBot', 'Flat'):
    babelStringMetrics(contextName)

