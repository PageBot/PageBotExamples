#!/usr/bin/env python3

from pagebot.fonttoolbox.objects.font import findFont
from pagebot.constants import A5
from pagebot.toolbox.units import pt
from pagebot.contributions.filibuster.blurb import Blurb
from flat import * # rgb, font, shape, strike, document
import random

w, h = pt(A5)
w = int(w)
h = int(h)

red = rgb(255, 0, 0)
black = rgb(0, 0, 0)
bungee = findFont('Bungee-Regular')
bungeeFlat = font.open(bungee.path)

blurb = Blurb()
types = blurb.getBlurbTypes()

txts = []

for i in range(5):
    i = random.randint(0, len(types))
    t = types[i]
    print(t)
    txts.append(blurb.getBlurb(t, noTags=True))

txt = '. '.join(txts)
#print(txt)
headline = strike(bungeeFlat).color(red).size(20, 24)
body = strike(bungeeFlat).color(black).size(10, 12)

redStroke = shape().stroke(red).width(0.5)
blackFill = shape().nostroke().fill(black)
blackStroke = shape().stroke(black).width(0.2)

d = document(w, h, 'pt')
d.meta('hello')
p = d.addpage()
p.place(redStroke.circle(50, 50, 20))
p.place(blackFill.rectangle(200, 200, 20, 40))

p.place(headline.text('Hello world!'))#.frame(10, 10, 170, 80)
w = headline.width('Hello world!')
p.place(redStroke.line(0, 24, 0+w, 24))
print(w)

w = 200
h = 100
x = 20
y = 100
placedText = p.place(body.text(txt)).frame(x, y, w, h)
print(placedText.overflow())

p.place(blackStroke.rectangle(x, y, w, h))

# Export.

p.image(kind='rgb').png('_export/hello.png')
p.svg('_export/hello.svg')
d.pdf('_export/hello.pdf')
