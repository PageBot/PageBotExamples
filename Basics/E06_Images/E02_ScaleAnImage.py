#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     www.pagebot.io
#     Licensed under MIT conditions
#
# -----------------------------------------------------------------------------
#
#     E02_ScaleAnImage.py
#

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

    newScale = 0.5

    # Make a page with the size of the scaled image, rounded to whole pixels.
    context.newPage(pt(int(w*newScale)), pt(int(h*newScale)))

    # Tells the context to use the new scale.
    context.scale(newScale)

    # Draws the scaled image at the bottom-left corner. It should fill the
    # entire page.
    context.image(path, pt(0, 0))

    # Saves the page as png file (and also do conversion from jpg to png this
    # way).
    if not os.path.exists('_export/'):
        os.makedirs('_export/')

    #context.saveImage('_export/%s-%s-%d-%s.png' % (FILENAME, IMAGENAME, newScale*100, contextName))
    context.saveImage('_export/%s-%s-%dpercent-%s.jpg' % (FILENAME, IMAGENAME, newScale*100, contextName))
    #context.saveImage('_export/%s-%s-%d-%s.gif' % (FILENAME, IMAGENAME, newScale*100, contextName))

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
