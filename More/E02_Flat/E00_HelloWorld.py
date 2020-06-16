#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2017 Thom Janssen <https://github.com/thomgb>
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E00_HelloWorld.py
#
#	  This examples creates a Hello world" file, by just using
#     Flat functions.
#
import os
from flat import rgb, font, shape, strike, document
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.constants import DEFAULT_FONT

EXPORT_PATH = '_export/00_HelloWorld'
if not os.path.exists('_export'):
	os.mkdir('_export')

red = rgb(255, 0, 100)

pagebotFont = findFont(DEFAULT_FONT)
flatFont = font.open(pagebotFont.path)
#flatFont = font.open('/Library/Fonts/Georgia Bold.ttf')
figure = shape().stroke(red).width(2.5)
headline = strike(flatFont).color(red).size(20, 24)

d = document(100, 100, 'mm')
p = d.addpage()
p.place(figure.circle(50, 50, 20))
p.place(headline.text('Hello world!')).frame(10, 10, 80, 80)
p.image(kind='rgb').png(EXPORT_PATH + '.png') # Export the page
p.svg(EXPORT_PATH + '.svg') # Export the page 
d.pdf(EXPORT_PATH + '.pdf') # Export the document

print('Done', EXPORT_PATH)