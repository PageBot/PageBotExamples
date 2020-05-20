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
#     E03_TextSize.py
#
import os
from flat import rgb, font, shape, strike, document, paragraph, text
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.loremipsum import loremipsum

EXPORT_PATH = '_export/03_TextSize.pdf'
if not os.path.exists('_export'):
	os.mkdir('_export')

# Get the PageFont instance
pbFont = findFont('Georgia')
#pbFont = findFont('Verdana')
#pbFont = findFont('PageBot-Bold')
#pbFont = findFont('PageBot-Book')
#pbFont = findFont('Times New Roman')
#pbFont = findFont('Stickway-Bold')
#pbFont = findFont('ResponderP-Black')
fontSize = 100
fontSize3 = fontSize*3
red = rgb(255, 0, 50)
black = rgb(0, 0, 0)
flatFont = font.open(pbFont.path)

figure = shape().stroke(black).width(1)

W, H = 1000, 1000

# Flat has origin in top-left
flatDoc = document(W, H, 'pt')
flatPage = flatDoc.addpage()

txt = loremipsum()

P = 80 # Page padding
x = P

# Size of a string
y = H/2-2*P # Padding from above.
strk = strike(flatFont).color(red).size(fontSize3, leading=0).tracking(0)
paragraphs = [paragraph([strk.span('Hkpx')])]
placedText = flatPage.place(text(paragraphs))
# Placing as frame seems to give better control on vertical position.
#placedText.position(x, y) # Placing on baseline
ascender = fontSize3*pbFont.info.typoAscender/pbFont.info.unitsPerEm
# Baseline of the blox on M from top-left
placedText.frame(x, y-ascender, W-2*P, fontSize3)
flatPage.place(figure.rectangle(x, y-20, 20, 20))
# Draw rectangle of calculated width/height
flatPage.place(figure.rectangle(x, y-ascender, placedText.width, placedText.height))

# Size of a text box.
# Text has to be split, not to contain newlines, into paragraphs.
y = H/2+P # Flat has origin on top left
paragraphs = []
for txtParagraph in txt.split('\n'):
    strk = strike(flatFont).color(red).size(fontSize, leading=fontSize)
    paragraphs.append(paragraph([strk.span(txtParagraph)]))
placedText = flatPage.place(text(paragraphs))
# Placing as frame seems to give better control on vertical position.
#placedText.position(x, y) # Placing on baseline
ascender = fontSize*pbFont.info.typoAscender/pbFont.info.unitsPerEm
# Baseline of the blox on M from top-left
placedText.frame(x, y-ascender, W-2*P, 4*fontSize)
# Show baseline of the first line of the text box
flatPage.place(figure.rectangle(x, y-20, 20, 20))
# Fontsize is now distance to the next line
flatPage.place(figure.rectangle(x, y, fontSize, fontSize))
flatPage.place(figure.rectangle(x+fontSize, y+fontSize, fontSize, fontSize))
flatPage.place(figure.rectangle(x+2*fontSize, y+2*fontSize, fontSize, fontSize))

yy = None
for height, run in placedText.layout.runs():
	if yy is None:
		yy = y
	else:
		yy += height
	flatPage.place(figure.rectangle(x-P/2, yy, P, 0))

# Shifted by ascender is the CSS box around the line.
flatPage.place(figure.rectangle(x+3*fontSize, y-ascender, fontSize, fontSize))
flatPage.place(figure.rectangle(x+4*fontSize, y+fontSize-ascender, fontSize, fontSize))
flatPage.place(figure.rectangle(x+5*fontSize, y+2*fontSize-ascender, fontSize, fontSize))
flatPage.place(figure.rectangle(x+6*fontSize, y+3*fontSize-ascender, fontSize, fontSize))
# Draw rectangle of calculated width/height, different from 4xfontSize
flatPage.place(figure.rectangle(x, y-ascender, placedText.width, placedText.height))

flatDoc.pdf(EXPORT_PATH)

print('Done')
