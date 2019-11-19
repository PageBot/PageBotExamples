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

from pagebot import getContext
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.toolbox.units import pt
from pagebot.toolbox.color import color, Color
from pagebot.fonttoolbox.objects.font import findFont

H = 850
W = 652
LINE = 20
PADDING = 6
f = Color(1, 0, 0)

blurb = Blurb()
context = getContext('DrawBot')
context.newDrawing()
context.newPage(W, H)
b = blurb.getBlurb('stylewars_documentary')
font = findFont('Bungee-Regular')
style = dict(font=font, fontSize=pt(18), textFill=color(0.5, 1, 0))
s = context.newString(b, style=style)
lines = s.getTextLines(w=300, h=1200)
print(lines)

y = H - LINE

for line in lines:
    for run in line.textRuns:
        #print(run.string)
        s = context.newString(run.string, style=style)
        context.text(s, (PADDING, y))
        context.stroke(f)
        p0 = (PADDING, y)
        p1 = (PADDING + 300, y)
        context.line(p0, p1)

    y -= LINE

path = '_export/TextLines-%s.pdf' % context.name
context.saveImage(path)
