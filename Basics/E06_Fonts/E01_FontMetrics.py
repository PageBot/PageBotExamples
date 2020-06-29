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
#     E01_FontMetrics.py
#

from pagebot.document import Document
from pagebot.elements import newLine, newText
from pagebot import getContext
from pagebot.toolbox.units import pt, em
from pagebot.toolbox.color import Color, color
from pagebot.fonttoolbox.objects.font import findFont

def draw(contextName):
    context = getContext(contextName)
    font = findFont('PageBot-Regular')
    W, H = pt(800, 200)
    fontSize = pt(100)
    print('Size:', fontSize)
    txt = "Hello World"
    x, y = pt(50, 50) # Position of the text block and relative position of the lines.
    #context.marker(x, y)

    # Get the font for metrics.
    ratio = fontSize / font.info.unitsPerEm
    print('Scaling ratio', ratio)
    style = dict(fontSize=fontSize, leading=em(1), font=font)
    doc = Document(w=W, h=H, context=context)
    page = doc[1]

    # draw the text.
    bs = context.newString(txt, style=style)
    tw, th = bs.textSize
    print('Text width & height', tw, th)
    e = newText(bs, x=x, y=y, parent=page)

    # calculate the size of the text.
    textWidth, textHeight = bs.textSize

    # set a red stroke color.
    red = color(1, 0, 0) # Color instance can translate into any other color type.
    green = color(0, 1, 0) # Color instance can translate into any other color type.

    # loop over all font metrics and scale to the fontSize


    d = dict(baseline=0, descenter=font.getDescender(),
            ascender=font.getAscender(), xheight=font.getXHeight(),
            capheight=font.getCapHeight())

    padding=pt(10)
    style = dict(fontSize=pt(10), font=font)

    for name, metric in d.items():
        # Draw a red line with the size of the drawn text
        # Context drawing functions expect measures to be Unit instances.
        value = metric * ratio
        #print(value)
        newLine(x=x, y=y+value, w=tw, h=0, parent=page, stroke=green, strokeWidth=0.5)
        text = '%s: %s / %s' % (name, metric, value)
        t = context.newString(text, style=style)
        newText(t, x=x+textWidth+padding, y=y+value, parent=page)

    doc.export('_export/E00_FontMetric-%s.pdf' % contextName)


for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
