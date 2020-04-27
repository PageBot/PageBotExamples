#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
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
#     00_TextBoxAlignment.py
#
#	  Create a page in A3 landscape
#	  Show text box with  multiple lines on all alignment combination horizontal/vertical
#     Show origins of the text boxes
#     Show alignment lines
#     Show labels with alignment names.
#
from pagebot import getContext
context = getContext('DrawBot')
#context = getContext('Flat')

from pagebot.constants import *
from pagebot.elements import newText, newRect, newLine
from pagebot.document import Document
from pagebot.conditions import *
from pagebot.toolbox.color import color, blackColor
from pagebot.toolbox.units import pt, em, mm
from pagebot.toolbox.lorumipsum import lorumipsum
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.fonttoolbox.objects.font import findFont

DO_BLURB = True

fontSize = pt(28)
colWidth = mm(50)

W, H = mm(500, 250) # Customize paper size
padding = mm(60) # Outside measures to accommodate the crop makrs.
FONT_NAME = 'PageBot-Regular'

textColor = blackColor
bgColor = color(0.9) # Background color of the text box

if DO_BLURB:
	# Get a random english article text to show hyphenation
	b = Blurb()
	headline = b.getBlurb('news_headline')
	article = b.getBlurb('article')
	article += '\n\n' + b.getBlurb('article')
else:
	headline = 'Headline of column'
	article = lorumipsum()

# Export in _export folder that does not commit in Git. Force to export PDF.
# The _export folder is automatically created.
EXPORT_PATH = '_export/00_TextBoxAlignment.pdf'
print('Generating:', EXPORT_PATH)

# Make a new document with one text box.

title = 'Single text box' # As will be shown on the page name info.
doc = Document(w=W, h=H, title=title, autoPages=1, context=context)

view = doc.view # Get the current view of the document.
view.showPadding = True # Show the page padding

page = doc[1] # Get page on pageNumber, first in row (this is only one now).
page.padding = padding

XALIGNS = (LEFT, CENTER, RIGHT)
YALIGNS = (TOP, CAPHEIGHT, XHEIGHT, MIDDLE_CAP, MIDDLE_X, BASELINE, BOTTOM)

rowCnt = len(XALIGNS)-1
colCnt = len(YALIGNS)-1


for ix, yAlign in enumerate(YALIGNS): # Flipped, yAligns show horizontal

	if 0 < ix < colCnt:
		# Show the line for the middle row of texts
		newLine(x=padding + ix*page.pw/colCnt, y=padding, w=0, h=page.ph, parent=page,
			stroke=(0, 0, 0.5), strokeWidth=0.5)

	for iy, xAlign in enumerate(XALIGNS):

		style1 = dict(font=FONT_NAME, fontSize=fontSize, leading=em(1), 
			textFill=textColor, xAlign=xAlign) # xAlignment is part of the BabelString.
		# Add width to the string, as target width value for the box.
		bs = context.newString('Hkpx\n', style1)
		style2 = dict(font=FONT_NAME, fontSize=fontSize/2, leading=em(1), 
			textFill=textColor, xAlign=xAlign) # xAlignment is part of the BabelString.
		bs += context.newString('Multiple lines of text making it a BabelString box', style2)

		x = padding + ix*page.pw/colCnt
		y = padding + iy*page.ph/rowCnt
		newText(bs, parent=page, x=x, y=y, w=colWidth, h=mm(30),
			fill=bgColor, # Show background to mark the real position of the box.
			yAlign=yAlign, # Vertical alignment is part of the Text element box.
			showOrigin=True)
		# Ajust the style for label
		style2['textFill'] = color(0.4)
		style2['fontSize'] = fontSize/3
		y -= bs.th + 4
		bs = context.newString(' %s | %s ' % (xAlign.capitalize(), yAlign.capitalize()), style2)
		newText(bs, parent=page, x=x, y=y, yAlign=TOP, showOrigin=False)

# Show the line for the middle row of texts
newLine(x=padding, y=padding+page.ph/2, w=page.pw, h=0, parent=page,
	stroke=(0, 0, 0.5), strokeWidth=0.5)

doc.export(EXPORT_PATH)
