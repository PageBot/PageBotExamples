#
#     Copyright (c) 2017 Thom Janssen <https://github.com/thomgb>
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E15_MixedBaselines.py
#
#     Show a page filling column with baselines.

import os
from flat import rgb, font, shape, strike, document, paragraph, text
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.loremipsum import loremipsum

EXPORT_PATH = '_export/15_MixedBaselines.pdf'
if not os.path.exists('_export'):
	os.mkdir('_export')

# Get the PageFont instance
pbFont = findFont('PageBot-Regular')
fontSize = 24
red = rgb(255, 0, 100)
black = rgb(0, 0, 0)
flatFont = font.open(pbFont.path)

figure = shape().stroke(black).width(1)
strikes = [
	strike(flatFont).color(red).size(fontSize),
	strike(flatFont).color(red).size(fontSize+10),
	strike(flatFont).color(red).size(fontSize+20),
]
W, H = 1000, 1000
R = 20 # radius of origin marker

# Flat has origin in top-left
fDoc = document(W, H, 'pt')
fPage = fDoc.addpage()

txt = loremipsum()

# Text has to be split, not to contain newlines, into paragraphs.
P = 80 # Padding
x = P
y = P # Flat has origin on top left
paragraphs = []
sIndex = 0
for txtParagraph in txt.split('\n'):
    paragraphs.append(paragraph([strikes[sIndex].span(txtParagraph)]))
    sIndex += 1
    if sIndex >= len(strikes):
    	sIndex = 0
pt = fPage.place(text(paragraphs)) # Place the text
# Placing as frame seems to give better control on vertical position.
ascender = fontSize*pbFont.info.typoAscender/pbFont.info.unitsPerEm
# Baseline of the blox on M from top-left
pt.frame(x, y, W-2*P, H-2*P)

# Get the bounding box of this placedText,
# so we can use the (w, h) to create the doc/page size.
lines = [0]
# Find the y-positions of the lines
for lIndex, (height, _) in enumerate(pt.layout.runs()):
	if lIndex >= 0:
		lines.append(lines[-1]+height)
for ly in lines:
	fPage.place(figure.line(x, y+ly, W-P, y+ly))

# Cross hair marker on text origin baseline
y += ascender
fPage.place(figure.circle(x, y, R))
fPage.place(figure.line(x-R, y, x+R, y))
fPage.place(figure.line(x, y-R, x, y+R))

fDoc.pdf(EXPORT_PATH)

print('Done', EXPORT_PATH)