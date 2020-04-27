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
#     ScalingAnImage.py
#
#     How to scale an image (without being an element) in plain DrawBot?
#     Since the core DrawBot does not support w/h attrbiutes for images,
#     it needs to be done by using the scale() function.
#
#     Unfortunately this also changes to x/y position scale, so when
#     drawing an image on the canvas, the position must be scaled the
#     other way around. In this example it doesn't matter, because the
#     scaled image is positioned at (0, 0).
#
import os # Import module that communicates with the file system.
import sys

from pagebot.document import Document
from pagebot.filepaths import getResourcesPath
from pagebot.toolbox.units import pt, mm
from pagebot import getContext
from pagebot.constants import A4
from pagebot.elements import *
from pagebot.conditions import *

context = getContext()

W, H = mm(1000, 240) 

M = pt(12) # Margin between the images
P = mm(30) # Padding of the page

EXPORT_PATH = '_export/01_CacheScaledImage.pdf'

# Define the path where to find the example image.
path = getResourcesPath() + "/images/cookbot1.jpg"
# Use the standard DrawBot function to get the width/height of the image from the file.
doc = Document(w=W, h=H, context=context) # New simple document with default padding.

page = doc[1] # Get first (and only) automatic page.
page.padding = P
factor = 5 # Incremental scale division factor of the image width.

for n in range(15): # Stop before they become invisible small
	# Create a range of scaled imaged that try to fit by floating conditions.
	newImage(path, w=page.pw/factor, mr=10*M/(n+1), parent=page,
		conditions=(Right2Right(), Float2Top(), Float2Left()),
		scaleImage=False)
	factor *= 1.3

doc.solve() # Solve the fitting of the scaled images on the page.

doc.export(EXPORT_PATH)
