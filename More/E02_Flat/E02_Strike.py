#!/usr/bin/env python3
#
#     Copyright (c) 2017 Thom Janssen <https://github.com/thomgb>
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E02_Strike.py
#
#     This example shows the basics of the Flat library, without
#     the use of PageBot document, pages and components.
#
#     Show the role of strike in the generation of a page.
#     Basically the strike is the seed of style information 
#     for spans, paragraphs and text generated from it.
#
#     st = strike(flatFont).color(red).size(fontSize, leading=0)
#
import os
from flat import rgb, font, shape, strike, document, paragraph, text
from pagebot.fonttoolbox.objects.font import findFont

EXPORT_PATH = '_export/02_Strike.pdf'
if not os.path.exists('_export'):
	os.mkdir('_export')

# Font the PageBot Font instance
pbFont = findFont('PageBot-Regular')
flatFont = font.open(pbFont.path) # Make a Flat font.
fontSize = 200
red = rgb(255, 20, 100)
black = rgb(0, 0, 0)

figure = shape().stroke(black).width(0.5)
st = strike(flatFont)
# Set additional attributes of the strike as chained call.
st.color(red).size(fontSize, leading=0).tracking(0)

S = 'Hkpx'
P = 50 # Padding
R = 20 # radius of origin marker

# Flat has origin in top-left
w = st.width(S)+2*P # Calculated with to fit the string + padding
h = st.style.ascender() - st.style.descender() + 2*P
fDoc = document(w, h, 'pt') # Size of text + padding around
fPage = fDoc.addpage()

x, y = P, 200
pt = fPage.place(st.text(S)) # Make PlacedText
pt.position(x, y) # Placing on baseline

# Cross hair marker on text origin
fPage.place(figure.circle(x, y, R))
fPage.place(figure.line(x-R, y, x+R, y))
fPage.place(figure.line(x, y-R, x, y+R))

# Export the document to PDF
fDoc.pdf(EXPORT_PATH)

print('Done', EXPORT_PATH)
