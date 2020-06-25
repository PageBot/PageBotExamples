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

    FILE_NAME = '_export/07_LinesByContext%s.pdf' % contextName

    # Landscape A3.
    H, W = A3
    SQ = 150
    P  = 50

    # Create a new document for the current context. Create one automatic page.
    doc = Document(w=W, h=H, context=context)
    page = doc[1] # Get the one and single page of the document.
    page.padding = P, P, 2*P, P # Set the page padding, not equal to test vertical position.

    style = dict(font='PageBot-Regular', fontSize=100, textFill=color(0), w=800)
    bs = context.newString('ABCD', style, w=800)
    print(bs.w)
    #print(bs.topLineXHeight)
    bs.add('EFGH', dict(fontSize=200, textFill=color(0, 1, 0)))
    print(bs.w)
    #print(bs.topLineXHeight)
    bs.add('IJKL', dict(fontSize=300))
    #print(bs.topLineXHeight)
    #print(bs.bottomLineDescender)
    #print(bs.bottomLineDescender_p)

    # Parent of the element is the current page.
    e = newText(bs, w=SQ, h=SQ, parent=page, conditions=Fit())
    print(bs.w)
    x, y, w, h = e.x, e.y, e.w, e.h
    newRect(parent=page, w=w, h=h, x=x, y=y, fill=None, stroke=color(0, 0, 1),
            strokeWidth=0.5)



    #print(e.bs)
    #print(e.bs.cs) # FormattedString (DrawBot), <FlatBabelData (Flat)

    for line in bs.lines:
        for run in line.runs:
            print(' * run', run)

    # Solve conditions of all placed elements on the page
    page.solve()

    view = doc.view
    #view.showPadding = True

    # Export in _export folder that does not commit in Git. Force to export PDF.
    doc.export(FILE_NAME)


