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
#     00_TextA3Box.py
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
from pagebot.toolbox.lorumipsum import lorumipsum
from pagebot.contributions.filibuster.blurb import Blurb

DO_BLURB = False

fontSize = pt(20)
W, H = A3 # Standard portrait, swapped to be used as landscape ratio.
padding = mm(30) # Outside measures to accommodate the crop makrs.

textColor = blackColor
bgColor = color(0.9) # Background color of the text box

if DO_BLURB:
	# Get a random english article text to show hyphenation
	b = Blurb()
	headline = b.getBlurb('news_headline')
	article = b.getBlurb('article')
	article = ' ' + b.getBlurb('article')
else:
	headline = 'Headline of column'
	article = lorumipsum()

# Export in _export folder that does not commit in Git. Force to export PDF.
# The _export folder is automatically created.
EXPORT_PATH = '_export/00_TextA3Box.pdf'

# Make a new document with one text box.

title = 'Single text box' # As will be shown on the page name info.
doc = Document(w=W, h=H, title=title, autoPages=1, context=context)

view = doc.view # Get the current view of the document.
view.padding = pt(40) # Make space to show crop marks, etc.
view.showCropMarks = True 
view.showRegistrationMarks = True
view.showFrame = True # Show the frame of the  page as blue line
view.showNameInfo = True # Showing page info and title on top of the page.

page = doc[1] # Get page on pageNumber, first in row (this is only one now).
page.padding = padding

style = dict(font='PageBot-Bold', fontSize=fontSize*2.5, leading=em(1), 
	textFill=textColor, xAlign=LEFT)
bs = context.newString(headline+'\n', style)
style = dict(font='PageBot-Regular', fontSize=fontSize, leading=em(1), 
	textFill=textColor, xAlign=LEFT, hyphenation=True)
bs += context.newString(article, style)

t = newText(bs, parent=page, conditions=[Fit()], fill=bgColor, xAlign=LEFT, showOrigin=True)

doc.solve()

doc.export(EXPORT_PATH)
