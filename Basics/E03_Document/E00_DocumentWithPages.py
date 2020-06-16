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
#     E00_DocumentWithPages.py
#
#     Test handling of pages in a document.
#
from pagebot.contexts import getContext
from pagebot.document import Document
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt, mm
from pagebot.constants import CENTER, LEFT

# Template for the export path, allowing to include context name
EXPORT_PATH = '_export/E00_DocumentWithPages-%s.pdf'

W, H = mm(120), pt(300)

fontName = 'PageBot-Regular'

def makeDocument(context):
    doc = Document(w=W, h=H, context=context)
    # Gets the first page from te document.
    page = doc[1]
    page.name = 'First page'
    page.padding = 20

    print('One page in the document of %s x %s' % (page.w, page.h))

    view = doc.getView()
    view.showPadding = True

    bs = context.newString(page.name, dict(font=fontName, fontSize=pt(50),
        xTextAlign=LEFT))

    conditions = (Center2Center(), Middle2Middle())
    # Try other positions
    #conditions= (Left2Left(), Top2SideTop())
    conditions= (Right2Right(), Top2SideTop())
    #conditions= (Center2Center(), Top2SideTop())

    # Position rectangle in the center of the page area. Notice that the (x, y)
    # position is undefined, default is (0, 0), since will be filled by the
    # condition. Size measures can be any type of units. Their type is shown
    # in the measured output.
    e = newText(bs, w=mm(86), h=pt(164), parent=page, #pl=3, pt=3,
        showDimensions=True, showOrigin=True,# xAlign=CENTER,
        conditions=conditions, fill=color(0.8))

    print((mm(120) - mm(86))/2)
    page.solve()
    print(e.x, e.y, e.w, e.h)

    # Export in _export folder that does not commit in Git. Force to export PDF.
    doc.export(EXPORT_PATH % context.name)

for contextName in (
        'DrawBot',
        'Flat'
    ):
    context = getContext(contextName)
    makeDocument(context)
