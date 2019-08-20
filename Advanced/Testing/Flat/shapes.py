#!/usr/bin/env python3

from pagebot.fonttoolbox.objects.font import findFont
from pagebot.constants import A5
from pagebot.toolbox.units import pt
from flat import *
import random

documentName = 'shapes'
w, h = pt(A5)
w = int(w)
h = int(h)

# Colors.

red = rgb(255, 0, 0)
green = rgb(0, 255, 0)
blue = rgb(0, 0, 255)
black = rgb(0, 0, 0)
white = rgb(255, 255, 255)

# Strokes.

strokeWidth = 0.5
redStroke = shape().stroke(red).width(strokeWidth)
greenStroke = shape().stroke(green).width(strokeWidth)
blueStroke = shape().stroke(blue).width(strokeWidth)
blackStroke = shape().stroke(black).width(strokeWidth)
whiteStroke = shape().stroke(white).width(strokeWidth)

# Fills.

blackFill = shape().nostroke().fill(black)
whiteFill = shape().nostroke().fill(white)

padding = 10
w0 = w - 2 * padding
h0 = h - 2 * padding
x = padding
y = padding

sq = 100
radius = sq / 2

d = document(w, h, 'pt')
d.meta(documentName)
p = d.addpage()

p.place(blackFill.rectangle(0, 0, w, h))
p.place(redStroke.circle(x + radius, y + radius, radius))
p.place(greenStroke.ellipse(x + radius, y + radius, radius *0.7, radius))
p.place(blueStroke.ellipse(x + radius, y + radius, radius, radius * 0.7))
p.place(whiteStroke.rectangle(x, y, sq, sq))

# Export.

p.image(kind='rgb').png('_export/%s.png' % documentName)
p.svg('_export/%s.svg' % documentName)
d.pdf('_export/%s.pdf' % documentName)
