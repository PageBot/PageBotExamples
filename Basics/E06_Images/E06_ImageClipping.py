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
#     E06_ImageClipping.py
#
#     Draw images with clipping paths and rotation.

from random import random

from pagebot import getContext
from pagebot.conditions import *
from pagebot.constants import *
from pagebot.elements import *
from pagebot.filepaths import getResourcesPath
from pagebot.document import Document
from pagebot.toolbox.color import color, noColor
from pagebot.toolbox.transformer import path2FileName
from pagebot.toolbox.units import em, p, pt, inch, degrees

FILENAME = path2FileName(__file__)

# Document size.
W = pt(400)
H = pt(400)
PADDING = pt(24) # Page padding.
BLEED = pt(6)

def draw(contextName):
    context = getContext(contextName)

    # Example image that has nice areas to put text as example.
    imagePath = getResourcesPath() + '/images/pagebot.png'
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)

    # Create a new document with 1 page. Set overall size and padding.
    doc = Document(w=W, h=H, padding=PADDING, context=context)
    # Get the default page view of the document and set viewing parameters
    view = doc.view
    view.padding = pt(30)
    view.showFrame = True
    view.showPadding = True
    view.showColorBars = False
    view.showCropMarks = True
    view.showRegistrationMarks = True
    view.showNameInfo = True # Showing page info and title on top of the page.
    page = doc[1]

    # Make image box as child element of the page and set its layout
    # conditions. The image is portrait, so fitting vertical makes the image
    # fit in the padding box of the page.
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
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
