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


def draw(fontName, fontSize, leading):
    w = 400
    h = 200
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, fontName)
    context = getContext('DrawBot')
    context.newDrawing()
    context.newPage(w, h)
    style = dict(font=fontName, fontSize=fontSize, leading=leading)
    #style = dict(font='PageBot-Regular', fontSize=pt(16), leading=em(1))
    bs = context.newString(loremIpsum, style=style)
    lines = bs.lines
    fs = bs.cs
    attrString = fs.getNSObject()
    setter = CTFramesetterCreateWithAttributedString(attrString)
    path = CGPathCreateMutable()
    x = 0
    y = 0
    r = 2
    CGPathAddRect(path, None, CGRectMake(x, y, w, h))
    ctBox = CTFramesetterCreateFrame(setter, (x, y), path, None)
    ctLines = CTFrameGetLines(ctBox)
    origins = CTFrameGetLineOrigins(ctBox, (0, len(ctLines)), None)
    #print(origins)

    context.drawText(bs, (x, y, w, h))


    offsetY = h - origins[-1].y - origins[0].y
    print(offsetY)
    for origin in origins:
        yLine = origin.y#y + h - origin.y
        p1 = (x, yLine)
        p2 = (x + bs.tw, yLine)
        context.stroke((1, 0, 0))
        context.line(p1, p2)
        context.marker(x, yLine, r=r, fontSize=pt(5))
    context.saveImage(exportPath)
    context.clear()


for fontName in ('Roboto-Regular', 'PageBot-Regular', 'Bungee-Regular'):
    fontSize=16
    leading=em(1.5)
    draw(fontName, fontSize, leading)
