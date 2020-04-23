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
#     DocumentWithPages.py
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


def makeDocument(context):
    doc = Document(w=W, h=H, autoPages=1, context=context)
    print('One page in the document', doc.pages)

    view = doc.getView()
    view.showPadding = True
    view.showDimensions = True
    view.showOrigin = True

    # Gets the first page from te document.
    page = doc[1]
    page.name = 'First page'
    page.padding = 20

    conditions = (Center2Center(), Middle2Middle())
    # Try other positions
    #conditions= (Left2Left(), Top2SideTop())
    #conditions= (Right2Right(), Top2SideTop())

    # Position square in the center of the page area. Notice that their alignment
    # (left) does not matter for the conditions. Measures can be any type of
    # units. Their type is show in the measured output.

    newTextBox(page.name, w=mm(86), h=pt(164), parent=page, pl=3, pt=3,
        showDimensions=True,
        conditions=conditions, fill=color(0.8))

    page.solve()
    # Export in _export folder that does not commit in Git. Force to export PDF.
    EXPORT_PATH = '_export/DocumentWithPages-%s.pdf' % context.name
    doc.export(EXPORT_PATH)

if __name__ == '__main__':
    from pagebot import getContext

    for contextName in ('DrawBot', 'Flat'):
        context = getContext(contextName)
        makeDocument(context)
