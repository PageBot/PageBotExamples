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
#     E02_TextSizeSimple.py
#
#     This example shows the basics of the Flat library, without
#     the use of PageBot document, pages and components.
#
#     Calculate the text of a block, before doc/page are created,
#     to the (w, h) of content can be used to size the page.
#
import os
from flat import rgb, font, shape, strike, document, paragraph, text
from flat.misc import inf
from pagebot.fonttoolbox.objects.font import findFont

EXPORT_PATH = '_export/02_TextSizeSimple.pdf'
if not os.path.exists('_export'):
	os.mkdir('_export')

# Font the PageBot Font instance
pbFont = findFont('PageBot-Regular')
flatFont = font.open(pbFont.path) # Make a Flat font.
fontSize = 100
leading = fontSize*1.2
red = rgb(255, 20, 100)
green = rgb(20, 160, 100)
blue = rgb(20, 100, 255)
black = rgb(0, 0, 0)

# Holds figure style information
figure = shape().stroke(black).width(0.5)

# Strikes for the paragraphs
st1 = strike(flatFont)
st1.color(red).size(fontSize, leading=0)
st2 = strike(flatFont)
st2.color(green).size(fontSize+100)
st3 = strike(flatFont)
st3.color(blue).size(fontSize+200)

S = 'Hkpx'
P = 50 # Padding
R = 20 # radius of origin marker

paragraphs = [
	st1.paragraph(S),
	st2.paragraph(S),
	st3.paragraph(S),
]
tx = text(paragraphs)
# Make a placedText, without binding to document or page.
pt = tx.placed(1)

# Get the bounding box of this placedText,
# so we can use the (w, h) to create the doc/page size.
w = h = 0
# Find the max width of the paragraph, 
# so they with on the page
for p in paragraphs:
	for span in p.spans:
		# Loop through boundary generators
		for tw, th, _ in span.boundaries(0):
			w = max(w, tw)
# Find the max height of the lines
pt.frame(0, 0, w, inf)
for lIndex, (height, _) in enumerate(pt.layout.runs()):
	if lIndex >= 0:
		h += height

# Create document with the calculated size
fDoc = document(w+2*P, h, 'pt') # Size of text + padding around
fPage = fDoc.addpage()

x, y = P, P+st1.style.ascender()
pt = fPage.place(tx) # Make PlacedText
pt.position(x, y) # Placing on baseline

# Cross hair marker on text origin
fPage.place(figure.circle(x, y, R))
fPage.place(figure.line(x-R, y, x+R, y))
fPage.place(figure.line(x, y-R, x, y+R))

print('Items on the page:', len(fPage.items))

# Export the document to PDF
fDoc.pdf(EXPORT_PATH)

print('Done', EXPORT_PATH)
