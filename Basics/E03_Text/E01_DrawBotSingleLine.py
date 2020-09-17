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
#     DrawBotTextLines.py
#
#     DrawBot only example to test text lines.

from CoreText import (CTFontDescriptorCreateWithNameAndSize, CGPathAddRect,
        CTFramesetterCreateWithAttributedString, CGPathCreateMutable,
        CTFramesetterCreateFrame, CTFrameGetLines, CTFrameGetLineOrigins,
        CTFontDescriptorCopyAttribute, kCTFontURLAttribute, CGRectMake,
        CTLineGetGlyphRuns, CTRunGetAttributes)
from AppKit import NSFont

from pagebot import getContext
from pagebot.constants import *
from pagebot.toolbox.units import pt, em
from pagebot.toolbox.loremipsum import loremipsum
from pagebot.toolbox.transformer import path2FileName
FILENAME = path2FileName(__file__)
loremIpsum = loremipsum()
W = 800
H = 800
P = 10
TOPBASELINE = 30*P
FONTSIZE = 200
LEADING = 1.3

def drawWord(context, x, y, word, fontSize, leading):
    style = dict(font=fontName, fontSize=fontSize, leading=em(leading))
    bs = context.newString(word, style=style)
    fs = bs.cs
    attrString = fs.getNSObject()
    setter = CTFramesetterCreateWithAttributedString(attrString)
    path = CGPathCreateMutable()
    r = 2
    CGPathAddRect(path, None, CGRectMake(0, 0, W, H))
    ctBox = CTFramesetterCreateFrame(setter, (0, 0), path, None)
    ctLines = CTFrameGetLines(ctBox)
    origins = CTFrameGetLineOrigins(ctBox, (0, len(ctLines)), None)
    #context.drawText(bs, (x, y, W, H))
    context.drawString(bs, (x, y))

    for i, origin in enumerate(origins):
        # Baseline.
        yLine = origin.y + y
        p1 = (x, yLine)
        x1 = x + bs.tw
        p2 = (x1, yLine)
        context.stroke((1, 0, 0))
        context.line(p1, p2)
        yFromTop = H - yLine - y
        context.marker(x1, yLine, r=r, fontSize=pt(5), prefix='# %s = %dpt from top' % (i, yFromTop))

    # Total text height.
    context.stroke((0, 0, 1))
    x0 = x + bs.tw + P
    y1 = y + bs.topLineDescender
    y0 = y1 + bs.th
    y2 = y0 + (y1 - y0) / 2

    p0 = (x0, y0)
    p1 = (x0, y1)
    p2 = (x0 + P/2, y2)
    context.line(p0, p1)
    context.marker(x0, y0, prefix='p0: (%d, %d)' % p0)
    context.marker(x0, y1, prefix='p1: (%d, %d)' % p1)
    context.text('bs.th = %dpt' % bs.th, p2)

    x0 = x
    x1 = x + bs.tw
    x2 = x0 + (x0 + x1) / 2
    y3 = H - y - bs.th - P
    y4 = y3 - P
    p0 = (x0, y3)
    p1 = (x1, y3)
    p2 = (x2, y4)
    context.line(p0, p1)
    context.text('bs.tw = %dpt' % bs.tw, p2)

    context.fill(None)
    context.stroke((1, 0, 1))
    context.rect(x, y1, bs.tw, bs.th)

def draw(fontName, fontSize, leading):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, fontName)
    context = getContext('DrawBot')
    context.newDrawing()
    context.newPage(W, H)
    drawWord(context, P, H-TOPBASELINE, 'Hp', fontSize, leading)
    drawWord(context, W/2, H-TOPBASELINE, 'xk', fontSize, leading)
    context.stroke((0, 0, 1))
    p0, p1 = (0, H-TOPBASELINE), (W, H-TOPBASELINE)
    context.line(p0, p1)
    context.saveImage(exportPath)
    context.clear()

for fontName in ('Roboto-Regular','PageBot-Regular', 'Bungee-Regular'):
    fontSize=FONTSIZE
    leading=LEADING
    draw(fontName, fontSize, leading)
