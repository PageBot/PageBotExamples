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
#     E06_BasicElements.py
#
#     Test handling of pages in a document.
#

from pagebot.contexts import getContext
from pagebot.document import Document
from pagebot.elements import *
from pagebot.filepaths import getResourcesPath
from pagebot.fonttoolbox.fontpaths import getTestFontsPath
from pagebot.fonttoolbox.objects.font import Font
from pagebot.conditions import *
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt, mm
from pagebot.constants import CENTER, LEFT, EXPORT
from pagebot.toolbox.transformer import path2FileName
from pagebot.toolbox.loremipsum import  loremIpsum

# Template for the export path, allowing to include context name.
W, H = pt(800), pt(600)
FILENAME = path2FileName(__file__)
fontName = 'PageBot-Regular'
SQ = 50
"""Types of elements: rectangle, circle, text, polygon, curve, glyph."""
N = 6
F = 1.0 / N

def getColor(i):
    r = F
    g = 1
    b = F/2
    f = (i*r, i*g, i*b)
    return f

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

    # TODO: findFont instead.
    fontPath = getTestFontsPath() + '/google/roboto/Roboto-Medium.ttf'
    font = Font(fontPath)

    '''Positions the elements to the top left of the page area. Notice that the
    (x, y) position is undefined, default is (0, 0), since it will be
    determined by the condition. Size measures can be any type of units. Their
    type is shown in the measured output.'''
    conditions = (Right2Right(), Float2Top(), Float2Left(), )

    options = dict(parent=page, showOrigin=True, showDimensions=True,
            showElementInfo=True, showFlowConnections=True,
            conditions=conditions, stroke=0, strokeWidth=0.5)

    newRect(name='rect', r=SQ, fill=getColor(1), **options)
    newText(bs, name='text', w=2*SQ, h=2*SQ, fill=getColor(2), **options)
    newCircle(name='circle', r=SQ, fill=getColor(3), **options)
    points = [(0, 0), (20, 100), (40, 0), (60, 100), (80, 0), (100, 100)]
    newPolygon(name='polygon', points=points, fill=getColor(4), **options)

    # Bézier curve points.
    points = [(0, 0),
        ((-6.722045442950497, 11.097045442950499), (-4.847045442950498,
            12.972045442950499), (6.250000000000001, 6.25)),
        ((17.3470454429505, -0.4720454429504981), (19.222045442950503,
            1.402954557049501), (12.500000000000002, 12.5)),
        ((5.777954557049505, 23.5970454429505), (7.652954557049505,
            25.4720454429505), (18.750000000000004, 18.75)),
        ((29.847045442950503, 12.027954557049501), (31.722045442950503,
            13.902954557049501), (25.000000000000004, 25.0)),
        ((18.277954557049505, 36.0970454429505), (20.152954557049505,
            37.9720454429505), (31.250000000000004, 31.25)),
        ((42.3470454429505, 24.5279545570495), (44.22204544295051,
            26.4029545570495), (37.50000000000001, 37.5)),
        ((30.77795455704951, 48.5970454429505), (32.65295455704951,
            50.4720454429505), (43.75000000000001, 43.75)),
        ((54.8470454429505, 37.027954557049505), (56.72204544295051,
            38.9029545570495), (50.00000000000001, 50.0)),
        ((43.27795455704951, 61.0970454429505), (45.15295455704951,
            62.9720454429505), (56.25000000000001, 56.25)),
        ((67.3470454429505, 49.527954557049505), (69.2220454429505,
            51.4029545570495), (62.50000000000001, 62.5)),
        ((55.77795455704951, 73.5970454429505), (57.65295455704951,
            75.4720454429505), (68.75000000000001, 68.75)),
        ((79.84704544295052, 62.027954557049505), (81.72204544295052,
            63.9029545570495), (75.00000000000001, 75.0)),
        ((68.27795455704951, 86.0970454429505), (70.15295455704951,
            87.9720454429505), (81.25000000000001, 81.25)),
        ((92.34704544295052, 74.5279545570495), (94.22204544295052,
            76.4029545570495), (87.50000000000001, 87.5)),
        ((80.77795455704951, 98.5970454429505), (82.65295455704951,
            100.4720454429505), (93.75000000000001, 93.75)),
        ((104.84704544295052, 87.0279545570495), (106.72204544295052,
            88.9029545570495), (100.00000000000001, 100.0)),
     ]

    newBezierCurve(closed=False, points=points, fill=getColor(5), **options)
    newGlyphPath(font['Q'], fill=getColor(6), **options)

    path = getResourcesPath() + "/images/cookbot1.jpg"
    im = newImage(path, **options)
    print(im.x, im.y, im.w, im.h)

    # Sets alignmetns and saves the results as a PDF.
    page.solve()
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
