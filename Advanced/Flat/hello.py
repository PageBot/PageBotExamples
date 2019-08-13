#!/usr/bin/env python3

from pagebot.fonttoolbox.objects.font import findFont
from pagebot.constants import A5
from pagebot.toolbox.units import pt
from flat import rgb, font, shape, strike, document
w, h = pt(A5)
w = int(w)
h = int(h)

bungee = findFont('Bungee-Regular')
red = rgb(255, 0, 0)
lato = font.open(bungee.path)
figure = shape().stroke(red).width(2.5)
headline = strike(lato).color(red).size(20, 24)

d = document(w, h, 'pt')
p = d.addpage()
p.place(figure.circle(50, 50, 20))
p.place(headline.text('Hello world!')).frame(10, 10, 80, 80)
p.image(kind='rgb').png('hello.png')
p.svg('hello.svg')
d.pdf('hello.pdf')
