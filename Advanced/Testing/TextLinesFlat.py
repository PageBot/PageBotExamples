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
x = 0
y = 0
context.text('(%s, %s)' % (x, y), (x, y))

b = blurb.getBlurb('stylewars_documentary')[:200]
font = findFont('Bungee-Regular')
style = dict(font=font, fontSize=pt(18), textFill=color(0.5, 1, 0))
bs = context.newString(b, style=style)
lines = bs.getTextLines(w=wbox, h=hbox)

print(lines)

context.fill(None)
context.stroke(f)
x = W / 2
y = H - hbox
context.text('(%s, %s)' % (x, y), (x, y))
context.textBox(bs, (W/2, H - hbox, wbox, hbox))
context.rect(W/2, H - hbox, wbox, hbox)
context.textBox(bs, (PADDING, H - hbox, wbox, hbox))
#context.textBox(bs, (PADDING, 0, wbox, hbox))
context.rect(PADDING, 0, wbox, hbox)

path = '_export/TextLines-%s.pdf' % context.name
context.saveImage(path)
