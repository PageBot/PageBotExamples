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

red = rgb(255, 0, 0)
black = rgb(0, 0, 0)
white = rgb(255, 255, 255)
bungee = findFont('Bungee-Regular')
bungeeFlat = font.open(bungee.path)
cotg = '../../docs/stylewars/dondi-white-children-of-the-grave-pt3-martha-cooper.png'
i = image.open(cotg)
print(i.kind)

line = 12
blurb = Blurb()

title = blurb.getBlurb('stylewars_original')
txt = blurb.getBlurb('stylewars_documentary')
headline = strike(bungeeFlat).color(red).size(20, 24)
body = strike(bungeeFlat).color(white).size(10, 12)

redStroke = shape().stroke(red).width(0.5)
blackFill = shape().nostroke().fill(black)
blackStroke = shape().stroke(black).width(0.2)
whiteFill = shape().nostroke().fill(white)

d = document(w, h, 'pt')
d.meta(documentName)
p = d.addpage()
p.place(redStroke.circle(50, 50, 20))
padding = 10
w0 = w - 2* padding
h0 = h - 2 * padding
x = padding
y = padding

p.place(i)
p.place(blackFill.rectangle(padding, padding, w0, 24))
p.place(headline.text(title)).frame(padding, padding, w0, 24)
y += 24

#p.place(blackStroke.rectangle(x, y, w0, h0))
#p.place(whiteFill.rectangle(x, y, w0, h0))
t0 = body.text(txt)
strikeWidth = body.width(txt)
print(strikeWidth/ w0)
placedText = p.place(t0).frame(x, y, w0, h0 - y)

of = placedText.overflow()
lines = len(placedText.lines())
print(lines)
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


# Export.
export = '_export'
p.image(kind='rgb').png('%s/%s.png' % (export, documentName))
p.svg('%s/%s.svg' % (export, documentName))
d.pdf('%s/%s.pdf' % (export, documentName))
