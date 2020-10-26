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
#     E01_CacheScaledImage.py
#
#     How to scale an image (without being an element).
#     Because DrawBot doesn't support setting the width and height attributes
#     explicitly, scaling needs to be done using the scale() function. This
#     also changes to (x, y) position, therefore it also  must be inversely
#     scaled. However, in this example scaled image is positioned at (0, 0).

import os
import sys

from pagebot import getContext
from pagebot.conditions import *
from pagebot.constants import A4, EXPORT
from pagebot.elements import *
from pagebot.document import Document
from pagebot.filepaths import getResourcesPath
from pagebot.toolbox.units import pt, mm
from pagebot.toolbox.transformer import path2FileName

FILENAME = path2FileName(__file__)
W, H = mm(1000, 240)
M = pt(12) # Margin between the images.
P = mm(30) # Padding of the page.

def draw(contextName):
    context = getContext(contextName)
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    doc = Document(w=W, h=H, context=context)
    page = doc[1]
    page.padding = P

    # Defines the path where to find the example image.
    path = getResourcesPath() + "/images/cookbot1.jpg"

    # Incremental scale division factor of the image width.
    factor = 5

    # Stop before they become invisibly small
    for n in range(15):
            # Create a range of scaled imaged that try to fit by floating
            # conditions.
            newImage(path, w=page.pw/factor, mr=10*M/(n+1), parent=page,
                    conditions=(Right2Right(), Float2Top(), Float2Left()),
                    scaleImage=False)
            factor *= 1.3

    doc.solve()
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
