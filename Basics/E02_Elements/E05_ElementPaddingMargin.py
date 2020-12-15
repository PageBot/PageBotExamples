#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#

#     www.pagebot.io
#     Licensed under MIT conditions
#


# -----------------------------------------------------------------------------
#
#     E05_ElementPaddingMargin.py
#
#     Show element padding and margin
#
from pagebot import getContext
from pagebot.constants import EXPORT
from pagebot.document import Document
from pagebot.elements import newRect
from pagebot.toolbox.units import p, pt
from pagebot.toolbox.color import color
from pagebot.conditions import *
from pagebot.toolbox.transformer import path2FileName

W = H = 500
PADDING = p(2)
MARGIN = p(1)
FILENAME = path2FileName(__file__)

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    doc = Document(w=W, h=H, context=context)
    view = doc.view
    view.padding = p(4)
    view.showCropMarks = True
    view.showFrame = True
    view.showPadding = True # Show padding and margin on page
    view.showMargin = True

    page = doc[1] # Get the single page from te document.
    page.margin = page.bleed = MARGIN
    page.padding = PADDING

    # Add element without conditions. Hard positioning from bottom-left
    newRect(parent=page, x=60, y=60, fill=color(0.7, 0.7, 0.7, 0.3),
        w=150, h=200, showMargin=True, showPadding=True,
        margin=MARGIN, padding=PADDING)

    # Condition alignment takes the element margin into account.
    newRect(parent=page, fill=color(0.7, 0.7, 0.7, 0.3),
        w=150, h=200, showMargin=True, showPadding=True,
        margin=MARGIN, padding=PADDING,
        conditions=[Right2Right(), Top2Top()])

    page.solve()
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
