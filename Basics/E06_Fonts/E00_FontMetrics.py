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
#     FontMetrics.py
#
#     It is possible to measure the metrics from a font.
#     These show examples how to do that.
#
from pagebot.document import Document
from pagebot.elements import *
from pagebot import getContext
from pagebot.toolbox.units import pt, em
from pagebot.toolbox.color import Color, color
from pagebot.fonttoolbox.objects.font import findFont

context = getContext('DrawBot')

W, H = pt(1000, 200)
fontSize = pt(100)

txt = "Hello World"
x, y = pt(50, 50) # Position of the text block and relative position of the lines.

# Get the font for metrics.
font = findFont('PageBot-Regular')
ratio = fontSize/font.info.unitsPerEm
style = dict(fontSize=fontSize, leading=em(1), font=font)

doc = Document(w=W, h=H, context=context)
page = doc[1]

# draw the text.
bs = context.newString(txt, style=style)
tw, th = bs.textSize
e = newText(bs, x=x, y=y, w=800, h=200, parent=page)

# calculate the size of the text.
textWidth, textHeight = bs.textSize

# set a red stroke color
strokeColor = color(1, 0, 0) # Color instance can translate into any other color type.

# loop over all font metrics and scale to the fontSize

for metric in (0, font.getDescender(), font.getAscender(), font.getXHeight(), font.getCapHeight()):
    # Draw a red line with the size of the drawn text
    # Context drawing functions expect measures to be Unit instances.
    newLine(x=x, y=y+metric*ratio, w=tw, h=0, parent=page, strokeColor=strokeColor)

doc.export('_export/E00_FontMetric.pdf')
