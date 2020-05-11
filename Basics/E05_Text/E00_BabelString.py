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
#     E00_BabelString.py
#
#     For demo, run this in DrawBot, with PageBot installed.
#
#     Some examples showing the working of BabelString with context
#     without the making of Document and Text elements.
#
from pagebot import getContext
c = getContext('DrawBot')
#context = getContext('Flat')

from pagebot.constants import *
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt, em

W, H = A4 # Standard paper size from constants.
c.newPage(W, H) # Make a new A4 page.

# Defin font, fontSize and color of the square
fontName = 'PageBot-Regular'
fontSize = pt(200)
textColor = color(1, 0, 0)

# Define the style of the text, alignment is centered on baseline.
style = dict(font=fontName, fontSize=fontSize, tracking=-em(0.02), 
	leading=em(1), textFill=0, xTextAlign=CENTER)
# Have the context create a BabelString with the style.
bs = c.newString('Hkpx', style)

# Draw red square, bottom-left on middle of the page
# and sides of 50% page width.
c.fill(textColor)
c.rect(W/2, H/2, W/2, W/2)

# Draw frame on the text
c.fill(None)
c.stroke((0, 0, 0.5))
x = W/2-bs.tw/2 # Left side of the frame
y = H/2-bs.th+bs.topLineAscender # Bottom position
c.rect(x, y, bs.tw, bs.th)

# Draw the string, centered/baseline in middle of the page.
c.drawString(bs, (W/2, H/2))

