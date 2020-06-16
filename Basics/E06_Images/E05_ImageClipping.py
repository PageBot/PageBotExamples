#!/usr/bin/env python3
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
import flat

def imageClipping(contextName):
    context = getContext(contextName)

    # Example image that has nice areas to put text as example.
    imagePath = getResourcesPath() + '/images/pagebot.png'
    EXPORT_PATH = '_export/05_ImageClipping-%s.pdf' % contextName

    W = pt(400) # Document size
    H = pt(400)
    PADDING = pt(24) # Page padding on all sides
    BLEED = pt(6)

    # Create a new document with 1 page. Set overall size and padding.
    doc = Document(w=W, h=H, title=EXPORT_PATH, padding=PADDING, context=context)
    # Get the default page view of the document and set viewing parameters
    view = doc.view
    view.padding = pt(30)
    view.showFrame = True
    view.showPadding = True
    view.showColorBars = False
    view.showCropMarks = True
    view.showRegistrationMarks = True
    view.showNameInfo = True # Showing page info and title on top of the page.

    # Get the page
    page = doc[1]
    # Make image box as child element of the page and set its layout conditions.
    # The image is portrait, so fitting vertical makes the image fit in the
    # padding box of the page.
    conditions = [Fit2Height(), Center2Center()]
    im = newImage(imagePath, parent=page, conditions=conditions,
            showOrigin=True)

    page = page.next
    # Fitting the image by width, it does not fit vertically anymore.
    conditions = [Fit2Width(), Middle2Middle()]
    im = newImage(imagePath, parent=page, conditions=conditions,
            showOrigin=True)

    page = page.next
    # Fitting the image by width, it does not fit vertically anymore.
    # Adding a mask as sibling, we can clip the image on the page padding.
    conditions = [Fit2Width(), Middle2Middle()]
    im = newImage(imagePath, parent=page, conditions=conditions,
            showOrigin=True)
    conditions =[Fit()]
    mask = newMask(parent=page, conditions=conditions, # Fit page padding
            showOrigin=True)

    page = page.next
    # Fitting the image by width, it does not fit vertically anymore.
    # The Mask can be any size and position on the page.
    conditions = [Fit2Width(), Middle2Middle()]
    im = newImage(imagePath, parent=page, conditions=conditions,
            showOrigin=True)
    conditions = [Right2Right(), Top2Top()]
    mask = newMask(parent=page, conditions=conditions,
            w=page.pw/2, h=page.ph/2, showOrigin=True)

    page = page.next
    page.bleed = BLEED # Set all bleed sides to the same value
    # Fitting the image by width, it does not fit vertically anymore.
    # Making the image bleed on page width.
    conditions = [Left2BleedLeft(), Fit2BleedRight(), Middle2Middle()]
    im = newImage(imagePath, parent=page, conditions=conditions,
            showOrigin=True)
    conditions = [Right2Right(), Top2Top()]

    page = page.next
    page.bleed = BLEED # Set all bleed sides to the same value
    # Fitting the image by width, it does not fit vertically anymore.
    # Making the image bleed on page width.
    # Now the mask needs to follow the bleed fit too.
    conditions = [Left2BleedLeft(), Fit2BleedRight(), Middle2Middle()]
    im = newImage(imagePath, parent=page, conditions=conditions,
            showOrigin=True)
    # Fit the mask on top half of the page, including bleed
    conditions = [Left2BleedLeft(), Fit2BleedRight(), Top2BleedTop()]
    mask = newMask(parent=page, conditions=conditions,
            w=page.w/2+2*BLEED, h=page.h/2+BLEED, showOrigin=True)

    doc.solve()

    # Export the document to this PDF file.
    doc.export(EXPORT_PATH)

for contextName in (
    'DrawBot',
    'Flat',
    ):
    imageClipping(contextName)
