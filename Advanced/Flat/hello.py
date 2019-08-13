#!/usr/bin/env python3

from pagebot.fonttoolbox.objects.font import findFont
from pagebot.constants import A5
from pagebot.toolbox.units import pt
from pagebot.contributions.filibuster.blurb import Blurb
from flat import * # rgb, font, shape, strike, document

w, h = pt(A5)
w = int(w)
h = int(h)

red = rgb(255, 0, 0)
black = rgb(0, 0, 0)
bungee = findFont('Bungee-Regular')
bungeeFlat = font.open(bungee.path)

blurb = Blurb()
txt = blurb.getBlurb('news_headline', noTags=True)

headline = strike(bungeeFlat).color(red).size(20, 24)
body = strike(bungeeFlat).color(black).size(12, 14)
#p = paragraph('bla bla bla')

figure = shape().stroke(red).width(2.5)

d = document(w, h, 'pt')
d.meta('hello')
p = d.addpage()
p.place(figure.circle(50, 50, 20))
p.place(headline.text('Hello world!')).frame(10, 10, 80, 80)
p.place(body.text(txt)).frame(100, 100, 100, 100)

# Export.
p.image(kind='rgb').png('hello.png')
p.svg('hello.svg')
d.pdf('hello.pdf')
