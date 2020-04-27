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
#     OriginPosition.py
#
#     The originTop attribute is no longer supported
#     (In never worked properly and was a lot of work to make consistent)
#     All y-origin is in bottom-left.
#
"""
# Document is the main instance holding all information about
# the document togethers (pages, styles, etc.)
from pagebot.document import Document
from pagebot.elements import newTextBox, newRect
from pagebot.toolbox.units import p
from pagebot.toolbox.color import color
from pagebot.conditions import *
from pagebot.constants import *

W = H = 500
PADDING = p(5)

def makeDocument(context):
    doc = Document(w=W, h=H, padding=PADDING, context=context)
    view = doc.view
    view.padding = PADDING
    view.showOrigin = True
    view.showPadding = True
    view.showFrame = True
    view.showCropMarks = True

    page = doc[1] # Get the single page from te document.
    print(page, 'Origin on top:', page.originTop) # Inherited from document
    e = newRect(x=0, y=0, w=100, h=100, parent=page, fill=0.5)
    print(e, 'yAlign', e.yAlign)
    e = newRect(w=100, h=100, parent=page, fill=0.5)
    e.top = page.h
    e.right = page.w

    page = page.next
    page.originTop = True # Force this page to have origin on top
    print(page, 'Origin on top:', page.originTop)
    # Auto aligns on top, yAlign initializing from page.originTop
    e = newRect(x=0, y=0, w=100, h=100, parent=page, fill=0.5)
    print(e, 'yAlign', e.yAlign)
    e = newRect(w=100, h=100, parent=page, fill=0.5, yAlign=TOP, xAlign=RIGHT)
    e.top = page.h
    e.right = page.w

    #doc.originTop = True
    page = page.next
    print(page, 'Origin on top:', page.originTop) # Inherited from document
    # Auto aligns on top, yAlign initializing from page.originTop
    e = newRect(x=0, y=0, w=100, h=100, parent=page, fill=0.5)
    print(e, 'yAlign', e.yAlign)
    e = newRect(w=100, h=100, parent=page, fill=0.5, yAlign=TOP, xAlign=RIGHT)
    e.top = page.h
    e.right = page.w

    # Export in _export folder that does not commit in Git. Force to export PDF.
    EXPORT_PATH = '_export/OriginPosition-%s.pdf' % context.name
    doc.export(EXPORT_PATH)

"""
