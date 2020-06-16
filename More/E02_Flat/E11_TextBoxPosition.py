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
#     E11_TextBoxPosition.py
#
#     This example shows the basics of the Flat library, without
#     the use of PageBot document, pages and components.
#
#     Show the position of a text box.

import os
from flat import rgb, font, shape, strike, document, paragraph, text
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.loremipsum import loremipsum

EXPORT_PATH = '_export/11_TextBoxPosition.pdf'
if not os.path.exists('_export'):
	os.mkdir('_export')

W, H = 1000, 1000
R = 20 # radius of origin marker

# Get the PageFont instance
pbFont = findFont('PageBot-Regular')
flatFont = font.open(pbFont.path)
fontSize = 24

red = rgb(255, 0, 100)
black = rgb(0, 0, 0)

figure = shape().stroke(black).width(1)
st = strike(flatFont).color(red).size(fontSize).tracking(0.1)


# Flat has origin in top-left
fDoc = document(W, H, 'pt')
fPage = fDoc.addpage()

txt = loremipsum()

# Text has to be split, not to contain newlines, into paragraphs.
M = 80 # Margin
x = M
y = M # Flat has origin on top left

paragraphs = []

for txtParagraph in txt.split('\n'):
    st = strike(flatFont).color(red).size(fontSize)
    paragraphs.append(paragraph([st.span(txtParagraph)]))

placedText = fPage.place(text(paragraphs))
# Placing as frame seems to give better control on vertical position.
#placedText.position(x, y) # Placing on baseline
ascender = fontSize*pbFont.info.typoAscender/pbFont.info.unitsPerEm
# Baseline of the blox on M from top-left
placedText.frame(x, y-ascender, W-2*M, H-2*M)

# Cross hair marker on text origin
fPage.place(figure.circle(x, y, R))
fPage.place(figure.line(x-R, y, x+R, y))
fPage.place(figure.line(x, y-R, x, y+R))

fDoc.pdf(EXPORT_PATH)

print('Done', EXPORT_PATH)
