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
#     E00_DrawBotTextLines.py
#
#     DrawBot only example to test text lines.

from CoreText import (CTFontDescriptorCreateWithNameAndSize, CGPathAddRect,
        CTFramesetterCreateWithAttributedString, CGPathCreateMutable,
        CTFramesetterCreateFrame, CTFrameGetLines, CTFrameGetLineOrigins,
        CTFontDescriptorCopyAttribute, kCTFontURLAttribute, CGRectMake,
        CTLineGetGlyphRuns, CTRunGetAttributes)
from AppKit import NSFont


from drawBot import textBoxBaselines
from pagebot import getContext
from pagebot.constants import *
from pagebot.toolbox.units import pt, em
from pagebot.toolbox.loremipsum import loremipsum
from pagebot.toolbox.transformer import path2FileName
FILENAME = path2FileName(__file__)
loremIpsum = loremipsum()
W = 1500
H = 1000
P = 10

def drawWord(context, x, y, word, fontSize, leading):
    style = dict(font=fontName, fontSize=fontSize, leading=em(leading))
    bs = context.newString(word, style=style)
    fs = bs.cs
    attrString = fs.getNSObject()
    setter = CTFramesetterCreateWithAttributedString(attrString)
    path = CGPathCreateMutable()
    r = 2
    CGPathAddRect(path, None, CGRectMake(0, 0, bs.tw, bs.th))
    ctBox = CTFramesetterCreateFrame(setter, (0, 0), path, None)
    ctLines = CTFrameGetLines(ctBox)
    origins = CTFrameGetLineOrigins(ctBox, (0, len(ctLines)), None)

    box = 0, 0, bs.tw, bs.th
    baselines = textBoxBaselines(fs, box)
    context.drawText(bs, (x, -y, W, H))

    # (Native OSX) origins.
    for i, origin in enumerate(origins):
        # Baseline.
        print('origin.y', origin.y)
        # Offset from top of textbox.
        dy = bs.th - (origin.y) + y
        # Abs value.
        y0 = H - dy
        #print('y0', y0)
        p1 = (x + bs.tw / 2, y0)
        p2 = (x + bs.tw, y0)
        context.stroke((1, 0, 0))
        context.line(p1, p2)

        yBaseline = baselines[i][1]
        # Offset from top of textbox.
        dy = bs.th - yBaseline + y
        y1 = H - dy
        p3 = (x, y1)
        p4 = (x + bs.tw / 2, y1)
        context.stroke((0, 1, 0))
        context.line(p3, p4)

        x0 = x + bs.tw
        context.marker(x0, y0, r=r, fontSize=pt(5), prefix='# %s: %dpt from top, %dpt from below' % (i, dy, origin.y))

    # Total text height.
    context.stroke((0, 0, 1))
    x0 = x + bs.tw + P
    y0 = H - y
    y1 = y0 - bs.th
    y2 = y1 + (y0 - y1) / 2

    p0 = (x0, y0)
    p1 = (x0, y1)
    p2 = (x0 + P/2, y2)
    context.line(p0, p1)
    msg = 'bs.th = %dpt' % bs.th
    hTotal = len(origins) * fontSize * leading
    msg += '\n%d * %d * %s == %d' % (len(origins), fontSize, leading, hTotal)
    context.text(msg, p2)

    x0 = x
    x1 = x + bs.tw
    x2 = x0 + (x1 - x0) / 2
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
    drawWord(context, P, P, 'Hh', fontSize, leading)
    drawWord(context, W/3, 5*P, 'Hp\nxk', fontSize, leading)
    drawWord(context, W/3*2, 10*P, 'Hp\nXx\nKk', fontSize, leading)
    context.saveImage(exportPath)
    context.clear()

for fontName in ('PageBot-Regular',):#, 'Roboto-Regular'):#, 'Bungee-Regular'):
    fontSize=200
    leading=1.2
    draw(fontName, fontSize, leading)
