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
#import pagebotosx
#print(pagebotosx)

import flat
print(flat)

import booleanOperations
import fontTools
import sass
import markdown
import svgwrite
import tornado
