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
#     E01_FlatMultiLine.py
#
#     DrawBot only example to test text lines.

from drawBot import textBoxBaselines
from pagebot import getContext
from pagebot.constants import *
from pagebot.toolbox.units import pt, em
from pagebot.toolbox.transformer import path2FileName

FILENAME = path2FileName(__file__)
FONTSIZE = 200
LEADING = 1.2
#LEADING = 2
W = 1500
H = 1000
P = 10
R = 2

def drawWord(context, x, y, word, fontSize, leading):
    style = dict(font=fontName, fontSize=fontSize, leading=em(leading))
    bs = context.newString(word, style=style)
    _, th0 = context.textSize(bs, ascDesc=False)
    diff = th0 - bs.th
    y += diff
    j = bs.ascender - bs.descender

    #context.drawString(bs, (x, 40))
    context.drawText(bs, (x, -y, W, H))
    baselines = bs.getTextLines()

    for i, baseline in enumerate(baselines):
        yBaseline = baseline.y
        # Offset from top of textbox.
        y0 = H - y - yBaseline
        p3 = (x, y0)
        p4 = (x + bs.tw, y0)
        context.stroke((0, 1, 0))
        context.line(p3, p4)

        x0 = x + bs.tw
        prefix = '#%d: %dpt from top' % (i, yBaseline)
        context.marker(x + bs.tw, y0, r=R, fontSize=pt(5), prefix=prefix)

        context.stroke((0, 0, 1))
        x0 = x + bs.tw + 2*P
        x1 = x0 + P/2
        y1 = y0 + bs.descender
        y2 = y1 + (y0 - y1) / 2
        p0 = (x0, y0)
        p1 = (x0, y1)
        context.line(p0, p1)

        context.stroke((0, 1, 0))
        y1 = y0 + bs.ascender
        y2 = y1 + (y0 - y1) / 2
        p0 = (x0, y0)
        p1 = (x0, y1)
        context.line(p0, p1)
        if i == 0:
            context.text('asc-desc = %s' % j, (x1, y1))

    context.text('diff = %s' % diff, (x0, H - y + diff / 2))
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
    n = len(baselines)
    if diff > 0:
        d = (n-1) * diff

        msg += '\n%d * %s + %s == %s' % (n, j, d, bs.th)
    else:
        msg += '\n%d * %s == %s' % (n, j, bs.th)
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

    y0 = H - y
    y1 = y0 - bs.th
    context.fill(None)
    context.stroke((0, 0, 1))
    context.rect(x, y1, bs.tw, th0)
    context.stroke((1, 0, 1))
    context.rect(x, y1, bs.tw, bs.th)

def draw(fontName, fontSize, leading):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, fontName, FILENAME)
    context = getContext('Flat')
    context.newDrawing(w=W, h=H)
    context.newPage(W, H)
    drawWord(context, P, P, 'Hh', fontSize, leading)
    drawWord(context, W/3, 5*P, 'Hp\nxk', fontSize, leading)
    drawWord(context, W/3*2, 10*P, 'Hp\nXx\nKk', fontSize, leading)
    context.saveImage(exportPath)
    context.clear()

for fontName in ('Bungee-Regular', 'PageBot-Regular', 'Roboto-Regular',):
    fontSize=FONTSIZE
    leading=LEADING
    draw(fontName, fontSize, leading)
