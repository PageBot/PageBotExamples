#!/usr/bin/env python3
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
#     E23_BezierPaths.py
#

from pagebot import getContext
from pagebot.constants import EXPORT
from pagebot.toolbox.transformer import path2FileName

FILENAME = path2FileName(__file__)

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    doc = Document(title='Color Squares', w=W, h=H, context=context)
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
    doc.export(exportPath)


for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
