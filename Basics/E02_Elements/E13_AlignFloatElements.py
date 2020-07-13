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
#     E13_AlignFloatElements.py
#
#     This script generates a page with aligned square, showing how conditional
#     placement works. Interactive Variable() only works in DrawBot context.
#
# Creation of the RootStyle (dictionary) with all available default style parameters filled.
from pagebot import getContext
from pagebot.conditions import *
from pagebot.constants import CENTER, EXPORT
from pagebot.document import Document
from pagebot.elements import newRect
from pagebot.toolbox.color import (blueColor, darkGrayColor, redColor, Color,
        noColor, color)
from pagebot.toolbox.transformer import path2FileName

FILENAME = path2FileName(__file__)
G = 8 # Distance between the squares.
SQ = 8 * G # Size of the squares

# Variables used as interactive globals in DrawBot context.
ShowOrigins = False
ShowElementInfo = False
ShowDimensions = False
PageSize = 500
W = H = PageSize

def draw(contextName):
    """Make a new document."""
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)

    doc = Document(w=W, h=H, autoPages=1, context=context)
    page = doc[1] # Get the single page from te document.

    # Hard coded padding, just for simple demo, instead of filling padding and
    # columns in the root style.
    page.padding = SQ

    # Position square in the 4 corners of the page area. Notice that their
    # alignment (left) does not matter for the conditions.
    newRect(w=SQ, h=SQ, parent=page,
            conditions=(Right2Right(), Top2Top()), fill=darkGrayColor)
    newRect(w=SQ, h=SQ, parent=page,
            conditions=(Left2Left(), Bottom2Bottom()), fill=darkGrayColor)
    newRect(w=SQ, h=SQ, parent=page,
            conditions=(Left2Left(), Top2Top()), fill=darkGrayColor)
    newRect(w=SQ, h=SQ, parent=page,
            conditions=(Right2Right(), Bottom2Bottom()), fill=darkGrayColor)

    # Make new container for adding elements inside with alignment.
    # cnt = newRect(w=W-2*SQ, h=H-2*SQ,
    #               fill=color(0.8, 0.8, 0.8, 0.4),
    #               parent=page, margin=SQ, yAlign=BOTTOM,
    #               xAlign=CENTER, stroke=noColor,
    #               conditions=(Center2Center(), Middle2Middle()))

    # Add rectangles to the page,
    # using alignment conditions to position rules.
    newRect(w=SQ, h=SQ, stroke=noColor, parent=page, xAlign=CENTER,
            conditions=(Center2Center(), Middle2Middle()), fill=redColor)

    conditions = [(Center2Center(), Top2Top()),
                  (Center2Center(), Bottom2Bottom()),
                  (Left2Left(), Middle2Middle()),
                  (Right2Right(), Middle2Middle())]

    for condition in conditions:
        newRect(w=SQ, h=SQ, stroke=noColor, parent=page, xAlign=CENTER,
                conditions=condition, fill=color(1, 1, 0))

    sideConditions = [(Center2Center(), Top2SideTop()),
                      (Center2Center(), Bottom2SideBottom()),
                      (Left2SideLeft(), Middle2Middle()),
                      (Right2SideRight(), Middle2Middle())]
    for condition in sideConditions:
        newRect(w=SQ, h=SQ, stroke=noColor, parent=page, xAlign=CENTER,
                conditions=condition, fill=color(0.5, 1, 0))

    cornerConditions = [(Left2SideLeft(), Top2SideTop()),
                        (Right2SideRight(), Top2SideTop()),
                        (Left2SideLeft(), Bottom2SideBottom()),
                        (Right2SideRight(), Bottom2SideBottom())]
    for condition in cornerConditions:
        newRect(w=SQ, h=SQ, stroke=noColor, parent=page, xAlign=CENTER,
                conditions=condition, fill=blueColor)

    # Solves the layout placement conditions on the page by moving the elements
    # that are not on the right positions (which is all of them, because we did
    # not add point attributes when creating them.

    score = page.solve()
    if score.fails:
        print('Failed to solve %d conditions:' % len(score.fails))
    for condition, e in score.fails:
        print(e.bottom2SideBottom())
        print(condition, e, e.bottom,
              Bottom2SideBottom().test(e),
              e.isBottomOnSideBottom(), e.bottom)

    # Gets the current view of the document. This allows setting of parameters
    # how the document is represented on output.
    view = doc.view
    view.w, view.h = W, H

    # Sets view options. Full list is in elements / views / baseviews.py
    view.padding = 30 # Showing cropmarks and registration marks
                      # need >= 20 padding of the view.
    view.showRegistrationMarks = True
    view.showCropMarks = True
    view.showFrame = True
    view.showPadding = True
    view.showNameInfo = True

    # These values can be changed in the Variable window, when in DrawBot
    # context.
    view.showOrigin = ShowOrigins # Show origin alignment
    view.showDimensions = ShowDimensions
    view.showElementInfo = ShowElementInfo # Show boxes with element info
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
