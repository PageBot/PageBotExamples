#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#

#     www.pagebot.io
#     Licensed under MIT conditions
#


# -----------------------------------------------------------------------------
#
#     E05_ImageCondition.py
#
#     Position an image element in the page.
#
import os
import sys

from pagebot import getContext
from pagebot.constants import A4, LEFT, RIGHT, BOTTOM, TOP, EXPORT
from pagebot.conditions import *
from pagebot.document import Document
from pagebot.elements import *
from pagebot.filepaths import getResourcesPath
from pagebot.toolbox.units import pt, mm
from pagebot.toolbox.transformer import path2FileName

FILENAME = path2FileName(__file__)
W, H = pt(800, 800)
P = pt(30) # Padding of the page

def draw(contextName):
    context = getContext(contextName)
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)

    # Define the path where to find the example image.
    path = getResourcesPath() + "/images/cookbot1.jpg"

    doc = Document(w=W, h=H, context=context)
    doc.view.showPadding = True

    page = doc[1]
    page.padding = P

    # Position the image on bottom-left of the page padding.
    # Height of the image is 50% of usable space.
    newImage(path, x=P, y=P, h=page.ph/2, parent=page, showOrigin=True)

    # Position the image on bottom-right of the page padding.
    # Add opaque red overlay.
    newImage(path, x=page.w-P, y=P, h=page.ph/2, parent=page, fill=(1, 0, 0, 0.5),
            xAlign=RIGHT, yAlign=BOTTOM)

    # Position at top-right, rotated, yellow opaque overlay.
    newImage(path, x=P, y=page.h-P, h=page.ph/2, parent=page,
            xAlign=LEFT, yAlign=TOP, fill=(0, 1, 1, 0.5), rotate=90)

    # Position at top-right, rotated, yellow opaque overlay.
    newImage(path, x=page.w-P, y=page.h-P, h=page.ph/2, parent=page,
            xAlign=RIGHT, yAlign=TOP, fill=(1, 1, 0, 0.5), rotate=90)

    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
