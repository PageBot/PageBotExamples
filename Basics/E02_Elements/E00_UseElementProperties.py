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
#     UseElementProperties.py
#

from pagebot.elements import *

W = H = 500

# Creates a new container class (or uses other specialized ELements).
e = Element(name='myElement')

# The default Element instance has the origin on (0pt, 0pt) and width / height of (100pt, 100pt).
print(e)
print('Position and size:', (e.x, e.y, e.w, e.h))

# Sets the position. (Most) elements know their position and size as properties.
e.x = 200
e.y = 100
e.w = 400
e.h = 500
print('New position and size:', (e.x, e.y, e.w, e.h))
print('Unique element Id (eId) for this element:', e.eId)

# Gets the element info string, as used in meta info boxes.
print('-' * 20)
print(e.getMetricsString())
print('-' * 20)

