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
from pagebot.toolbox.loremipsum import loremipsum
from pagebot.toolbox.units import pt, em

txt = loremipsum()

def babelStringMetrics(c):

    # Define font, fontSize and color of the square
    fontName = 'PageBot-Regular'
    fontSize = pt(24)
    textColor = color(1, 0, 0)

    # Define the style of the text, alignment is centered on baseline.
    style = dict(font=fontName, fontSize=fontSize, tracking=-em(0.02),
            leading=em(1.2), textFill=0, xTextAlign=CENTER)
    # Have the context create a BabelString with the style.
    bs = context.newString(txt, style)

    # (999.19pt, 1556pt) in DrawBot, ( ) in Flat
    #print(bs.getTextSize(w=2000)) 
    for span in bs.cs.pt.layout.lines:
        print(span)

for contextName in (
    #'DrawBot', 
    'Flat',):
    context = getContext(contextName)
    babelStringMetrics(context)

