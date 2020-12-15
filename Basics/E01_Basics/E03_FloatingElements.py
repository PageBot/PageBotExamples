#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     www.pagebot.io
#     Licensed under MIT conditions
#
# -----------------------------------------------------------------------------
#
#     E03_FloatingElements.py
#
#     Make a page with a variety of elements and use conditions to place them.

from pagebot import getContext
from pagebot.toolbox.units import *
from pagebot.toolbox.color import Color, blackColor, blueColor, greenColor
from pagebot.elements import *
from pagebot.document import Document
from pagebot.toolbox.color import blueColor, darkGrayColor, redColor, Color, noColor, color
from pagebot.conditions import *
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.constants import A3, EXPORT
from pagebot.toolbox.transformer import path2FileName

FILENAME = path2FileName(__file__)
H, W = A3
X0 = 100
Y0 = 100
SQ = 50
P  = 50
N = 70
F = 1.0 / N

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)

    # Landscape A3.
    font = findFont('PageBot-Regular') # TYPETR Upgrade® subset font for demo.

    # Create a new document for the current context. Create one automatic page.
    doc = Document(w=W, h=H, context=context)
    page = doc[1] # Get the one and single page of the document.
    page.padding = P # Set the page padding.

    c = (Right2Right(), Float2Top(), Float2Left())
    #c = (Float2Top(), Float2Left())
    #c = ()
    #c = (Float2Top())
    #c = (Right2Right()) #Float2Top(), Float2Left())
    #c = (Left2Left(), Top2Top())

    # Creates new geometric elements and aligns them.
    for i in range(N):
        r = F
        g = 0
        b = F/2
        f = (i*r, i*g, i*b)

        if i % 3 == 0:
            newCircle(r=SQ, parent=page, conditions=c, fill=f,
                    stroke=0, showOrigin=True)
        elif i % 3 == 1:
            newOval(w=2*SQ, h=2*SQ/2, parent=page, conditions=c, fill=f, stroke=0, strokeWidth=0.5)
        else:
            newRect(r=SQ, parent=page, conditions=c, fill=f,
                    stroke=0, showOrigin=True)

    # Solve conditions of all placed elements on the page
    score = page.solve()

    # Set some viewing parameters.
    view = doc.view

    # Show the padding of the page, where conditions align.
    view.showPadding = True

    # Export in _export folder that does not commit in Git. Force to export PDF.
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
