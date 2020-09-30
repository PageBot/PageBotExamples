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
    #conditions = ()
    conditions = (Right2Right(), Float2Top(), Float2Left(), )
    f = color(0.8)

    '''Position rectangle in the center of the page area. Notice that the (x, y)
    position is undefined, default is (0, 0), since will be filled by the
    condition. Size measures can be any type of units. Their type is shown in
    the measured output.'''

    rectangle = newRect(r=SQ, x=0, y=0, parent=page, conditions=conditions, fill=f, stroke=0,
            showOrigin=True, showElementInfo=True,)

    # FIXME: text box doesn't align correctly.
    textBox = newText(bs, w=2*SQ, h=2*SQ, parent=page, showDimensions=True,
            showFrame=True, showOrigin=True, conditions=conditions, fill=f,
            showElementInfo=True)#, yAlign='bottom')

    newCircle(r=SQ, parent=page, conditions=conditions, fill=f, stroke=0,
            showOrigin=True)


    '''
    print(rectangle.mTop)
    print(rectangle.top)
    print(rectangle.mBottom)
    print(rectangle.bottom)

    print(textBox.mTop)
    print(textBox.top)
    print(textBox.mBottom)
    print(textBox.bottom)
    '''
    page.solve()

    # Export in _export folder that does not commit in Git. Force to export PDF.
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
