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
#     07_BezierPath.py
#
#     Draw a string outline as PageBotPath.
#
from pagebot.toolbox.units import pt
from pagebot import getContext
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.document import Document
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.constants import A3

def makeDocument(context):
    H, W = A3
    doc = Document(w=W, h=H, context=context)
    page = doc[1]
    style = {}
    style['fill'] = (1, 0, 0)
    style['stroke'] = (0, 0, 0)
    style['strokeWidth'] = 5
    path = newBezierPath(context=context, style=style)
    path.beginPath('TestID')
    path.moveTo((0, 0))
    path.lineTo((0, 100))
    path.curveTo((50, 75), (60, 50), (50, 25), (0, 0))
    path.closePath()
    print(path)

    # testing the "no on-curve point" scenario
    #path.qCurveTo((0, 0), (0, 100), (100, 100), (100, 0), None)
    #path.closePath()


    #bungee = findFont('BungeeOutline-Regular')
    #c = (Right2Right(), Top2Top(), Float2Left())
    #t = newText('*PageBot Path*', parent=page, conditions=c, style={'fill': 1, 'fontSize': 32, 'stroke': 0, 'strokeWidth': 2})
    #path.text('ABC', style=dict(font=bungee, fontSize=pt(120)))
    #newPaths(path, parent=page, fill=(1, 0, 0), conditions=c)
    #roboto = findFont('Roboto-Bold')
    #path = BezierPath(context=context)
    # FIXME: y-translation always same direction?
    #path.translate((-60, 200))
    #path.text('CDE', style=dict(font=roboto, fontSize=pt(240)))
    #path = path.removeOverlap()
    #newPaths(path, parent=page, fill=(1, 1, 0), stroke=0, conditions=c)

    page.solve()
    doc.export('_export/07_BezierPath-%s.pdf' % context.name)

if __name__ == '__main__':
    from pagebot import getContext

    for contextName in ('DrawBot', 'Flat'):
        context = getContext(contextName)
        makeDocument(context)

