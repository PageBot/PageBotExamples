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
#     E03_FitOvalByContext.py
#
#     Show some principles of FlatContext usage.

from pagebot import getContext
from pagebot.document import Document
from pagebot.constants import A5
from pagebot.conditions import *
from pagebot.elements import *
from pagebot.toolbox.units import *
from pagebot.toolbox.color import noColor, color

for contextName in ('DrawBot', 'Flat'):
	context = getContext(contextName)

	FILE_NAME = '_export/03_FitOvalByContext%s.pdf' % contextName

	# Landscape A3.
	H, W = A5
	SQ = 150
	P  = 50

	# Create a new document for the current context. Create one automatic page.
	doc = Document(w=W, h=H, context=context)
	page = doc[1] # Get the one and single page of the document.
	page.padding = P, P, 2*P, P # Set the page padding, not equal to test vertical position.

	# Parent of the element is the current page. 
	# Use conditions to make it fit the page.
	newOval(parent=page, conditions=Fit(), fill=color(1,0,0), stroke=noColor)

	# Solve conditions of all placed elements on the page
	page.solve()

	# Set some viewing parameters.
	view = doc.view
	view.showPadding = True # Show the padding of the page, where conditions align.

	# Export in _export folder that does not commit in Git. Force to export PDF.
	doc.export(FILE_NAME)


