#!/usr/bin/env python3
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
#     E10_TextByContext.py
#
#     Show some principles of FlatContext usage.

from pagebot import getContext
from pagebot.document import Document
from pagebot.constants import A3, TOP
from pagebot.conditions import *
from pagebot.elements import *
from pagebot.toolbox.units import *
from pagebot.toolbox.color import noColor, color
"""
from pagebot.toolbox.color import Color, blackColor, blueColor, greenColor
from pagebot.elements.paths.pagebotpath import PageBotPath
"""
for contextName in ('DrawBot', 'Flat'):
	print('Running example with', contextName)
	context = getContext(contextName)

	FILE_NAME = '_export/06_TextByContext%s.pdf' % contextName

	# Landscape A3.
	H, W = A3
	SQ = 150
	P  = 50
	fontSize = pt(300)

	# Create a new document for the current context. Create one automatic page.
	doc = Document(w=W, h=H, context=context)
	page = doc[1] # Get the one and single page of the document.
	page.padding = P, P, 2*P, P # Set the page padding, not equal to test vertical position.

	style = dict(font='PageBot-Regular', fontSize=fontSize, textFill=color(1))
	bs = context.newString('ABCD', style)
	# Parent of the element is the current page.
	e = newText(bs, w=SQ, h=SQ, parent=page, conditions=Fit(),
		fill=(0.8), stroke=noColor)
	print(e.bs) # <-- $ABCD$
	print(e.bs.cs) # FormattedString (DrawBot), <FlatBabelData (Flat)

	# Solve conditions of all placed elements on the page
	page.solve()

	if contextName == 'Flat':
		span = bs.cs.txt.paragraphs[0].spans[0]
		print('e.bs.cs.txt.paragraphs[0].spans[0].string', span.string, span.style.width(span.string))
		print('e.bs.cs.pt.width, e.bs.cs.pt.height', e.bs.cs.pt.width, e.bs.cs.pt.height)
		for height, run in e.bs.cs.pt.layout.runs():
			for rr in run:
				print('e.bs.cs.pt.layout.runs():', rr)
		print('e.bs.textSize:', e.bs.textSize)
		print('e.bs.getTextSize():', e.bs.getTextSize())
		print('e.bs.getTextSize(w=e.w, h=e.h):', e.bs.getTextSize(w=e.w, h=e.h))

		print('context.textSize(bs):', context.textSize(bs))
		print('context.textSize(bs, w=e.w, h=e.h):', context.textSize(bs, w=e.w, h=e.h))


		span = bs.cs.txt.paragraphs[0].spans[0]
		newRect(parent=page, w=span.style.width(span.string), h=bs.th, x=page.pl,
			y=page.ph-page.pt, yAlign=TOP,
			fill=None, stroke=color(1, 0, 0), strokeWidth=0.5)

	newRect(parent=page, w=bs.tw, h=bs.th, x=page.pl, y=page.ph-page.pt, yAlign=TOP,
		fill=None, stroke=color(0, 0, 1), strokeWidth=0.5)

	# Set some viewing parameters.
	view = doc.view
	view.showPadding = True # Show the padding of the page, where conditions align.

	# Export in _export folder that does not commit in Git. Force to export PDF.
	doc.export(FILE_NAME)


