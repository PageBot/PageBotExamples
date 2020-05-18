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
#     E01_HkpgxH110FromSketch.py
#
#	  https://blog.sketchapp.com/typesetting-in-sketch-dc870fc334fc
#
#	  Sketch has a special way to decide on vertical positioning of text line.
#
from pagebot.contexts.basecontext.babelstring import BabelString
from pagebot.contexts import getContext
from pagebot.constants import XHEIGHT, RIGHT
from pagebot.toolbox.transformer import path2Dir
from pagebot.toolbox.units import pt, em, upt
from pagebot.toolbox.color import color, noColor
from pagebot.document import Document
from pagebot.elements import *

# Sketch related SketchString --> BabelString conversion
import sketchapp2py
from pagebot.contexts.sketchcontext.sketchcontext import SketchContext

FONT_NAME = 'PageBot-Regular'

LINE_HEIGHT = 110

# Get a SketchString from an existing Sketch template file, 
# convert the string to BabelString with SketchContext flavor.
path = 'HpgxH%d.sketch' % LINE_HEIGHT
#path = 'HpgxH%dImpact.sketch' % LINE_HEIGHT
EXPORT_PATH = '_export/' + path + '.pdf'

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
#exportContext = getContext('DrawBot')
exportContext = getContext('Flat')
# Create a Document instance with this exportContext and let the 
# SketchContext read its pages into it.
doc = Document(name='TestBabelString', context=exportContext)
# Read the Sketch file, convert SketchAttributedStrings into BabelStrings
context.readDocument(doc) 
print('Doc page size', doc.w, doc.h, doc[1].w, doc[1].h)

# Now we'll make some modifications.
# Get the first page of the document
page = doc[1]
print('Page size:', page.w, page.h)
# Get one of the the SketchText that is now on the page as PageBot Text element.
for e in page.elements:
	if isinstance(e, Text):
		break
print('Element type:', e.__class__.__name__, e.x, e.y, e.w, e.h)
e.showOrigin = True
#e.y = 80
print('Textbox e height:', e.h)

G = 0
labelSize = pt(9)
labelLeading = labelSize*2.4
lineStyle1 = dict(fill=noColor, stroke=0, strokeWidth=0.5)
lineStyle2 = dict(fill=noColor, stroke=(0, 0, 0.7), strokeWidth=1)
lineStyle3 = dict(fill=noColor, stroke=(1, 0, 0), strokeWidth=2)
labelStyle = dict(font=font, fontSize=labelSize, textFill=0.4)

# Font em measure to pt factor
f2pt = fontSize / font.info.unitsPerEm

ascender = f2pt * font.info.ascender
descender = f2pt * font.info.descender

lines = (
	('ascender', ascender, lineStyle1),
	('typoAscender',f2pt * font.info.typoAscender, lineStyle2),
	('e-top', e.h + descender - (e.h - fontSize)/2, lineStyle2),
	('capHeight', f2pt * font.info.capHeight, lineStyle1),
	('xHeight', f2pt * font.info.xHeight, lineStyle1),
	('baseline', 0, lineStyle3),
	('typoDescender', f2pt * font.info.typoDescender, lineStyle2),
	('descender', descender, lineStyle2),
	('e-bottom', descender - (e.h - fontSize)/2, lineStyle2),
)
for lIndex, (label, my, style) in enumerate(lines):
	lIndex = len(lines)-lIndex
	newLine(x=e.x, y=e.y+my, w=e.w-60, h=0, style=style, parent=page)
	newText('%s: %d (%d)' % (label, my, font.info.unitsPerEm/fontSize*my), parent=page, style=labelStyle, 
		xAlign=RIGHT, x=e.x-G, y=e.y+labelLeading*lIndex-90, yAlign=XHEIGHT)
	newLine(x=e.x-40, y=e.y+labelLeading*lIndex-90, w=40, h=-labelLeading*lIndex+my+90, style=style, parent=page)

# Eport the document "as is" for checking consistency with the original.
doc.export(EXPORT_PATH)
