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
#     E00_HelloWorld.py
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
    txt = 'Hello World'
    bs = context.newString(txt, dict(font=fontName, fontSize=pt(96)))
    f = color(0.8)
    textBox = newText(bs, x=W/2, y=W/4, w=W/2, h=H/2, parent=page, showDimensions=True,
            showFrame=True, showOrigin=True, xTextAlign=CENTER, fill=f, showElementInfo=True)

    # Export in _export folder that does not commit in Git. Force to export PDF.
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
