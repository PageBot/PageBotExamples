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
#     E06_Elements.py
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

    conditions = (Right2Right(), Float2Top(), Float2Left(), )
    f = color(0.8)

    '''Position rectangle in the center of the page area. Notice that the (x, y)
    position is undefined, default is (0, 0), since will be filled by the
    condition. Size measures can be any type of units. Their type is shown in
    the measured output.'''
    options = dict(parent=page, showOrigin=True, showDimensions=True,
            showElementInfo=True, showFlowConnections=True,
            conditions=conditions, fill=f, stroke=0)

    rectangle = newRect(name='rect', r=SQ ,**options)
    textBox = newText(bs, name='text', w=2*SQ, h=2*SQ, **options)
    newCircle(name='circle', r=SQ, **options)
    newPolygon(name='polygon', points=[(0, 0), (20, 100), (40, 0), (60, 100), (80, 0), (100, 100)], **options)
    #newPaths(**options)

    from pagebot.fonttoolbox.fontpaths import getTestFontsPath
    from pagebot.fonttoolbox.objects.font import Font
    fontPath = getTestFontsPath() + '/google/roboto/Roboto-Medium.ttf'
    font = Font(fontPath)
    e = newGlyphPath(font['e'], **options)

    page.solve()

    # Export in _export folder that does not commit in Git. Force to export PDF.
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
