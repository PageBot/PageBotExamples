#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E07_BezierPath.py
#
#     Draw a string outline as PageBotPath.
#
from pagebot import getContext
from pagebot.conditions import *
from pagebot.constants import A3, EXPORT
from pagebot.toolbox.color import color
from pagebot.document import Document
from pagebot.elements import *
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.units import pt
from pagebot.toolbox.transformer import path2FileName

FILENAME = path2FileName(__file__)

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    H, W = 400, 400
    doc = Document(w=W, h=H, context=context)
    page = doc[1]

    conditions = (Right2Right(), Float2Top(), Float2Left(), )
    options = dict(parent=page, stroke=0, strokeWidth=0.5, showOrigin=True, showDimensions=True,
            showElementInfo=True, showFlowConnections=True,
            conditions=conditions)

    points = [(0, 0),
        ((-6.722045442950497, 11.097045442950499), (-4.847045442950498, 12.972045442950499), (6.250000000000001, 6.25)),
        ((17.3470454429505, -0.4720454429504981), (19.222045442950503, 1.402954557049501), (12.500000000000002, 12.5)),
        ((5.777954557049505, 23.5970454429505), (7.652954557049505, 25.4720454429505), (18.750000000000004, 18.75)),
        ((29.847045442950503, 12.027954557049501), (31.722045442950503, 13.902954557049501), (25.000000000000004, 25.0)),
        ((18.277954557049505, 36.0970454429505), (20.152954557049505, 37.9720454429505), (31.250000000000004, 31.25)),
        ((42.3470454429505, 24.5279545570495), (44.22204544295051, 26.4029545570495), (37.50000000000001, 37.5)),
        ((30.77795455704951, 48.5970454429505), (32.65295455704951, 50.4720454429505), (43.75000000000001, 43.75)),
        ((54.8470454429505, 37.027954557049505), (56.72204544295051, 38.9029545570495), (50.00000000000001, 50.0)),
        ((43.27795455704951, 61.0970454429505), (45.15295455704951, 62.9720454429505), (56.25000000000001, 56.25)),
        ((67.3470454429505, 49.527954557049505), (69.2220454429505, 51.4029545570495), (62.50000000000001, 62.5)),
        ((55.77795455704951, 73.5970454429505), (57.65295455704951, 75.4720454429505), (68.75000000000001, 68.75)),
        ((79.84704544295052, 62.027954557049505), (81.72204544295052, 63.9029545570495), (75.00000000000001, 75.0)),
        ((68.27795455704951, 86.0970454429505), (70.15295455704951, 87.9720454429505), (81.25000000000001, 81.25)),
        ((92.34704544295052, 74.5279545570495), (94.22204544295052, 76.4029545570495), (87.50000000000001, 87.5)),
        ((80.77795455704951, 98.5970454429505), (82.65295455704951, 100.4720454429505), (93.75000000000001, 93.75)),
        ((104.84704544295052, 87.0279545570495), (106.72204544295052, 88.9029545570495), (100.00000000000001, 100.0)),
    ]

    curve = newBezierCurve(x=0, y=0, closed=False, points=points, **options)
    page.solve()
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
