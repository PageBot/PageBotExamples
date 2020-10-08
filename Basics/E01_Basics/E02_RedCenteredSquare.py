#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
# -----------------------------------------------------------------------------
#
#     E02_RedCenteredSquare.py
#
from pagebot import getContext
from pagebot.document import Document
from pagebot.elements import newRect
from pagebot.conditions import Center2Center, Middle2Middle
from pagebot.toolbox.units import pt
from pagebot.toolbox.color import color
from pagebot.constants import EXPORT
from pagebot.toolbox.transformer import path2FileName

FILENAME = path2FileName(__file__)

# Get size units.
W, H = pt(200, 200)

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    # Create document with default 1 page.
    doc = Document(w=W, h=H)
    # First page in the list is uneven (right side).
    page = doc[1]

    # Creates a new rectangle element with position conditions.
    newRect(parent=page, fill=color('red'), size=pt(140, 140),
        # Show measure lines on the element.
        showDimensions=True,
        conditions=[Center2Center(), Middle2Middle()])

    # Make the page apply all conditions.
    page.solve()

    # Exports the document page as PDF.
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
