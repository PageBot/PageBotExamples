#!/usr/bin/env python3

from pagebot.fonttoolbox.objects.font import findFont
from flat import rgb, font, shape, strike, document

roboto = findFont('Bungee-Regular')
print('bla')
print(roboto)
red = rgb(255, 0, 0)
print(roboto.path)
lato = font.open(roboto.path)
figure = shape().stroke(red).width(2.5)
headline = strike(lato).color(red).size(20, 24)

d = document(100, 100, 'mm')
p = d.addpage()
p.place(figure.circle(50, 50, 20))
p.place(headline.text('Hello world!')).frame(10, 10, 80, 80)
p.image(kind='rgb').png('hello.png')
p.svg('hello.svg')
d.pdf('hello.pdf')
