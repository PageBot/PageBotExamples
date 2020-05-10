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
#     E05_ImageClipping.py
#
#     Draw images with clipping paths and rotation.
#
from random import random
#from pagebot.contexts.flat.flatcontext import FlatContext
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
EXPORT_PATH = '_export/05_ImageClipping.pdf'

W = pt(400) # Document size
H = pt(400)
PADDING = pt(24) # Page padding on all sides

# Create a new document with 1 page. Set overall size and padding.
doc = Document(w=W, h=H, padding=PADDING, context=context)
# Get the default page view of the document and set viewing parameters
view = doc.view
view.padding = pt(20)
view.showFrame = True
view.showPadding = True
view.showColorBars = False
view.showCropMarks = True
view.showRegistrationMarks = True

# Get the page
page = doc[1]
# Make image box as child element of the page and set its layout conditions.
conditions = [Fit2Height(), Center2Center()]
#conditions = [Center2Center()]
conditions = [Fit2Height(), Right2Right()]
im = newImage(imagePath, parent=page, conditions=conditions, 
	xAlign=RIGHT, showOrigin=True)
conditions = [Center2Center(), Middle2Middle()]
conditions = None 
#mask = newMask(parent=page, conditions=conditions, showOrigin=True)
#mask.rect(0, 0, w=200, h=300)

doc.solve()

# Export the document to this PDF file.
doc.export(EXPORT_PATH)

