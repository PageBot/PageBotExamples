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
from pagebot.elements import newText, newRect, newLine
from pagebot.toolbox.color import color
from pagebot.toolbox.loremipsum import loremIpsum
from pagebot.toolbox.units import pt, em
from pagebot.toolbox.transformer import path2FileName
from pagebot.document import Document

H, W = A4 # Standard paper size from constants.
FILENAME = path2FileName(__file__)
LOREM_IPSUM = loremIpsum()
P = 10

def draw(contextName, fontName):
    fontSize = pt(64)
    exportPath = '%s/%s-%s-%s.pdf' % (EXPORT, FILENAME, fontName, contextName)
    context = getContext(contextName)
    padding = pt(40) # Outside measures to accommodate the crop makrs.
    bgColor = color(0.9) # Background color of the text box
    black = color(0)
    context.newDrawing(w=W, h=H)
    context.newPage(W, H) # Make a new A4 page.

    # Define font, fontSize and color of the square
    textColor = color(1, 0, 0)

    # Define the style of the text, alignment is centered on baseline.
    style = dict(font=fontName, fontSize=fontSize,# tracking=-em(0.02),
            leading=em(1), textFill=0) #, xTextAlign=CENTER)

    # Have the context create a BabelString with the style.
    bs = context.newString(LOREM_IPSUM, style=style)
    #print(bs.h)

    x = pt(20)
    y = pt(H / 2)
    r = 2
    w = pt(400)
    h = 200
    r = pt(r)


    # This doesn't give the same results.
    #context.drawString(bs, (x, y))
    context.text('context.drawText(bs, (%d, %d, %d, %d))' % (x, y ,w, h), (x, y - P))
    context.drawText(bs, (x, y, w, h))
    context.marker(x, y, r=r, fontSize=pt(10))
    context.fill(None)
    context.stroke((0, 1, 0))
    context.rect(x, y, w, h)
    context.stroke((1, 0, 0))
    context.strokeWidth(1)
    context.rect(x, y, w, h)
    #context.rect(x, y, bs.w, bs.h)

    for i, line in enumerate(bs.lines):
        yLine = line.y
        if yLine > h:
            break

        yLine = y + h - yLine
        context.marker(x+w, yLine, r=r, fontSize=pt(6), prefix='#%d: %s' % (i, str(line.y)))
        context.stroke((1, 0, 0))
        context.line((x, yLine), (x+w, yLine))

    context.saveImage(exportPath)
    print('* Saved', exportPath)
    context.clear()

for contextName in ('DrawBot', 'Flat'):
    for fontName in ('PageBot-Regular', 'Roboto-Regular', 'Bungee-Regular'):
        draw(contextName, fontName)
