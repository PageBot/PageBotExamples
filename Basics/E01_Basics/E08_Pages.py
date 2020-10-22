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
#     E08_Pages.py
#
#     Test handling of pages in a document.
#

from pagebot.contexts import getContext
from pagebot.document import Document
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt, mm
from pagebot.constants import CENTER, LEFT, EXPORT
from pagebot.toolbox.transformer import path2FileName

# Template for the export path, allowing to include context name
W, H = mm(120), pt(300)
FONT_NAME = 'Roboto-Regular'
FILENAME = path2FileName(__file__)

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    doc = Document(w=W, h=H, context=context)
    # Gets the first page from te document.
    page = doc[1]
    page.name = 'First page'
    page.padding = 20
    #print('One page in the document of %s x %s' % (page.w, page.h))
    view = doc.getView()
    view.showPadding = True

    style = dict(font=FONT_NAME, fontSize=pt(50), xTextAlign=LEFT)
    bs = context.newString(page.name, style=style)

    # Try other positions
    #conditions= (Left2Left(), Top2SideTop())
    #conditions= (Right2Right(), Top2SideTop())
    #conditions = (Center2Center(), Middle2Middle())
    #conditions = (Center2Center(), Top2SideTop())
    #conditions = (Left2Left(), Bottom2Bottom())
    conditions = (Left2Left(), Float2Left(), Bottom2Bottom())

    # Position rectangle in the center of the page area. Notice that the (x, y)
    # position is undefined, default is (0, 0), since will be filled by the
    # condition. Size measures can be any type of units. Their type is shown
    # in the measured output.
    e = newText(bs, w=100, h=100, parent=page, #pl=3, pt=3,
            showDimensions=True, showOrigin=True, #xAlign=CENTER,
            conditions=conditions, stroke=color(1, 0, 0), strokeWidth=1)
    f = newRect(w=100, h=100, parent=page, conditions=conditions, showOrigin=True, fill=color(0, 1, 0))
    g = newRect(w=100, h=100, parent=page, conditions=conditions, showOrigin=True, fill=color(0, 0, 1))

    #print((mm(120) - mm(86))/2)
    page.solve()
    #print(e.x, e.y, e.w, e.h)
    #print(e.bs.lines[0].y)
    #print(e.bs.style)
    #print(e.bs.lines)

    # Export in _export folder that does not commit in Git. Force to export PDF.
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
