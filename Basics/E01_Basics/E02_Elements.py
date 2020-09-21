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
#     E02_Elements.py
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

    # Create a new blue rectangle element and align it on top-left,
    # floating to that position in case something is already there.
    # Parent of the element is the current page.
    #c = (Float2Top(), Float2Left())
    #c = ()
    #c = (Float2Top())
    c = (Right2Right(), Float2Top(), Float2Left())
    #c = (Right2Right()) #Float2Top(), Float2Left())
    #c = (Left2Left(), Top2Top())

    # Create a new red circle element and align it on top-left,
    # floating to that position relative to what is already there.
    # Parent of the element is the current page.


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
    '''
    # Create two text boxes and align it on top-left,
    # floating to that position relative to what is already there.
    newText('Text    !', parent=page, conditions=c, fontSize=60, stroke=(1, 1, 0),
            strokeWidth=20, textFill=0.5, font=font)
    newText('Text Box', parent=page, conditions=c, stroke=0, strokeWidth=0.5, fill=(1, 1, 0),
            fontSize=30, font=font, textFill=(0, 0, 1))
    '''

    '''
    # Create two text boxes and align it on top-left,
    # floating to that position relative to what is already there.
    newRect(parent=page, conditions=(Left2Left(), Fit2Width(), Float2Top(), Fit2Bottom()),
            fill=0.9, showOrigin=True)
    '''

    # Solve conditions of all placed elements on the page
    score = page.solve()

    # Set some viewing parameters.
    view = doc.view
    view.showPadding = True # Show the padding of the page, where conditions align.

    # Export in _export folder that does not commit in Git. Force to export PDF.
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
