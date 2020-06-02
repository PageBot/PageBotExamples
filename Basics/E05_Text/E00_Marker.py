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
#     E00_BabelString.py
#
#     For demo, run this in DrawBot, with PageBot installed.
#
#     Some examples showing the working of BabelString with context
#     without the making of Document and Text elements.
#
import traceback

from pagebot import getContext
from pagebot.constants import *
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt, em

W, H = 100, 100 #A4 # Standard paper size from constants.

def marker(contextName):
    context = getContext(contextName)
    context.newPage(W, H) # Make a new A4 page.


    context.marker(1, 10, fontSize=2)
    context.marker(1, 1, fontSize=2)
    context.marker(10, 1, fontSize=2)
    context.marker(10, 10, 2, fontSize=2)
    context.saveImage('_export/00_Marker-%s.pdf' % contextName)

for contextName in ('DrawBot', 'Flat'):
    marker(contextName)
