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
#     00_BabelString.py
#
#     Some examples showing the working of BabelString with context
#     without the making of Document and Text elements.
#
from pagebot import getContext
context = getContext('DrawBot')
#context = getContext('Flat')

from pagebot.constants import *
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt, em

W, H = A4 # Standard paper size from constants.
context.newPage(W, H) # Make a new A4 page.

# Defin font, fontSize and color of the square
fontName = 'PageBot-Regular'
fontSize = pt(200)
textColor = color(1, 0, 0)

# Define the style of the text, alignment is centered on baseline.
style = dict(font=fontName, fontSize=fontSize, tracking=-em(0.02), 
	leading=em(0.8), textFill=0, xTextAlign=CENTER)
# Have the context create a BabelString with the style.
bs = context.newString('A4', style)

# Draw red square
context.fill(textColor)
context.rect(W/2, H/2, W/2, W/2)

# Draw the string, centered/baseline in middle of the page.
context.drawString(bs, (W/2, H/2))

