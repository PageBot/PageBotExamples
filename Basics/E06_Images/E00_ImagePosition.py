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
#     Position an image element on the page.

import os
import sys
from pagebot import getContext
from pagebot.conditions import *
from pagebot.constants import A4, LEFT, RIGHT, BOTTOM, TOP, EXPORT
from pagebot.document import Document
from pagebot.elements import *
from pagebot.filepaths import getResourcesPath
from pagebot.toolbox.transformer import path2FileName
from pagebot.toolbox.units import pt, mm

FILENAME = path2FileName(__file__)
W, H = pt(400, 400)
P = pt(30) # Page padding.

def draw(contextName):
    context = getContext(contextName)
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)

    # Defines the path where to find the example image.
    path = getResourcesPath() + "/images/cookbot1.jpg"
    doc = Document(w=W, h=H, context=context)
    doc.view.showPadding = True
    page = doc[1] # Get first (and only) automatic page.
    page.padding = P

    # Positions the image on bottom-left of the page padding. Height of the
    # image is 50% of usable space.
    newImage(path, x=P, y=P, h=page.ph/2, parent=page, showOrigin=True)

    # Positions the image on bottom-right of the page padding. Adds a opaque
    # red overlay.
    newImage(path, x=page.w-P, y=P, h=page.ph/2, parent=page, fill=(1, 0, 0, 0.5),
            xAlign=RIGHT, yAlign=BOTTOM)

    # Positions at top-right, rotated, yellow opaque overlay.
    newImage(path, x=P, y=page.h-P, h=page.ph/2, parent=page,
            xAlign=LEFT, yAlign=TOP, fill=(0, 1, 1, 0.5), rotate=90)

    # Positions at top-right, rotated, yellow opaque overlay.
    newImage(path, x=page.w-P, y=page.h-P, h=page.ph/2, parent=page,
            xAlign=RIGHT, yAlign=TOP, fill=(1, 1, 0, 0.5), rotate=90)

    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
