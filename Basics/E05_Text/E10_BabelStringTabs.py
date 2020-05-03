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
#     E10BabelStringTabs.py
#
#	  Create a page in custom landscape size
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

from pagebot.constants import A4, CENTER, LEFT, RIGHT, TOP
from pagebot.elements import newText, newLine
from pagebot.document import Document
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt, em

fontSize = pt(20)
W, H = 800, 200 
padding = pt(40) # Outside measures to accommodate the crop makrs.
M = pt(5) # Distance of the labels from the line

FONT_NAME = 'PageBot-Regular'

textColor = color(1, 0, 0) # Red of the “A4”
bgColor = color(0.9) # Background color of the text box
lineColor = color(0, 0, 0.5)

# Export in _export folder that does not commit in Git. Force to export PDF.
# The _export folder is automatically created.
EXPORT_PATH = '_export/E10_BabelStringTabs.pdf'

# Make a new document with one text box.

doc = Document(w=W, h=H, autoPages=1, context=context)

view = doc.view # Get the current view of the document.
view.padding = padding # Make space to show crop marks, etc.
view.showCropMarks = True 
view.showRegistrationMarks = True
view.showFrame = True # Show the frame of the  page as blue line
view.showNameInfo = True # Showing page info and title on top of the page.

page = doc[1] # Get page on pageNumber, first in row (this is only one now).

TABS = ((pt(100), LEFT), (pt(200), LEFT), (pt(400), CENTER), (pt(600), RIGHT))
style = dict(font=FONT_NAME, fontSize=fontSize, textFill=textColor, tabs=TABS)
bs = context.newString('ABCD\tFirst tab\tSecond tab\tCentered tab\tRight tab\nMore\tMore\tMore\tMore\tMore\n', style)
x = 100
# Text box with tabbed string. Since (w, h) are omitted, the box will resize itself
# depending on the rendered size of the string, as defined in (bs.tw, bs.th)
t = newText(bs, parent=page, x=x, y=page.h/2, fill=bgColor, showElementOrigin=True)

# Show vertical lines on the tab positions.
labelStyle = dict(font=FONT_NAME, fontSize=pt(12), textFill=0.5, tracking=em(0.03))
label = context.newString('Tab start 0', labelStyle)
newText(label, x=x+M, y=t.bottom - pt(4), parent=page)
newLine(x=x, y=0, w=0, h=H, parent=page, stroke=lineColor, strokeWidth=pt(0.3))

# Show lines at tab positions
for value, alignment in TABS:
	# Add a vertical line element, with a label showing the alignment and tab distance.
	newLine(x=x+value, y=0, w=0, h=H, parent=page, stroke=lineColor, strokeWidth=pt(0.3))
	label = context.newString('Tab %s %s' % (alignment, value), labelStyle)
	newText(label, x=x+M+value, y=t.bottom - pt(4), parent=page, yAlign=TOP)

doc.export(EXPORT_PATH)
