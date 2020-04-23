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
#     00_Text.py
#
#	  Create a page in A4 landscape
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

from pagebot.constants import A4, CENTER
from pagebot.elements import newText, newRect
from pagebot.document import Document
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt, em

fontSize = pt(200)
H, W = A4 # Standard portrait, swapped to be used as landscape ratio.
padding = pt(40) # Outside measures to accommodate the crop makrs.

textColor = color(1, 0, 0) # Red of the “A4”
bgColor = color(0.9) # Background color of the text box

# Export in _export folder that does not commit in Git. Force to export PDF.
# The _export folder is automatically created.
EXPORT_PATH = '_export/00_Text.pdf'

# Make a new document with one text box.

title = 'Single text box' # As will be shown on the page name info.
doc = Document(w=W, h=H, title=title, autoPages=1, context=context)

view = doc.view # Get the current view of the document.
view.padding = padding # Make space to show crop marks, etc.
view.showCropMarks = True 
view.showRegistrationMarks = True
view.showFrame = True # Show the frame of the  page as blue line
view.showNameInfo = True # Showing page info and title on top of the page.

page = doc[1] # Get page on pageNumber, first in row (this is only one now).

style = dict(font='PageBot-Regular', fontSize=fontSize, leading=0, 
	textFill=textColor, xAlign=CENTER)
bs = context.newString('A4', style)
t = newText(bs, parent=page, x=page.w/2, y=page.h/2, fill=bgColor, showOrigin=True)
newRect(parent=page, x=page.w/2, y=page.h/2+bs.descender, showOrigin=True,
	w=t.w, h=t.h, fill=None, stroke=0, xAlign=CENTER)

doc.export(EXPORT_PATH)
