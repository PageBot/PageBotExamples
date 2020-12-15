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
#     E01_FontMetrics.py
#

from pagebot import getContext
from pagebot.constants import EXPORT
from pagebot.document import Document
from pagebot.elements import newLine, newText
from pagebot.toolbox.units import pt, em
from pagebot.toolbox.color import Color, color
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.transformer import path2FileName

FILENAME = path2FileName(__file__)

W, H = pt(800, 600)
P = 50

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    doc = Document(w=W, h=H, context=context)
    page = doc[1]
    x, y = pt(P), pt(P)
    fontName = 'PageBot-Regular'
    h = drawFont(context, page, x, y, fontName)
    y += h + P
    fontName = 'Bungee-Regular'
    h = drawFont(context, page, x, y, fontName)
    y += h + P
    fontName = 'Roboto-Regular'
    h = drawFont(context, page, x, y, fontName)
    doc.export(exportPath)

def drawFont(context, page, x, y, fontName):
    font = findFont(fontName)
    fontSize = pt(100)
    txt = "Hpxk"
    #context.marker(x, y)

    # Get the font for metrics.
    upem = font.info.unitsPerEm
    ratio = fontSize / upem
    style = dict(fontSize=fontSize, leading=em(1), font=font)

    # draw the text.
    bs = context.newString(txt, style=style)
    tw, th = bs.textSize
    e = newText(bs, x=x, y=y, parent=page, showOrigin=True)

    # calculate the size of the text.
    textWidth, textHeight = bs.textSize

    # set a red stroke color.
    red = color(1, 0, 0) # Color instance can translate into any other color type.
    green = color(0, 1, 0) # Color instance can translate into any other color type.

    # loop over all font metrics and scale to the fontSize

    asc = font.getAscender()
    desc = font.getDescender()
    h = asc - desc

    d = dict(baseline=0, descender=desc, ascender=asc,
            xheight=font.getXHeight(), capheight=font.getCapHeight())

    padding=pt(10)
    style = dict(fontSize=pt(10), font=font, leading=em(1.5))

    for name, metric in d.items():
        # Draw a red line with the size of the drawn text
        # Context drawing functions expect measures to be Unit instances.
        value = metric * ratio
        newLine(x=x, y=y+value, w=tw, h=0, parent=page, stroke=green, strokeWidth=0.5)
        text = '%s: %s / %s' % (name, metric, value)
        t = context.newString(text, style=style)
        newText(t, x=x+textWidth+padding, y=y+value, parent=page)


    # TODO: calculate maxwidth info text.
    x1 = x + textWidth + 3*P
    y1 = y + desc * ratio
    h1 = h * ratio
    y2 = y1 + h1
    y3 = (y1 + y2) / 2

    newLine(parent=page, x=x1, y=y1, w=0, h=h1, stroke=0, strokeWidth=0.5)
    newLine(parent=page, x=x1-5, y=y1, w=10, h=0, stroke=0, strokeWidth=0.5)
    newLine(parent=page, x=x1-5, y=y2, w=10, h=0, stroke=0, strokeWidth=0.5)
    text = ' upem: %s\n font size: %s\n height (asc + desc): %s / %s' % (upem, fontSize, h, h*ratio)
    t = context.newString(text, style=style)
    newText(t, parent=page, x=x1, y=y3, showOrigin=True)
    return h * ratio

    # Return h.



for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
