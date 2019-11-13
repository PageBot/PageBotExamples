#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     HandleDocWithPages.py
#
#     Test handling of pages in a document.
#
#import pagebot # Import to know the path of non-Python resources.

from pagebot.document import Document
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt, mm

W, H = pt(400, 300)

# Export in _export folder that does not commit in Git. Force to export PDF.
EXPORT_PATH = '_export/HandleDocWithPages.pdf'

doc = Document(w=W, h=H, originTop=False, autoPages=1)
print('One page in the document', doc.pages)

view = doc.getView()
view.showPadding = True
view.showDimensions = True
view.showOrigin = True

page = doc[1] # Get the single page from te document.
page.name = 'First page'
page.padding = 20

conditions = (Center2Center(), Middle2Middle())
# Try other positions
#conditions= (Left2Left(), Top2SideTop())
#conditions= (Right2Right(), Top2SideTop())

# Position square in the center of the page area.
# Notice that their alignment (left) does not matter for the conditions.
# Measures can be any type of units.
# Their type is show in the measured output.
newTextBox(page.name, w=mm(86), h=pt(164), parent=page, pl=3, pt=3,
    showDimensions=True,
    conditions=conditions, fill=color(0.8))

page.solve()


doc.export(EXPORT_PATH)

