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
#     E12_TextSize.py

import os
from flat import rgb, font, shape, strike, document, paragraph, text
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.loremipsum import loremipsum

EXPORT_PATH = '_export/12_TextSize.pdf'

if not os.path.exists('_export'):
	os.mkdir('_export')

W, H = 1000, 1000
R = 20 # radius of origin marker

# Get the PageFont instance
pbFont = findFont('Georgia')
#pbFont = findFont('Verdana')
#pbFont = findFont('PageBot-Bold')
#pbFont = findFont('PageBot-Book')
#pbFont = findFont('Times New Roman')
#pbFont = findFont('Stickway-Bold')
#pbFont = findFont('ResponderP-Black')
flatFont = font.open(pbFont.path)
fontSize = 100
fontSize3 = fontSize*3

red = rgb(255, 0, 50)
black = rgb(0, 0, 0)

figure = shape().stroke(black).width(1)

# Flat has origin in top-left
fDoc = document(W, H, 'pt')
fPage = fDoc.addpage()
txt = loremipsum()
P = 80 # Page padding
x = P

# Size of a string
y = H/2-2*P # Padding from above.
st = strike(flatFont).color(red).size(fontSize3, leading=0).tracking(0)
paragraphs = [paragraph([st.span('Hkpx')])]
placedText = fPage.place(text(paragraphs))
# Placing as frame seems to give better control on vertical position.
#placedText.position(x, y) # Placing on baseline
ascender = fontSize3*pbFont.info.typoAscender/pbFont.info.unitsPerEm
# Baseline of the blox on M from top-left
placedText.frame(x, y-ascender, W-2*P, fontSize3)
# Draw rectangle of calculated width/height
fPage.place(figure.rectangle(x, y-ascender, placedText.width, placedText.height))

# Cross hair marker on text origin
fPage.place(figure.circle(x, y, R))
fPage.place(figure.line(x-R, y, x+R, y))
fPage.place(figure.line(x, y-R, x, y+R))

# Size of a text box.
# Text has to be split, not to contain newlines, into paragraphs.
y = H/2+P # Flat has origin on top left
paragraphs = []
for txtParagraph in txt.split('\n'):
    st = strike(flatFont).color(red).size(fontSize, leading=fontSize)
    paragraphs.append(paragraph([st.span(txtParagraph)]))
placedText = fPage.place(text(paragraphs))
# Placing as frame seems to give better control on vertical position.
#placedText.position(x, y) # Placing on baseline
ascender = fontSize*pbFont.info.typoAscender/pbFont.info.unitsPerEm
# Baseline of the block on M from top-left
placedText.frame(x, y-ascender, W-2*P, 4*fontSize)
# Fontsize is now distance to the next line
fPage.place(figure.rectangle(x, y, fontSize, fontSize))
fPage.place(figure.rectangle(x+fontSize, y+fontSize, fontSize, fontSize))
fPage.place(figure.rectangle(x+2*fontSize, y+2*fontSize, fontSize, fontSize))

yy = y
for lIndex, (height, run) in enumerate(placedText.layout.runs()):
	if lIndex > 0:
		yy += height
	fPage.place(figure.line(x-P/2, yy, x+P/2, yy))

# Shifted by ascender is the CSS box around the line.
fPage.place(figure.rectangle(x+3*fontSize, y-ascender, fontSize, fontSize))
fPage.place(figure.rectangle(x+4*fontSize, y+fontSize-ascender, fontSize, fontSize))
fPage.place(figure.rectangle(x+5*fontSize, y+2*fontSize-ascender, fontSize, fontSize))
fPage.place(figure.rectangle(x+6*fontSize, y+3*fontSize-ascender, fontSize, fontSize))
# Draw rectangle of calculated width/height, different from 4xfontSize
fPage.place(figure.rectangle(x, y-ascender, placedText.width, placedText.height))

# Cross hair marker on text origin
fPage.place(figure.circle(x, y, R))
fPage.place(figure.line(x-R, y, x+R, y))
fPage.place(figure.line(x, y-R, x, y+R))

fDoc.pdf(EXPORT_PATH)

print('Done', EXPORT_PATH)
