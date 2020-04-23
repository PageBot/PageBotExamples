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
#     TODO: Floating on second line does not seem to work currently

from pagebot.toolbox.color import color
from pagebot import getContext

EXPORT_PATH = '_export/Start'

# Export in _export folder that does not commit in Git.
# Force to export to a few file formats:
EXPORT_PATH_PDF = EXPORT_PATH + '.pdf'
EXPORT_PATH_JPG = EXPORT_PATH + '.jpg'
EXPORT_PATH_PNG = EXPORT_PATH + '.png'
EXPORT_PATH_SVG = EXPORT_PATH + '.svg'

# Document is the main instance holding all information about the document
# together (pages, styles, etc.)
from pagebot.document import Document
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.toolbox.color import Color

W, H = 500, 400

def makeDocument():
    # Creates the publication/document that holds the pages.
    doc = Document(w=W, h=H, autoPages=1)
    print(doc.view)
    print(doc.pages)

    doc.view.padding = 0 # Don't show cropmarks in this example.
    #doc.margin =
    doc.view.showPadding = True

    c1 = [Right2Right(), Float2Top(), Float2Left()]
    c2 = [Right2Right(), Float2Top()]
    c3 = [Left2Left()]
    c4 = [Left2Left(), Float2TopLeft()]
    c5 = [Right2Right(), Float2TopLeft()]
    c6 = [Left2Left(), Float2TopRight()]

    conditions = [c1]#, c2]#, c3, c4, c5, c6]
    page = doc[1]

    for c in conditions:
        makePage(doc, page, c)
        #page = page.next

    testCoordinates()


rectSets = []

def makePage(doc, page, conditions):

    # Gets page by pageNumber, first in row (at this point there is only one in
    # this row).

    page.padding = 1
    page.showPadding = True
    numberOfSquares = 8
    ratio = 1 / numberOfSquares
    rects = []

    for n in range(numberOfSquares):
        r = newRect(w=40, h=42, mr=4, mt=4, parent=page,
                fill=color(1 - n*ratio, 0, 0.5),
                conditions=conditions, margin=0)
        rects.append(r)
    rectSets.append(rects)

    score = doc.solve()
    doc.build()

def testCoordinates():
    context = getContext()
    context.fill((0, 1, 0))
    context.stroke(None)

    for rects in rectSets:
        i = 0
        for r in rects:
            i +=1
            x = r.getFloatSideLeft()
            y = r.getFloatSideTop()
            #print('%d %d' % (x, y))
            context.circle(x, y, 2)
            context.text('%d' % i, (x + 5, y - 5))

makeDocument()
