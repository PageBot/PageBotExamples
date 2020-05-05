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
#     E00_CreateSketchFile.py
#
#     As it is much easier to use an existing Sketch document, than creating
#     one from scratch, we use one of the exiting template documents, such as
#     PageBot/resources/sketchapp/Base.sketch
# 

import pagebot
from pagebot.contexts import getContext
from pagebot.toolbox.transformer import path2Dir
from pagebot.toolbox.units import pt, em
from pagebot.toolbox.color import color
from pagebot.document import Document
from pagebot.elements import *

# Sketch related SketchString --> BabelString conversion
import sketchapp2py
from pagebot.contexts.sketchcontext.sketchcontext import SketchContext

FONT_NAME = 'PageBot-Regular'

EXPORT_PATH = '_export/E05_CreateSketchFile.pdf'

#templatePath = path2Dir(pagebot.__file__) + '/resources/sketchapp/Base.sketch'
templatePath = '/Users/petr/Desktop/PageBot-DeliciousTest/Delicious-template.sketch'
#templatePath = '/Users/petr/Desktop/PageBot-DeliciousTest/TEST.sketch'
sketchContext = SketchContext(templatePath) # Used for reading/writing Sketch files.

# Create a drawBotContext to save the Sketch based Document as other format.
# The content and styles of the BabelStrings comes from the Sketch file,
# but they are converted to DrawBot behavior, able to export to PDF.
drawBotContext = getContext('DrawBot')
# Create an empty Document instance with this DrawBotContext and let the 
# SketchContext read its pages into it, setting page sizes, etc.
doc = Document(title=EXPORT_PATH, context=drawBotContext)
# Read the Sketch file, convert SketchAttributedStrings into BabelStrings
sketchContext.readDocument(doc) 
# Set output flag in the doc.view
view = doc.view
view.padding = pt(40)
view.showCropMarks = True
view.showRegistrationMarks = True
view.showPadding = True # Show the page padding
view.showFrame = True # Show the frame of the  page as blue line
view.showNameInfo = True # Showing page info and title on top of the page.
view.showGrid = doc[1].showGrid
print(view.showGrid)
# Add colums
page = doc[7]
g = page.gw
cw = page.gridX[0][0]
print(g, cw, page.w-52-52)
fff = (0, 0, 0, 0.2)
print(page.gridX, page.gw)

newRect(parent=page, x=page.pl, w=cw, y=page.pb, h=page.ph, fill=fff)
newRect(parent=page, x=page.pl+cw+g, w=cw, y=page.pb, h=page.ph, fill=fff)
newRect(parent=page, x=page.pl+cw+g+cw+g, w=cw, y=page.pb, h=page.ph, fill=fff)
doc.export(EXPORT_PATH)


