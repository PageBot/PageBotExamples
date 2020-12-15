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
#     E03_ElementPaddingPositions.py
#
#     Position elements by their sides
#
#      Document is the main instance holding all information about the document
#      togethers (pages, styles, etc.)
#

from pagebot import getContext
from pagebot.constants import EXPORT
from pagebot.conditions import *
from pagebot.document import Document
from pagebot.elements import newRect
from pagebot.toolbox.units import p
from pagebot.toolbox.color import color
from pagebot.toolbox.transformer import path2FileName

W = H = 500
PADDING = p(5)
FILENAME = path2FileName(__file__)

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    doc = Document(w=W, h=H, context=context)
    page = doc[1] # Get the single page from te document.
    page.padding = PADDING
    page.showPadding = True

    e = newRect(parent=page, fill=color('red'))
    e.left = page.pl
    e.bottom = page.pb

    e = newRect(parent=page, fill=color('green'))
    e.top = page.h - page.pt
    e.center = page.w/2

    e = newRect(parent=page, fill=color('blue'))
    e.top = page.h - page.pt
    e.right = page.w - page.pr

    e = newRect(parent=page, fill=color('orange'))
    e.left = page.pl
    e.middle = page.h/2

    e = newRect(parent=page, fill=color('yellow'))
    e.left = page.pl
    e.top = page.h - page.pt

    e = newRect(parent=page, fill=color('purple'))
    e.bottom = page.pb
    e.right = page.w - page.pr

    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)

