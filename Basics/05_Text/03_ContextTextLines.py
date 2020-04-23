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
#	  Show a column made from context.textLines rendering
#     Add a label under the column.
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
M = pt(16) # Distance of the labels from the line

textColor = color(1, 0, 0) # Red of the “A4”
bgColor = color(0.9) # Background color of the text box
lineColor = color(0, 0, 0.5)

# Export in _export folder that does not commit in Git. Force to export PDF.
# The _export folder is automatically created.
EXPORT_PATH = '_export/03_ContextTextLines.pdf'

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

# Style, BabelString and left text box
style = dict(font='PageBot-Regular', tracking=em(0.02), fontSize=fontSize, 
	hyphenation=True, language='en', leading=em(1.4))

# Create a BabelString with this style.
bs = context.newString(article, style)

# Let the context construct the textLines dictionary
textLines = context.textLines(bs, w=page.pw, h=page.ph)

# Make styles for the side labels;
labelStyle = dict(font='PageBot-Regular', fontSize=pt(8), tracking=em(0.02), textFill=0.7)

# Now we have a dictionary of wrapped BabelLines with their relative coordinates.
for lineIndex, ((x, y), bs) in enumerate(sorted(textLines.items())):
	newText(bs, parent=page, x=padding+x, y=padding+y, w=page.pw, h=page.ph)
	
	# Labels with line index on left side
	label = context.newString(str(len(textLines)-lineIndex-1), labelStyle)
	newText(label, x=padding+x-M, y=padding+y+2, parent=page)
	newLine(x=padding+x-M, y=padding+y, w=M, h=0, parent=page, stroke=0.5, fill=None, strokeWidth=0.5)
	
	# Labels with line index on right side
	label = context.newString(str(len(textLines)-lineIndex-1), labelStyle)
	newText(label, x=padding+x+page.pw, y=padding+y+2, parent=page)
	newLine(x=padding+x+page.pw, y=padding+y, w=M, h=0, parent=page, stroke=0.5, fill=None, strokeWidth=0.5)

# Export the page to PDF
doc.export(EXPORT_PATH)
