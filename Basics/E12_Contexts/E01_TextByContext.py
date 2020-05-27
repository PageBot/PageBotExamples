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
#     E01_TextByContext.py
#
#     Show some principles of FlatContext usage.

from pagebot import getContext
from pagebot.document import Document
from pagebot.constants import A5
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

	FILE_NAME = '_export/01_TextByContext%s.pdf' % contextName

	# Landscape A3.
	H, W = A5
	SQ = 150
	P  = 50
	fontSize = pt(150)

	# Create a new document for the current context. Create one automatic page.
	doc = Document(w=W, h=H, context=context)
	page = doc[1] # Get the one and single page of the document.
	page.padding = P # Set the page padding.

	style = dict(font='PageBot-Regular', fontSize=fontSize, textFill=color(1))
	bs = context.newString('ABCD', style)
	# Parent of the element is the current page.
	r = newText(bs, w=SQ, h=SQ, parent=page, conditions=Fit(), 
		fill=(0.2,0.2,0.5), stroke=noColor)
	print(r.bs) # <-- $ABCD$
	print(r.bs.cs) # FormattedString (DrawBot), <FlatBabelData (Flat)

	# Solve conditions of all placed elements on the page
	page.solve()

	# Set some viewing parameters.
	view = doc.view
	view.showPadding = True # Show the padding of the page, where conditions align.

	# Export in _export folder that does not commit in Git. Force to export PDF.
	doc.export(FILE_NAME)


