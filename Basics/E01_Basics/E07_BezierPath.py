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
    H, W = A3
    doc = Document(w=W, h=H, context=context)
    page = doc[1]
    f = color(0.8)

    conditions = (Right2Right(), Float2Top(), Float2Left(), )
    options = dict(parent=page, fill=f, stroke=0, showOrigin=True, showDimensions=True,
            showElementInfo=True, showFlowConnections=True)
            #conditions=conditions)

    curve = newBezierCurve(x=0, y=0, **options)
    curve.beginPath('TestID')
    #curve.moveTo((0, 0))
    #curve.lineTo((0, 100))
    #curve.curveTo((50, 75), (60, 50), (50, 25), (0, 0))
    '''
    [(50.0, 50.0)]
    [(51.662919807002076, 62.82913526331253), (54.162919807002076, 63.07913526331254), (58.33333333333333, 50.833333333333336)]
    [(62.50374685966458, 38.587531403354134), (65.00374685966457, 38.83753140335414), (66.66666666666666, 51.66666666666667)]
    [(68.32958647366874, 64.4958019299792), (70.82958647366874, 64.74580192997921), (74.99999999999999, 52.50000000000001)]
    [(79.17041352633123, 40.254198070020806), (81.67041352633123, 40.50419807002081), (83.33333333333331, 53.33333333333334)]
    [(84.9962531403354, 66.16246859664588), (87.4962531403354, 66.41246859664588), (91.66666666666664, 54.16666666666668)]
    [(95.83708019299789, 41.92086473668748), (98.33708019299789, 42.170864736687484), (99.99999999999997, 55.000000000000014)]
    [(101.66291980700205, 67.82913526331254), (104.16291980700205, 68.07913526331255), (108.3333333333333, 55.83333333333335)]
    [(112.50374685966455, 43.58753140335415), (115.00374685966455, 43.837531403354156), (116.66666666666663, 56.666666666666686)]
    [(118.32958647366871, 69.49580192997922), (120.82958647366871, 69.74580192997922), (124.99999999999996, 57.50000000000002)]
    [(129.1704135263312, 45.25419807002082), (131.6704135263312, 45.50419807002083), (133.3333333333333, 58.33333333333336)]
    [(134.99625314033537, 71.16246859664588), (137.49625314033537, 71.4124685966459), (141.66666666666663, 59.16666666666669)]
    [(145.8370801929979, 46.92086473668749), (148.3370801929979, 47.1708647366875), (149.99999999999997, 60.00000000000003)]
    '''

    #curve.closePath()
    print(curve)
    # testing the "no on-curve point" scenario
    #curve.qCurveTo((0, 0), (0, 100), (100, 100), (100, 0), None)
    #curve.closePath()
    page.solve()
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
