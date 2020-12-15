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
from pagebot.toolbox.loremipsum import loremIpsum
from pagebot.toolbox.transformer import path2FileName
FILENAME = path2FileName(__file__)
loremIpsum = loremIpsum()
W = 1500
H = 1000
P = 10
R = 2

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
    dbBaselines = textBoxBaselines(fs, box)

    # TODO: compare to pagebot textBox.
    #context.drawString(bs, (x, H-y))
    context.drawText(bs, (x, -y, W, H))
    pbBaselines = bs.getTextLines()

    # (Native OSX) origins.
    for i, origin in enumerate(origins):
        # baseline origin.
        # Offset from top of textbox.
        dy0 = bs.th - (origin.y)
        # Abs value.
        y0 = H - y - dy0
        x0 = x + bs.tw / 2
        x1 = x + bs.tw
        p1 = (x0, y0)
        p2 = (x1, y0)
        context.stroke((1, 0, 0))
        context.line(p1, p2)
        prefix = '# %s: %dpt from top, %dpt from below' % (i, dy0, origin.y)
        context.marker(x1, y0, r=R, fontSize=pt(5), prefix=prefix)

        context.stroke((0, 0, 1))
        x0 = x - 5
        y1 = y0 + bs.descender
        x2 = x
        y2 = y1 + (y0 - y1) / 2
        p0 = (x0, y0)
        p1 = (x0, y1)
        context.line(p0, p1)
        #context.text('descender = %s' % bs.descender, (x2, y2))

        context.stroke((0, 1, 0))
        x0 = x - 5
        y1 = y0 + bs.ascender
        x2 = x
        y2 = y1 + (y0 - y1) / 2
        p0 = (x0, y0)
        p1 = (x0, y1)
        context.line(p0, p1)
        #context.text('ascender = %s' % bs.ascender, (x2, y2))

        #yBaseline = dbBaselines[i][1]
        yBaseline = pbBaselines[i].y
        # Offset from top of textbox.
        y1 = H - y - yBaseline
        x0 = x
        x1 = x + bs.tw / 2
        p3 = (x0, y1)
        p4 = (x1, y1)
        context.stroke((0, 1, 0))
        context.line(p3, p4)
        prefix = '# %s: %dpt from top' % (i, yBaseline)
        context.marker(x1, y1, r=R, fontSize=pt(5), color=(0, 1, 0), prefix=prefix)

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
    exportPath = '%s/%s-%s.pdf' % (EXPORT, fontName, FILENAME)
    context = getContext('DrawBot')
    context.newDrawing()
    context.newPage(W, H)
    drawWord(context, P, P, 'Hh', fontSize, leading)
    drawWord(context, W/3, 5*P, 'Hp\nxk', fontSize, leading)
    drawWord(context, W/3*2, 10*P, 'Hp\nXx\nKk', fontSize, leading)
    context.saveImage(exportPath)
    context.clear()

for fontName in ('PageBot-Regular', 'Roboto-Regular', 'Bungee-Regular'):
    fontSize=200
    leading=1.2
    draw(fontName, fontSize, leading)
