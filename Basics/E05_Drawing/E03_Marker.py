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
#     E03_Marker.py
#
#     For demo, run this in DrawBot, with PageBot installed.
#
#     Some examples showing the working of BabelString with context
#     without the making of Document and Text elements.
#
from pagebot import getContext
from pagebot.constants import *
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt, em
from pagebot.toolbox.transformer import path2FileName

W, H = 100, 100 #A4 # Standard paper size from constants.
FILENAME = path2FileName(__file__)

def drawMarkers(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    context.newPage(W, H) # Make a new A4 page.


    context.marker(1, 10, fontSize=2)
    context.marker(1, 1, fontSize=2)
    context.marker(10, 1, fontSize=2)
    context.marker(10, 10, 2, fontSize=2)
    context.saveImage(exportPath)

for contextName in ('DrawBot', 'Flat'):
    drawMarkers(contextName)
