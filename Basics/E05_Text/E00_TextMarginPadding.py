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
#     00_TextPosition.py
#
#	  Create a page in A4 landscape
#	  Setup the document view to show registration marks and cropmarks
#	  Show red “Hkpx” centered on the page as Text element, 
#     with its x-height on the middle of page height
#     Show padding and maring of the text box, in addition to calculatate size.
#     Show the box of the element as blue guidelines with labels.
#
from pagebot import getContext
context = getContext('DrawBot')
#context = getContext('Flat')

from pagebot.constants import *
from pagebot.elements import newText, newRect, newLine
from pagebot.document import Document
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt, em

FONT_NAME = 'PageBot-Regular'
fontSize = pt(200)
H, W = A4 # Standard portrait, swapped to be used as landscape ratio.
padding = pt(40) # Outside measures to accommodate the crop makrs.
sw = pt(0.5) # Stroke width of guide lines
M = pt(40) # Text element margin

textColor = color(1, 0, 0) # Red of the “Hkpx”
bgColor = color(0.9) # Background color of the text box

# Export in _export folder that does not commit in Git. Force to export PDF.
# The _export folder is automatically created.
EXPORT_PATH = '_export/00_TextMarginPadding.pdf'

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
page.padding = padding

style = dict(font=FONT_NAME, fontSize=fontSize, tracking=-em(0.02), leading=em(1), 
	textFill=textColor, xAlign=CENTER, fill=bgColor, showOrigin=True, yAlign=XHEIGHT)
t = newText('Hkpx', parent=page, x=page.w/2, y=page.h/2, style=style, margin=M,
	showMargin=True, showPadding=True)
# In Text mode (no width defined), adding padding will increase width
# FIXME: Something wrong here still: Maximum indent of FormattedString is 20 and -20
# And it does not work yet in case width is fixed.
# https://developer.apple.com/documentation/uikit/nsparagraphstyle/1525556-tailindent
t.padding = pt(0, 30) 

print('Text/BabelString indent:', t.bs.indent, t.bs.tailIndent)
print('Hkpx text size:', t.bs.textSize)
print('Text in box size:', t.w, t.h)

# Horizontal guides
newLine(x=0, y=t.y, w=page.w, h=0, stroke=(0, 0, 0.7), strokeWidth=sw, parent=page)
newLine(x=0, y=t.bottom, w=page.w, h=0, stroke=(0, 0, 0.7), strokeWidth=sw, parent=page)
newLine(x=0, y=t.top, w=page.w, h=0, stroke=(0, 0, 0.7), strokeWidth=sw, parent=page)

# Vertical guides
newLine(x=t.left, y=0, w=0, h=page.h, stroke=(0, 0, 0.7), strokeWidth=sw, parent=page)
newLine(x=t.center, y=0, w=0, h=page.h, stroke=(0, 0, 0.7), strokeWidth=sw, parent=page)
newLine(x=t.right, y=0, w=0, h=page.h, stroke=(0, 0, 0.7), strokeWidth=sw, parent=page)

doc.export(EXPORT_PATH)
