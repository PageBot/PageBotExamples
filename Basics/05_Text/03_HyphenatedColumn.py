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
#     03_HyphenatedColumns.py
#
#	  Create a page in A4 landscape
#	  Setup the document view to show registration marks and cropmarks
#     Show the page frame and padding frame in blue
#     Show the generated PDF file name on top of the page.
#	  Show 2 columns with the same width, same text, different in hyphenation
#     Add labels under the columns.
#
from pagebot import getContext
context = getContext('DrawBot')
#context = getContext('Flat')

from pagebot.constants import A4, CENTER, LEFT, RIGHT
from pagebot.elements import newTextBox, newLine, newText
from pagebot.document import Document
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt, em
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.contributions.filibuster import blurbwriter, content

fontSize = pt(12)
W, H = 400, 600 
padding = pt(50) # Outside measures to accommodate the crop makrs.
M = pt(5) # Distance of the labels from the line
G = pt(20) # Gutter between columns.

textColor = color(1, 0, 0) # Red of the “A4”
bgColor = color(0.9) # Background color of the text box
lineColor = color(0, 0, 0.5)

# Export in _export folder that does not commit in Git. Force to export PDF.
# The _export folder is automatically created.
EXPORT_PATH = '_export/03_HyphenatedColumns.pdf'

# Make a new document with with one page.
doc = Document(w=W, h=H, title=EXPORT_PATH, autoPages=1, context=context)

# Set the view parameters that define the status of the output
view = doc.view # Get the current view of the document.
view.padding = padding # Make space to show crop marks, etc.
view.showCropMarks = True 
view.showRegistrationMarks = True
view.showFrame = True # Show the frame of the  page as blue line
view.showNameInfo = True # Showing page info and title on top of the page.

# Get a random english article text to show hyphenation
b = Blurb()
article = b.getBlurb('article')

# Get the page and calculate the column width
page = doc[1] # Get page on pageNumber, first in row (this is only one now).
page.padding = padding
colW = (page.pw - G)/2

# Style, BabelString and left text box
style = dict(font='PageBot-Regular', tracking=em(0.02), fontSize=fontSize, leading=em(1.4))
bs = context.newString(article, style)
newTextBox(bs, parent=page, x=padding, y=padding, w=(page.pw - G)/2, h=page.ph)

# Style with hyphenation and right text box
style = dict(font='PageBot-Regular', tracking=em(0.02), hyphenation=True, fontSize=fontSize, leading=em(1.4))
bs = context.newString(article, style)
newTextBox(bs, parent=page, x=padding+colW+G, y=padding, w=colW, h=page.ph)

# Labels under the columns
labelStyle = dict(font='PageBot-Regular', fontSize=pt(12), tracking=em(0.02), textFill=0.5)
label = context.newString('Not hyphenated', labelStyle)
newText(label, x=padding, y=padding/2, parent=page)
label = context.newString('Hyphenated (%s)' % bs.language, labelStyle)
newText(label, x=padding+colW+G, y=padding/2, parent=page)

# Export the page to PDF
doc.export(EXPORT_PATH)
