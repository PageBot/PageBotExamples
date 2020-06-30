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

from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt

# Document is the main instance holding all information about the document
# together (pages, styles, etc.)
from pagebot.document import Document
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.toolbox.color import Color
from pagebot import getContext


W, H = pt(500, 400)
RW = RH = pt(40)
PADDING = pt(28)
EXPORT_PATH = '_export/E06_AdvancedDocument-%s%s' # Template for export file formats.

def makeDocument(contextName):
    context = getContext(contextName)

    # Export in _export folder that does not commit in Git.
    # Force to export to a few file formats:
    exportPaths = (
        EXPORT_PATH % (context.name, '.pdf'),
        EXPORT_PATH % (context.name, '.jpg'),
        EXPORT_PATH % (context.name, '.png'),
        EXPORT_PATH % (context.name, '.svg')
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

if __name__ == '__main__':
    for contextName in ('DrawBot', 'Flat'):
        makeDocument(contextName)
