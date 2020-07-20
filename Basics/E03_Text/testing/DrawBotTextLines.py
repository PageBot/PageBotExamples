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
from pagebot.toolbox.transformer import path2FileName
FILENAME = path2FileName(__file__)


def draw():
    w = 400
    h = 200
    exportPath = '%s/%s.pdf' % (EXPORT, FILENAME)
    context = getContext('DrawBot')
    context.newPage(w, h)
    style = dict(font='PageBot-Regular', fontSize=pt(16), leading=em(1))
    bs = context.newString('Bla', style=style)
    lines = bs.lines
    fs = bs.cs
    attrString = fs.getNSObject()
    setter = CTFramesetterCreateWithAttributedString(attrString)
    path = CGPathCreateMutable()
    x = 0
    y = 0
    CGPathAddRect(path, None, CGRectMake(x, y, w, h))
    ctBox = CTFramesetterCreateFrame(setter, (x, y), path, None)
    ctLines = CTFrameGetLines(ctBox)
    origins = CTFrameGetLineOrigins(ctBox, (0, len(ctLines)), None)
    print(origins)
    context.saveImage(exportPath)

draw()
