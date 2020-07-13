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
#     DrawRedRectCenterPage.py
#
#     Needs debugging in dimension showing of views.
#
from pagebot import getContext
from pagebot.conditions import *
from pagebot.constants import A5, CENTER, MIDDLE, EXPORT
from pagebot.document import Document
from pagebot.elements import newRect
from pagebot.style import getRootStyle
from pagebot.toolbox.color import Color
from pagebot.toolbox.transformer import path2FileName

W, H = A5
W = 400
H = 480
ShowOrigins = False
ShowElementInfo = False
RedRect = True # Show red or gray
RectSize = 300
FILENAME = path2FileName(__file__)

def draw(contextName):
    """Creates new document with (w,h) size and fixed amount of pages. Note
    that most of the rootStyle is cascading through the e.css('name') call,
    except that values of x, y, z, w, h, d."""
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)

    # Just to show here how to get the root style. If not altered, it can be omitted.
    # as Document( ) will create a RootStyle by default.
    rootStyle = getRootStyle()

    doc = Document(rootStyle, w=W, h=H, context=context)
    page = doc[1] # Get the first/single page of the document.
    page.padding = 40 # TODO: order if 4 values?

    # Make rect as page element centered with centered origin.
    if RedRect:
        c = Color(1, 0, 0)
    else:
        c = Color(0.5)

    conditions = (Center2Center(), Middle2Middle())
    newRect(fill=c, parent=page, w=RectSize, h=RectSize,
            conditions=conditions, xAlign=CENTER, yAlign=MIDDLE)
    # Solve the layout conditions of the red rectangle.
    # Show if one of the conditions failed to solve.
    score = page.solve()
    if score.fails:
        print('Failed conditions', score.fails)

    # Set the view parameters for the required output.
    view = doc.getView()
    view.w = view.h = W, H
    view.padding = 40 # Make view padding to show crop marks and frame
    view.showFrame = True # Show frame of the page in blue
    view.showPadding = False
    view.showCropMarks = True # Show crop marks
    view.showOrigin = ShowOrigins # Show origin alignment markers on each element.
    view.showDimensions = ShowOrigins
    view.showElementInfo = ShowElementInfo # Show baxes with element info element.
    page.solve()
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
