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
#     E01_BabelString.py
#
#     For demo, run this in DrawBot, with PageBot installed.
#
#     Some examples showing the working of BabelString with context
#     without the making of Document and Text elements.
#
from pagebot import getContext
from pagebot.constants import *
from pagebot.toolbox.color import color
from pagebot.toolbox.transformer import path2FileName
from pagebot.toolbox.units import pt, em

H, W = A3 # Standard paper size from constants.
FILENAME = path2FileName(__file__)

# Some notes:
# Flat text height corresponds to ascender + descender.
# DrawBot height corresponds to fontsize * leading.
FONTSIZE = 200
LEADING = 1.2
P = 10

def draw(context, contextName, y, fontName):
    fontSize = pt(FONTSIZE)
    leading = em(LEADING)
    textColor = color(1, 0, 0)

    # Define the style of the text, alignment is centered on baseline.
    style = dict(font=fontName, fontSize=fontSize,
            # tracking=-em(0.02),
            leading=leading,
            #, xTextAlign=CENTER)
            textFill=0)

    # Have the context create a BabelString with the style.
    bs = context.newString('Hkpx', style)

    # Draw red square, bottom-left on middle of the page
    # and sides of 50% page width.
    #context.fill(textColor)
    #context.rect(W/2, H/2, W/2, W/2)

    # Draw frame on the text
    #x = W / 2 # Left side of the frame
    #y = H / 2 # Bottom position

    x = W / 2 - bs.tw / 2 # Left side of the frame

    # Draw the string, centered/baseline in middle of the page.
    #context.text(bs, (x, y))
    #context.drawString(bs, (W/2, H/2))
    context.drawString(bs, (x, y))
    r = 2
    x = pt(x)
    y = pt(y)
    r = pt(r)
    context.text('context.drawString(bs, (%d, %d))' % (x, y), (x, y - P))

    context.marker(x, y, r=r, fontSize=pt(10), prefix=fontName)
    context.fill(None)
    context.stroke((0, 0, 0.5))
    #print(fontName, bs.th)

    tw, th0 = context.textSize(bs, ascDesc=False)
    context.rect(x, y + bs.topLineDescender, tw, th0)
    msg = 'font size (%s) x leading (%s) = %s' % (fontSize, leading, th0)
    y0 = y + bs.topLineDescender + th0
    context.drawString(msg, (x, y0))

    context.stroke((0, 0.5, 0.0))
    tw, th1 = context.textSize(bs, ascDesc=True)
    context.rect(x, y + bs.topLineDescender, tw, th1)
    x3 = x + tw + 20
    y3 = y + bs.topLineDescender + th1
    context.drawString('asc-desc = %s' % th1, (x3, y3))

    msg = 'y = %s' % y
    context.drawString(msg, (x3, y))

    context.stroke((1, 0, 0))
    line = bs.lines[0]
    p1 = (x, y)
    p2 = (x + bs.tw, y)
    context.line(p1, p2)

    context.stroke((0, 1, 0))
    x1 = x + bs.tw + 10
    y1 = y + bs.ascender
    p3 = (x1, y)
    p4 = (x1, y1)
    context.line(p3, p4)
    x2 = x1 + 10
    y2 = y + ((y1 - y) / 2)
    context.drawString('ascender = %s' % bs.ascender, (x2, y2))

    context.stroke((0, 0, 1))
    y1 = y + bs.descender
    p3 = (x1, y)
    p4 = (x1, y1)
    context.line(p3, p4)
    x2 = x1 + 10
    y2 = y + ((y1 - y) / 2)
    context.drawString('descender = %s' % bs.descender, (x2, y2))
    return th0

for contextName in ('DrawBot', 'Flat'):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    context.newPage(W, H) # Make a new A4 page.
    P = 20
    y = 4*P
    for (h, fontName) in ((100, 'PageBot-Regular'), (300, 'Roboto-Regular'), (500, 'Bungee-Regular')):
        # Define font, fontSize and color of the square
        h = draw(context, contextName, y, fontName)
        y += h + P
    context.saveImage(exportPath)
