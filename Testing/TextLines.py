#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T  E X A M P L E S
#
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     TextLines.py
#

from CoreText import (CTFramesetterCreateWithAttributedString,
        CTFramesetterCreateFrame, CTFrameGetLines, CTFrameGetLineOrigins,
        CTLineGetGlyphRuns, CTRunGetAttributes)
from Quartz import CGPathAddRect, CGPathCreateMutable, CGRectMake

from pagebot import getContext
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.toolbox.units import pt
from pagebot.toolbox.color import color, Color
from pagebot.fonttoolbox.objects.font import findFont

H = 850
W = 652
LINE = 29.2
PADDING = 6
f = Color(1, 0, 0)
wbox = 300
hbox = 400

blurb = Blurb()
context = getContext('DrawBot')
context.newDrawing()
context.newPage(W, H)
x = 0
y = 0
context.text('(%s, %s)' % (x, y), (x, y))
x = W / 2
y = H - hbox
context.text('(%s, %s)' % (x, y), (x, y))
b = blurb.getBlurb('stylewars_documentary')[:200]
font = findFont('Bungee-Regular')
style = dict(font=font, fontSize=pt(18), textFill=color(0.5, 1, 0))
bs = context.newString(b, style=style)
lines = bs.getTextLines(w=wbox, h=hbox)
attrString = bs.s.getNSObject()
setter = CTFramesetterCreateWithAttributedString(attrString)
path = CGPathCreateMutable()
CGPathAddRect(path, None, CGRectMake(0, 0, wbox, hbox))
ctBox = CTFramesetterCreateFrame(setter, (0, 0), path, None)
ctLines = CTFrameGetLines(ctBox)
origins = CTFrameGetLineOrigins(ctBox, (0, len(ctLines)), None)
context.fill(None)
context.stroke(f)
context.rect(PADDING, H, wbox, -hbox)
context.fill(f)

for p in origins:
    context.circle(PADDING + p.x + 2, (p.y + 2), 4)
    print(p.y)

y = H - LINE

for line in lines:
    for run in line.textRuns:
        #print(run.attrs)
        s = context.newString(run.string, style=style)
        context.text(s, (PADDING, y))
        context.stroke(f)
        p0 = (PADDING, y)
        p1 = (PADDING + wbox, y)
        context.line(p0, p1)

    y -= LINE

context.fill(None)
context.stroke(f)
x = W / 2
y = H - hbox
context.textBox(bs, (x, y, wbox, hbox))
context.rect(W/2, H - hbox, wbox, hbox)
context.textBox(bs, (PADDING, 0, wbox, hbox))
context.fill(None)
context.stroke(f)
context.rect(PADDING, 0, wbox, hbox)
path = '_export/TextLines-%s.pdf' % context.name
context.saveImage(path)
