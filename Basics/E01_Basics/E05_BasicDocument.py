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
#     E05_BasicDocument.py
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
from pagebot.toolbox.loremipsum import  loremIpsum

# Template for the export path, allowing to include context name
W, H = pt(800), pt(600)
FILENAME = path2FileName(__file__)
fontName = 'PageBot-Regular'
SQ = 50

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    doc = Document(w=W, h=H, context=context)
    # Gets the first page from te document.
    page = doc[1]
    page.name = 'First page'
    page.padding = 20
    view = doc.getView()
    view.showPadding = True
    txt = loremIpsum(doShuffle=True)
    bs = context.newString(txt, dict(font=fontName, fontSize=pt(24)))

    # Try other positions
    #conditions = (Left2Left(), Bottom2Bottom())
    conditions = (Right2Right(), Float2Top(), Float2Left(), )
    f = color(0.8)

    '''Position rectangle in the center of the page area. Notice that the (x, y)
    position is undefined, default is (0, 0), since will be filled by the
    condition. Size measures can be any type of units. Their type is shown in
    the measured output.'''

    newRect(r=SQ, parent=page, conditions=conditions, fill=f, stroke=0,
            showOrigin=True)

    newCircle(r=SQ, parent=page, conditions=conditions, fill=f, stroke=0,
            showOrigin=True)

    # FIXME: text box doesn't align correctly.
    e = newText(bs, w=2*SQ, h=2*SQ, parent=page, showDimensions=True,
            showFrame=True, showOrigin=True, conditions=conditions, fill=f,
            showElementInfo=True)


    page.solve()

    # Export in _export folder that does not commit in Git. Force to export PDF.
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
