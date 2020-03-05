#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#    03_TestInstall.py
#

# Python version.
import sys
print(sys.version)
import platform
print (platform.python_version())

# Libary locations.
import site
print(site.getsitepackages())

# Pagebot.
import pagebot
from pagebot.constants import DEFAULT_TRACKING
print(pagebot)

# Uncomment on Mac.
#import pagebotcocoa
#print(pagebotcocoa)

import flat
print(flat)

import booleanOperations
import fontTools
import sass
import markdown
import svgwrite
import tornado
