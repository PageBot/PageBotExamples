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
SQ = 150
P  = 50

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
    c = (Right2Right(), Float2Top(), Float2Left())
    #c = (Left2Left(), Top2Top())
    #r = newRect(w=SQ, h=SQ, parent=page, conditions=c,
    #        fill=(0,0,1), stroke=0, showOrigin=True)

    # Create a new red circle element and align it on top-left,
    # floating to that position relative to what is already there.
    # Parent of the element is the current page.
    o = newCircle(r=SQ, parent=page, conditions=c, fill=(1, 0, 0),
            stroke=0, showOrigin=True)
    o = newCircle(r=SQ, parent=page, conditions=c, fill=(1, 0, 0),
            stroke=0, showOrigin=True)
    '''

    # Create a new black diagonal line element and align it on top-left,
    # floating to that position relative to what is already there.
    l = newLine(parent=page, x=0, y=0, w=100, h=100, conditions=c, stroke=0, strokeWidth=10)
    points=[(0,0), (100, 0), (150, 50), (150, 100), (100, 200)]
    # A quire is a drawboard
    q = newQuire(parent=page, conditions=c, fill=1, strokeWidth=5, stroke=0.5)
    # Make a rect with  more height, so it will push down any floating from below.
    r = newRect(w=SQ, h=2*SQ, parent=page, conditions=c, fill=noColor, stroke=0, strokeWidth=1)

    # Create two text boxes and align it on top-left,
    # floating to that position relative to what is already there.
    newText('Text    !', parent=page, conditions=c, fontSize=60, stroke=(1, 1, 0),
            strokeWidth=20, textFill=0.5, font=font)
    newText('Text Box', parent=page, conditions=c, stroke=0, strokeWidth=0.5, fill=(1, 1, 0),
            fontSize=30, font=font, textFill=(0, 0, 1))
    '''

    '''
    # A number of circles that will float the remaining space.
    for n in range(50):
        rr = pt(40)
        o = newOval(w=rr, h=rr/2, parent=page, conditions=c, fill=(1, 0, 0.5), stroke=0, strokeWidth=0.5)
    '''

    '''
    # Create two text boxes and align it on top-left,
    # floating to that position relative to what is already there.
    newRect(parent=page, conditions=(Left2Left(), Fit2Width(), Float2Top(), Fit2Bottom()),
            fill=0.9, showOrigin=True)
    '''

    # Solve conditions of all placed elements on the page
    page.solve()

    # Set some viewing parameters.
    view = doc.view
    view.showPadding = True # Show the padding of the page, where conditions align.

    # Export in _export folder that does not commit in Git. Force to export PDF.
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
