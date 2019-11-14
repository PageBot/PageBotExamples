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
documentName = 'layout'

# Colors.
red = rgb(255, 0, 0)
black = rgb(0, 0, 0)
white = rgb(255, 255, 255)

# Fonts.
f = findFont('Bungee-Regular')
bungee = font.open(f.path)
f = findFont('Bungee-OutlineRegular')
bungeeOutline = font.open(f.path)
f = findFont('PageBot-Book')
pageBotBook = font.open(f.path)


line = 12
blurb = Blurb()

h1Outline = strike(bungeeOutline).color(red).size(20, 24)
h1 = strike(bungee).color(black).size(20, 24)
intro = strike(bungee).color(black).size(10, 12)
body = strike(pageBotBook).color(black).size(16, 18)

title = blurb.getBlurb('stylewars_original')
txt = blurb.getBlurb('stylewars_documentary')

redStroke = shape().stroke(red).width(0.5)
blackFill = shape().nostroke().fill(black)
blackStroke = shape().stroke(black).width(0.2)
whiteFill = shape().nostroke().fill(white)

d = document(w, h, 'pt')
d.meta(documentName)
p = d.addpage()
padding = 10
w0 = w - 2 * padding
h0 = h - 2 * padding
x = padding
y = padding

p.place(h1.text(title)).frame(padding, padding, w0, 24)
p.place(h1Outline.text(title)).frame(padding, padding, w0, 24)
y += 24

#p.place(blackStroke.rectangle(x, y, w0, h0))
#p.place(whiteFill.rectangle(x, y, w0, h0))
t0 = intro.text(txt)
strikeWidth = intro.width(txt)
print(strikeWidth / w0)
placedText = p.place(t0).frame(x, y, w0, h0 - y)

of = placedText.overflow()
lines = len(placedText.lines())
textHeight = (lines+1) * 12
y += textHeight

t2 = blurb.getBlurb('stylewars_bluray')
placedText = p.place(body.text(t2)).frame(x, y, w0, h0 - y)
import difflib

if placedText.overflow():
    usedText = ''.join(placedText.lines())
    unusedText = ''

    for i,s in enumerate(difflib.ndiff(t2, usedText)):
        if s[0]==' ': continue
        elif s[0]=='-':
            unusedText += s[-1]
            #print(u'Delete "{}" from position {}'.format(s[-1],i))
        elif s[0]=='+':
            print(u'Add "{}" to position {}'.format(s[-1],i))

    print(unusedText)
    p1 = d.addpage()
    x = padding
    y = padding
    placedText = p1.place(body.text(unusedText)).frame(x, y, w0, h0 - y)

# Export.
export = '_export'
p.image(kind='rgb').png('%s/%s.png' % (export, documentName))
p.svg('%s/%s.svg' % (export, documentName))
d.pdf('%s/%s.pdf' % (export, documentName))
