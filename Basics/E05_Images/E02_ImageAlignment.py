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
#     E02_ImageAlignment.py
#
#     Draw images aligned on various positions
#
from random import random
from pagebot import getContext

from pagebot.filepaths import getResourcesPath
from pagebot.document import Document
from pagebot.toolbox.color import color, noColor
from pagebot.toolbox.units import em, p, pt, inch, degrees
from pagebot.conditions import * # Import all conditions for convenience.
from pagebot.constants import *
from pagebot.elements import *

#context = FlatContext()
context = getContext('DrawBot')

# Example image that has nice areas to put text as example.
imagePath = getResourcesPath() + '/images/peppertom_lowres_398x530.png'
EXPORT_PATH = '_export/02_ImageAlignment.pdf'
BLEED = pt(6)

W = pt(400) # Document size
H = pt(400)
PADDING = pt(24) # Page padding on all sides

# Create a new document with 1 page. Set overall size and padding.
doc = Document(w=W, h=H, title=EXPORT_PATH, padding=PADDING, context=context)
# Get the default page view of the document and set viewing parameters
view = doc.view
view.padding = pt(20)
view.showFrame = True
view.showPadding = True
view.showColorBars = False
view.showCropMarks = True
view.showRegistrationMarks = True
view.showNameInfo = True # Showing page info and title on top of the page.

def addLabel(e, page, s, condition):
	style = dict(font='PageBot-Regular', fontSize=pt(16),
		leading=em(1.2), textFill=0.6)
	bs = context.newString(s, style)
	newText(bs, parent=page, w=page.pw, xAlign=LEFT, yAlign=TOP,
		conditions=[Left2Left(), condition])

# Get the first page
# LEFT
page = doc[1]
page.bleed = BLEED
im = newImage(imagePath, parent=page, x=-page.bleedLeft, y=page.h/2,
	w=page.w/2+page.bleedLeft, xAlign=LEFT, yAlign=MIDDLE, showOrigin=True)
addLabel(im, page, 'x=-page.bleedLeft; y=page.h/2\nxAlign=LEFT; yAlign=MIDDLE', 
	Top2Top())

page = page.next
im = newImage(imagePath, parent=page, x=0, y=page.h/2,
	w=page.w/2, xAlign=LEFT, yAlign=MIDDLE, showOrigin=True)
addLabel(im, page, 'x=0; y=page.h/2\nxAlign=LEFT; yAlign=MIDDLE', 
	Top2Top())

page = page.next
im = newImage(imagePath, parent=page, x=page.pl, y=page.h/2,
	w=page.pw/2, xAlign=LEFT, yAlign=MIDDLE, showOrigin=True)
addLabel(im, page, 'x=page.pl; y=page.h/2\nxAlign=LEFT; yAlign=MIDDLE', 
	Top2Top())

page = page.next
im = newImage(imagePath, parent=page, x=page.pl+page.pw/4, y=page.h/2,
	w=page.pw/2, xAlign=CENTER, yAlign=MIDDLE, showOrigin=True)
addLabel(im, page, 'x=page.pl+page.pw/4; y=page.h/2\nxAlign=CENTER; yAlign=MIDDLE', 
	Top2Top())

page = page.next
im = newImage(imagePath, parent=page, x=page.w/2, y=page.h/2,
	w=page.pw/2, xAlign=RIGHT, yAlign=MIDDLE, showOrigin=True)
addLabel(im, page, 'x=page.w/2; y=page.h/2\nxAlign=RIGHT; yAlign=MIDDLE', 
	Top2Top())

# CENTER
page = page.next
im = newImage(imagePath, parent=page, x=page.pl+page.pw/4, y=page.h/2,
	w=page.pw/2, xAlign=LEFT, yAlign=MIDDLE, showOrigin=True)
addLabel(im, page, 'x=page.pl+page.w/2; y=page.h/2\nxAlign=LEFT; yAlign=MIDDLE', 
	Top2Top())

page = page.next
im = newImage(imagePath, parent=page, x=page.w/2, y=page.h/2,
	w=page.pw/2, xAlign=CENTER, yAlign=MIDDLE, showOrigin=True)
addLabel(im, page, 'x=page.w/2; y=page.h/2\nxAlign=CENTER; yAlign=MIDDLE', 
	Top2Top())

page = page.next
im = newImage(imagePath, parent=page, x=page.pl+page.pw*3/4, y=page.h/2,
	w=page.pw/2, xAlign=RIGHT, yAlign=MIDDLE, showOrigin=True)
addLabel(im, page, 'x=page.pl+page.pw*3/4; y=page.h/2\nxAlign=RIGHT; yAlign=MIDDLE', 
	Top2Top())

# RIGHT
page = page.next
im = newImage(imagePath, parent=page, x=page.w/2, y=page.h/2,
	w=page.pw/2, xAlign=LEFT, yAlign=MIDDLE, showOrigin=True)
addLabel(im, page, 'x=page.w/2; y=page.h/2\nxAlign=LEFT; yAlign=MIDDLE', 
	Top2Top())

page = page.next
im = newImage(imagePath, parent=page, x=page.pl+page.pw*3/4, y=page.h/2,
	w=page.pw/2, xAlign=CENTER, yAlign=MIDDLE, showOrigin=True)
addLabel(im, page, 'x=page.pl*page.pw*3/4; y=page.h/2\nxAlign=CENTER; yAlign=MIDDLE', 
	Top2Top())

page = page.next
im = newImage(imagePath, parent=page, x=page.w-page.pr, y=page.h/2,
	w=page.pw/2, xAlign=RIGHT, yAlign=MIDDLE, showOrigin=True)
addLabel(im, page, 'x=page.w-page.pr; y=page.h/2\nxAlign=RIGHT; yAlign=MIDDLE', 
	Top2Top())

page = page.next
im = newImage(imagePath, parent=page, x=page.w/2, y=page.h/2,
	w=page.w/2, xAlign=LEFT, yAlign=MIDDLE, showOrigin=True)
addLabel(im, page, 'x=page.w/2; y=page.h/2\nxAlign=LEFT; yAlign=MIDDLE', 
	Top2Top())

page = page.next
page.bleed = BLEED
im = newImage(imagePath, parent=page, x=page.w/2, y=page.h/2,
	w=page.w/2+page.bleedRight, xAlign=LEFT, yAlign=MIDDLE, showOrigin=True)
addLabel(im, page, 'x=page.w/2; y=page.h/2\nxAlign=LEFT; yAlign=MIDDLE', 
	Top2Top())

# TOP
page = page.next
im = newImage(imagePath, parent=page, x=page.w/2, y=page.h/2,
	h=page.ph/2, xAlign=CENTER, yAlign=BOTTOM, showOrigin=True)
addLabel(im, page, 'x=page.w/2; y=page.h/2\nxAlign=RIGHT; yAlign=MIDDLE', 
	Bottom2Bottom())

# MIDDLE
page = page.next
im = newImage(imagePath, parent=page, x=page.w/2, y=page.h/2,
	h=page.ph/2, xAlign=CENTER, yAlign=MIDDLE, showOrigin=True)
addLabel(im, page, 'x=page.w/2; y=page.h/2\nxAlign=RIGHT; yAlign=MIDDLE', 
	Top2Top())

# BOTTOM
page = page.next
im = newImage(imagePath, parent=page, x=page.w/2, y=page.h/2,
	h=page.ph/2, xAlign=CENTER, yAlign=TOP, showOrigin=True)
addLabel(im, page, 'x=page.w/2; y=page.h/2\nxAlign=RIGHT; yAlign=MIDDLE', 
	Top2Top())

page = page.next
im = newRect(fill=(1, 0, 0), parent=page, y=page.h/2,
	conditions=(Fit2Width(), Bottom2Bottom()),
	h=page.ph/2, yAlign=TOP, showOrigin=True)
addLabel(im, page, 'x=Fit2Width(); y=Bottom2Bottom()\nxAlign=LEFT; yAlign=MIDDLE', 
	Top2Top())

doc.solve()

# Export the document to this PDF file.
doc.export(EXPORT_PATH)

