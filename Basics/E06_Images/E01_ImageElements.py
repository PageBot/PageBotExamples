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
#     E01_ImageElements.py
#
#     This script generates a page with random color squares, indicating where their position is.
#

from pagebot.filepaths import getResourcesPath
from pagebot.contexts import getContext
from pagebot.constants import TOP, BOTTOM
from pagebot.conditions import *
from pagebot.elements import *
from pagebot.document import Document
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt
# Document is the main instance holding all information about the
# document together (pages, styles, etc.)

context = getContext('DrawBot')

PADDING = 30
W = H = 400

# The standard PageBot function getRootStyle() answers a standard Python dictionary,
# where all PageBot style entries are filled by their default values. The root style is kept in RS
# as reference for the ininitialization of all elements.
# Each element uses the root style as copy and then modifies the values it needs.
# Note that the use of style dictionaries is fully recursive in PageBot, implementing a cascading structure
# that is very similar to what happens in CSS.

# Export in _export folder that does not commit in Git. Force to export PDF.
EXPORT_PATH = '_export/01_ImageElements.pdf'

doc = Document(w=W, h=H, title='Color Squares', autoPages=1, context=context)

view = doc.getView()
view.padding = 0 # Avoid the showing of crop marks, etc.
view.showOrigin = True

# Get list of pages with equal y, then equal x.
page = doc[1] # Get page on pageNumber, first in row (this is only one now).
page.name = 'This is a demo page for floating child elements'
page.padding = PADDING

path = getResourcesPath() + '/images/cookbot10.jpg'

img = newImage(path, padding=0,
               parent=page, 
               conditions=(Top2Top(),
                           Fit2Width(),
                           ),
               yAlign=TOP,
               fill=color(0, 1, 0, 0.3),
               stroke=color(1, 0, 0),
               scaleImage=False)

newImage(path, padding=0,
               parent=page, 
               conditions=(Bottom2Bottom(),
                           Fit2Width(),
                           ),
               yAlign=BOTTOM,
               fill=color(1, 0, 0, 0.3),
               stroke=color(0, 0, 1),
               scaleImage=False)

score = page.solve()
if score.fails:
    print(score.fails)

print('Image size', img.w, img.h)
print('Image file size', img.iw, img.ih) # TODO: Should not be pt(0, 0)
for e in img.elements:
    print('Element', e)

doc.export(EXPORT_PATH)

