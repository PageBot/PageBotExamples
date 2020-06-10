#!/usr/bin/env python3
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
#     E00_ImagePosition.py
#
#     Position an image element in the page.
#
import os # Import module that communicates with the file system.
import sys

from pagebot.document import Document
from pagebot.filepaths import getResourcesPath
from pagebot.toolbox.units import pt, mm
from pagebot import getContext
from pagebot.constants import A4, LEFT, RIGHT, BOTTOM, TOP
from pagebot.elements import *
from pagebot.conditions import *

def imagePosition(contextName):
    context = getContext(contextName)
    W, H = pt(400, 400)

    P = pt(30) # Padding of the page

    EXPORT_PATH = '_export/00_ImagePosition.pdf'

    # Define the path where to find the example image.
    path = getResourcesPath() + "/images/cookbot1.jpg"
    # Use the standard DrawBot function to get the width/height of the image from the file.
    doc = Document(w=W, h=H, context=context) # New simple document with default padding.
    doc.view.showPadding = True

    page = doc[1] # Get first (and only) automatic page.
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

    doc.export(EXPORT_PATH)

for contextName in (
    'DrawBot',
    'Flat',
    ):
    imagePosition(contextName)
