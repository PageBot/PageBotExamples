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
LINE = 29.2
PADDING = 6
f = Color(1, 0, 0)
wbox = 300
hbox = 400

blurb = Blurb()
context = getContext('Flat')
context.newDrawing()
context.newPage(W, H)
b = blurb.getBlurb('stylewars_documentary')[:200]
font = findFont('Bungee-Regular')
style = dict(font=font, fontSize=pt(18), textFill=color(0.5, 1, 0))
bs = context.newString(b, style=style)
lines = bs.getTextLines(w=wbox, h=hbox)

print(lines)
#context.fill(None)
#context.stroke(f)
#context.rect(PADDING, H, wbox, -hbox)
#context.fill(f)

'''
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
'''

context.fill(None)
context.stroke(f)
context.textBox(bs, (W/2, H - hbox, wbox, hbox))
context.rect(W/2, H - hbox, wbox, hbox)
#context.textBox(bs, (PADDING, 0, wbox, hbox))
#context.rect(PADDING, 0, wbox, hbox)

path = '_export/TextLines-%s.pdf' % context.name
context.saveImage(path)
