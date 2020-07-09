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
#     E06_AdvancedDocument.py
#
#     Shows how to start a document and export it to PNG and
#     PDF in the simplest steps.
#
#     TODO: Floating on second line does not seem to work currently
from pagebot import getContext
from pagebot.constants import EXPORT
from pagebot.document import Document
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.toolbox.color import Color
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt
from pagebot.toolbox.transformer import path2FileName

W, H = pt(500, 400)
RW = RH = pt(40)
PADDING = pt(28)
FILENAME = path2FileName(__file__)

def draw(contextName):
    context = getContext(contextName)

    # Export in _export folder that does not commit in Git.
    # Force to export to a few file formats:
    exportPaths = (
        '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName),
        '%s/%s-%s.jpg' % (EXPORT, FILENAME, contextName),
        '%s/%s-%s.png' % (EXPORT, FILENAME, contextName),
        '%s/%s-%s.svg' % (EXPORT, FILENAME, contextName),
    )
    # Creates the publication/document that holds the pages.
    doc = Document(w=W, h=H, context=context)

    # Gets page by pageNumber, first in row (at this point there is only one in
    # this row).
    page = doc[1]
    page.padding = PADDING
    page.showPadding = True

    conditions = [Right2Right(), Float2Top(), Float2Left()]
    # TODO: Solve this bug, does not mirror.
    conditions = (
        Left2Left(),
        Float2Top(),
        Float2Right()
    )
    numberOfSquares = 88
    ratio = 1 / numberOfSquares

    for n in range(numberOfSquares):
        newRect(w=RW, h=RH, parent=page,
                fill=color(1 - n*ratio, 0, 0.5),
                conditions=conditions, margin=0)

    # Recursively solve the conditions in all page child elements..
    # If there are failing conditions, then the status
    # is returned in the Score instance.
    score = doc.solve()
    # Export to various export formats
    for exportPath in exportPaths:
        doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
