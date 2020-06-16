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
from pagebot.typesetter import Typesetter
from pagebot.composer import Composer

# Sketch related SketchString --> BabelString conversion
import pysketch
from pagebot.contexts.sketchcontext.sketchcontext import SketchContext

FONT_NAME = 'PageBot-Regular'

EXPORT_PATH = '_export/E05_CreateSketchFile.pdf'

#templatePath = path2Dir(pagebot.__file__) + '/resources/sketchapp/Base.sketch'
contentPath = '/Users/petr/Desktop/PageBot-DeliciousTest/'
templatePath = contentPath + 'Delicious-template2.sketch'
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
sketchContext.readDocument(doc, contentPath=contentPath)

# Now er have read the position of frames, images and elements,
# let the composer match the input file(s) with the naming of text
# blocks that refer to a file + overflow index.
typesetter = Typesetter(drawBotContext)
galley  = typesetter.typesetFile(contentPath + 'Stoven.md')
composer = Composer(doc)

# Set output flag in the doc.view
view = doc.view
view.padding = pt(40)
view.showCropMarks = True
view.showRegistrationMarks = True
view.showPadding = True # Show the page padding
view.showFrame = True # Show the frame of the  page as blue line
view.showNameInfo = True # Showing page info and title on top of the page.
view.showGrid = doc[1].showGrid

doc.export(EXPORT_PATH)


