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
#     E10_BabelStringFromSketch.py
#
#     BabelStrings are the (new) internal string format that can hold any information
#     that contexts need for their own formatted strings.
#     The store the context that created them, as well as context native representations
#     of the string, text size and lines with recovered styles per run.
#
#     This way abcString-->BabelString-->xyzString needs only two convertors, local
#     to the context, instead of writing converters from all contexts to all contexts.
#     In the original architecture of PageBot, the DrawBot FormattedStrings were used as
#     native format. But that only works in MacOS, and it only works to generate them,
#     not to retrieve information from them easily. 
#     While PageBot is extending the number of contexts, it no longer needs to run
#     on MacOS and contexts like SketchContext needs to read and write it strings into
#     PageBot elements, there is more need for a generic common independent format.
#
#     Since we control the BabelString format, all contexts must implement some basic
#     conversions, such as context.textSize, context.textLines, context.overflow,
#     fromBabelString and asBabelString() methods, without the need to know about
#     string behavior of any of the other contexts.
# 

from pagebot.contexts.basecontext.babelstring import BabelString
from pagebot.contexts import getContext
from pagebot.toolbox.transformer import path2Dir
from pagebot.toolbox.units import pt, em
from pagebot.toolbox.color import color
from pagebot.document import Document

# Sketch related SketchString --> BabelString conversion
import sketchapp2py
from sketchcontext.context import SketchContext

FONT_NAME = 'PageBot-Regular'

EXPORT_PATH = '_export/E01_BabelStringFromSketch.pdf'

# Create a BabelString, that PageBot uses in internal in text elements.
# This plain BabelString has no context defined, so we can't apply 
# rendering methods, such as bs.textSize
style = dict(font=FONT_NAME, fontSize=pt(18), textFill=color(1, 0, 0))
bs = BabelString('ABCD', style=style)
print('BabelString:', bs)

# Creating a BabelString, with context, those rendering methods work.
context = getContext('DrawBot')
style = dict(font=FONT_NAME, fontSize=pt(18), textFill=color(1, 0, 0))
bs = context.newString('EFGH', style=style) # Now the BabelString has a context.
print('BabelString:', bs)
print('BabelString.textSize', bs.textSize)

# Get a SketchString from file, convert the string to BabelString
path = path2Dir(sketchapp2py.__file__) + '/Resources/TemplateText.sketch'
context = SketchContext(path)
print('SketchContext:', context)
artboard = context.b.artboards[0] # Get the first artboard of
print('Artboard:', artboard) 
skText = artboard.layers[0] # Get the text from the first artboard layer
print('Artboard.layers[0]:', skText)
# The SketchContext knows how to convert the attributed string to BabelString.
bs = context.asBabelString(skText.attributedString)
print('BabelString:', bs)

# Create a drawBotContext to save the Sketch based Document as other format.
drawBotContext = getContext('DrawBot')
# Create a Document instance and let the SketchContext read its pages into it.
doc = Document(name='TestBabelString', context=drawBotContext)
# Read the Sketch file, convert SketchAttributedStrings into BabelStrings
context.readDocument(doc) 
# Get the first page of the document
page = doc[1]
# Get the Sketch text that is now on the page as PageBot Text element.
e = page.elements[0] 
e.fill = 0.8
print(e, e.yAlign)
print(e.bs.runs[0].style['font'])
# Move the element
e.x += 200
doc.export(EXPOT_PATH)


