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
#     E01_VerticalMetricsInSketch.py
#
#	  https://blog.sketchapp.com/typesetting-in-sketch-dc870fc334fc
#
#	  Sketch has a special way to decide on vertical positioning of text line.
#
from pagebot.contexts.basecontext.babelstring import BabelString
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

EXPORT_PATH = '_export/E01_VerticalMetricsInSketch.pdf'
EXPORT_PATH_MODIFIED = '_export/E01_VerticalMetricsInSketch_Modified.pdf'

# Get a SketchString from an existing Sketch template file, 
# convert the string to BabelString with SketchContext flavor.
path = 'VerticalMetrics.sketch'
context = SketchContext(path)
print('SketchContext:', context)
artboard = context.b.artboards[0] # Get the first artboard of the Sketch file
print('Artboard:', artboard) 
# Find a Text in the list of elements
for eIndex, e in enumerate(artboard.layers):
	if e.__class__.__name__ == 'SketchText':
		skText = e # Get the text from the first artboard layer
		print('Artboard.layers[%d]:' % eIndex, skText)
		break
print('skText.attributedString:', skText.attributedString)
# The SketchContext knows how to convert the attributed string to BabelString.
bs = context.asBabelString(skText.attributedString)
print('BabelString.runs:', bs.runs)
print('BabelString.runs[-1].style', bs.runs[-1].style.keys())
font = bs.runs[-1].style['font']
fontSize = bs.runs[-1].style['fontSize']
leading = bs.runs[-1].style['leading']
print('Font/fontSize/leading:', font, fontSize, leading)

# Create a drawBotContext to save the Sketch based Document as other format.
# The content and styles of the BabelStrings comes from the Sketch file,
# but they are converted to DrawBot behavior, able to export to PDF.
drawBotContext = getContext('DrawBot')
# Create a Document instance with this DrawBotContext and let the 
# SketchContext read its pages into it.
doc = Document(name='TestBabelString', context=drawBotContext)
# Read the Sketch file, convert SketchAttributedStrings into BabelStrings
context.readDocument(doc) 
print('Doc page size', doc.w, doc.h, doc[1].w, doc[1].h)
# Eport the document "as is" for checking consistency with the original.
doc.export(EXPORT_PATH)

# Now we'll make some modifications.
# Get the first page of the document
page = doc[1]
# Get one of the the SketchText that is now on the page as PageBot Text element.
for e in page.elements:
	if isinstance(e, Text):
		break
print('Element type:', e.__class__.__name__, )
e.fill = 0.8
print('Text element from file:', e)
print('Text element vertical alignment:', e.yAlign)
print('BabelString context:', e.bs.context, 'Font in run:', e.bs.runs[0].style['font'])
# Move the element
e.x += 200
# Export as different name.
doc.export(EXPORT_PATH_MODIFIED)


