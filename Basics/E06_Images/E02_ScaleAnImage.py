#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
# #     Copyright (c) 2017 Thom Janssen <https://github.com/thomgb>
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E01_ScalingAnImage.py
#

import os
import sys

from pagebot import getContext
from pagebot.filepaths import getResourcesPath
from pagebot.toolbox.units import pt
from pagebot.toolbox.transformer import path2FileName

FILENAME = path2FileName(__file__)
IMAGENAME = 'cookbot1'

def draw(contextName):
    context = getContext(contextName)
    path = getResourcesPath() + "/images/%s.jpg" % IMAGENAME
    w, h = context.imageSize(path)

    # Let's say we want to scale it to 50%. The 0.5 is the multiplication
    # factor.
    newScale = 0.5

    # Make a page with the size of the scaled image, rounded to whole pixels.
    context.newPage(pt(int(w*newScale)), pt(int(h*newScale)))

   # Saves the “graphics state“, just in case the script is extended later,
    # where other operation need to work in 100%.
    context.save()
    # Make all drawing scale to 50%
    context.scale(newScale)
    # Draw the scaled image at the bottom-left corner. It fills the whole page.
    context.image(path, pt(0, 0))

    # Saves the page as png file (and also do conversion from jpg to png this
    # way).
    if not os.path.exists('_export/'):
        os.makedirs('_export/')

    # Note that resulting images may look sharper, but has 4.5x the size of the .jpg.
    # 944Kb size
    context.saveImage('_export/%s-%s-%d-%s.png' % (FILENAME, IMAGENAME, newScale*100, contextName))
    # 168Kb size
    context.saveImage('_export/%s-%s-%d-%s.jpg' % (FILENAME, IMAGENAME, newScale*100, contextName))
    # 346Kb size
    context.saveImage('_export/%s-%s-%d-%s.gif' % (FILENAME, IMAGENAME, newScale*100, contextName))

    # Restores the graphics state, so context scaling is back to 100% after this.
    context.restore()

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
