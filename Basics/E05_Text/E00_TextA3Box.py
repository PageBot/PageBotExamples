#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E00_TextA3Box.py
#
#	  Create a page in A3 landscape
#	  Setup the document view to show registration marks and cropmarks
#     Show the page frame and padding frame in blue
#     Show the generated PDF file name on top of the page.
#	  Show red “A4” centered on the page as Text element, 
#     with its baseline on the middle
#     Show the box of the element as gray background color.
#
from pagebot import getContext
context = getContext('DrawBot')
#context = getContext('Flat')

from pagebot.constants import *
from pagebot.elements import newText, newRect
from pagebot.document import Document
from pagebot.conditions import *
from pagebot.toolbox.color import color, blackColor
from pagebot.toolbox.units import pt, em, mm
from pagebot.toolbox.loremipsum import loremipsum
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.fonttoolbox.objects.font import findFont

DO_BLURB = True

fontSize = pt(24)

W, H = A3 # Standard portrait
padding = mm(30) # Outside measures to accommodate the crop makrs.
#FONT_NAME = 'Responder_P-Base_Italic' 
FONT_NAME = 'Upgrade-Regular' #'PageBot-Regular'

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
	article = loremipsum()

# Export in _export folder that does not commit in Git. Force to export PDF.
# The _export folder is automatically created.
EXPORT_PATH = '_export/E00_TextA3Box.pdf'
print('Generating:', EXPORT_PATH)

# Make a new document with one text box.

title = 'Single text box' # As will be shown on the page name info.
doc = Document(w=W, h=H, title=title, autoPages=1, context=context)

view = doc.view # Get the current view of the document.
view.padding = pt(40) # Make space to show crop marks, etc.
view.showCropMarks = True 
view.showRegistrationMarks = True
view.showPadding = True # Show the page padding
view.showFrame = True # Show the frame of the  page as blue line
view.showNameInfo = True # Showing page info and title on top of the page.

page = doc[1] # Get page on pageNumber, f irst in row (this is only one now).
page.padding = padding

style = dict(font=FONT_NAME, fontSize=fontSize*1.5, leading=em(1), 
	textFill=textColor, xAlign=LEFT)
# Add width to the string, as target width value for the box.
bs = context.newString(headline+'\n', style, w=page.pw)

style = dict(font=FONT_NAME, fontSize=fontSize, leading=em(1.2), 
	textFill=textColor, xAlign=LEFT, hyphenation=True)
bs += context.newString(article, style, w=page.pw)

t = newText(bs, parent=page, conditions=[Fit()],
	fill=bgColor, # Show background to mark the real position of the box.
	xAlign=LEFT, yAlign=BASELINE, # Vertical align on largest capheight of top line.
	showOrigin=True)

doc.solve()

doc.export(EXPORT_PATH)
