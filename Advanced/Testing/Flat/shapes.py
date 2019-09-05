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
lightBlue = rgb(100, 200, 255)
black = rgb(0, 0, 0)
white = rgb(255, 255, 255)

# Strokes.

strokeWidth = 0.5
redStroke = shape().stroke(red).width(strokeWidth)
greenStroke = shape().stroke(green).width(strokeWidth)
blueStroke = shape().stroke(blue).width(strokeWidth)
lightBlueStroke = shape().stroke(lightBlue).width(strokeWidth)
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
r = sq / 2

d = document(w, h, 'pt')
d.meta(documentName)
p = d.addpage()

p.place(blackFill.rectangle(0, 0, w, h))
p.place(whiteStroke.rectangle(x, y, sq, sq))
p.place(redStroke.circle(x + r, y + r, r))
p.place(greenStroke.ellipse(x + r, y + r, r *0.7, r))
p.place(lightBlueStroke.ellipse(x + r, y + r, r, r * 0.7))

x += sq + padding
p.place(whiteStroke.rectangle(x, y, sq, sq))
p.place(redStroke.line(x, y+r, x+r, y+sq))
p.place(redStroke.line(x+r, y+sq, x+sq, y+r))
p.place(redStroke.line(x+sq, y+r, x+r, y))
p.place(redStroke.line(x+r, y, x, y+r))

x += padding
coordinates = (x, y+r, x+r, y+sq, x+sq, y+r, x+r, y)
p.place(greenStroke.polyline(coordinates))
x -= padding
y += padding
coordinates = (x, y+r, x+r, y+sq, x+sq, y+r, x+r, y)
p.place(lightBlueStroke.polygon(coordinates))

y -= padding
x += sq + padding
p.place(whiteStroke.rectangle(x, y, sq, sq))

offset = 10
commands = (moveto(x, y), lineto(x+r, y+r), curveto(x+r+offset, y+r-offset, x+sq-offset, y+sq+offset, x+sq, y+sq), closepath)
p.place(lightBlueStroke.path(commands))

# Export.

p.image(kind='rgb').png('_export/%s.png' % documentName)
#p.svg('_export/%s.svg' % documentName)
#d.pdf('_export/%s.pdf' % documentName)
