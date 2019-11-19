#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
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
LINE = 25.2
PADDING = 6
f = Color(1, 0, 0)
wbox = 300
hbox = 1200

blurb = Blurb()
context = getContext('DrawBot')
context.newDrawing()
context.newPage(W, H)
b = blurb.getBlurb('stylewars_documentary')
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
context.fill(f)

for p in origins:
    context.circle(PADDING + p.x + 2, H - (p.y + 2), 4)

y = H - LINE

for line in lines:
    for run in line.textRuns:
        print(run.attrs)
        #print(run.string)
        s = context.newString(run.string, style=style)
        context.text(s, (PADDING, y))
        context.stroke(f)
        p0 = (PADDING, y)
        p1 = (PADDING + wbox, y)
        context.line(p0, p1)

    y -= LINE

path = '_export/TextLines-%s.pdf' % context.name
context.saveImage(path)
