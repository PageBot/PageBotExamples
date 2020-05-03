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

# Template for the export path, allowing to include context name
EXPORT_PATH = '_export/E00_DocumentWithPages-%s.pdf' 

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

    newText(page.name, w=mm(86), h=pt(164), parent=page, pl=3, pt=3,
        showDimensions=True,
        conditions=conditions, fill=color(0.8))

    page.solve()
    # Export in _export folder that does not commit in Git. Force to export PDF.
    doc.export(EXPORT_PATH % context.name)


for contextName in ('DrawBot', 'Flat'):
    context = getContext(contextName)
    makeDocument(context)
