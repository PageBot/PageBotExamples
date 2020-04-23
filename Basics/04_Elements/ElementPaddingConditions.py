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
#     ElementConditions.py
#
#     Position elements by their page padding position with conditions
#
# Document is the main instance holding all information about
# the document togethers (pages, styles, etc.)
from pagebot.document import Document
from pagebot.elements import newRect
from pagebot.toolbox.units import p, pt
from pagebot.toolbox.color import color
from pagebot.conditions import *

W = H = pt(500)
PADDING = p(4)

def makeDocument(context):
    w = p(8)

    doc = Document(w=W, h=H, context=context)
    page = doc[1] # Get the single page from te document.
    page.padding = PADDING

    page.showPadding = True

    newRect(parent=page, w=w, h=w, fill=color('red'), conditions=[Left2Left(), Bottom2Bottom()])
    newRect(parent=page, w=w, h=w, fill=color('green'), conditions=[Center2Center(), Top2Top()])
    newRect(parent=page, w=w, h=w, fill=color('blue'), conditions=[Right2Right(), Top2Top()])
    newRect(parent=page, w=w, h=w, fill=color('orange'), conditions=[Left2Left(), Middle2Middle()])
    newRect(parent=page, w=w, h=w, fill=color('yellow'), conditions=[Left2Left(), Top2Top()])
    newRect(parent=page, w=w, h=w, fill=color('purple'), conditions=[Bottom2Bottom(), Right2Right()])
    newRect(parent=page, w=w, h=w, fill=color('violet'), conditions=[Middle2Middle(), Right2Right()])
    newRect(parent=page, w=w, h=w, fill=color('cyan'), conditions=[Center2Center(), Bottom2Bottom()])
    newRect(parent=page, w=w, h=w, fill=color('black'), conditions=[Center2Center(), Middle2Middle()])

    page.solve()

    # Export in _export folder that does not commit in Git. Force to export PDF.
    EXPORT_PATH = '_export/ElementPaddingConditions-%s.pdf' % context.name
    doc.export(EXPORT_PATH)

if __name__ == '__main__':
    from pagebot import getContext

    for contextName in ('DrawBot', 'Flat'):
        context = getContext(contextName)
        makeDocument(context)
