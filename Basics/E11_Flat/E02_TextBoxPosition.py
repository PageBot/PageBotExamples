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
#     E02_TextBoxPosition.py
#
#     This examples creates a Hello world" file, by just using
#     Flat functions.
#

import os
from flat import rgb, font, shape, strike, document, paragraph, text
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.loremipsum import loremipsum

EXPORT_PATH = '_export/02_TextBoxPosition.pdf'
if not os.path.exists('_export'):
	os.mkdir('_export')

# Get the PageFont instance
pbFont = findFont('PageBot-Regular')
fontSize = 24
red = rgb(255, 0, 100)
black = rgb(0, 0, 0)
flatFont = font.open(pbFont.path)

figure = shape().stroke(black).width(1)
strk = strike(flatFont).color(red).size(fontSize, tracking=0.1)

W, H = 1000, 1000

# Flat has origin in top-left
flatDoc = document(W, H, 'pt')
flatPage = flatDoc.addpage()

txt = loremipsum()

# Text has to be split, not to contain newlines, into paragraphs.
M = 80 # Margin
x = M
y = M # Flat has origin on top left
flatPage.place(figure.rectangle(x, y-20, 20, 20))
paragraphs = []
for txtParagraph in txt.split('\n'):
    strk = strike(flatFont).color(red).size(fontSize)
    paragraphs.append(paragraph([strk.span(txtParagraph)]))
placedText = flatPage.place(text(paragraphs))
# Placing as frame seems to give better control on vertical position.
#placedText.position(x, y) # Placing on baseline
ascender = fontSize*pbFont.info.typoAscender/pbFont.info.unitsPerEm
# Baseline of the blox on M from top-left
placedText.frame(x, y-ascender, W-2*M, H-2*M)
flatDoc.pdf(EXPORT_PATH)

print('Done')
