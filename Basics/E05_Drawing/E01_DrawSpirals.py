#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#    P A G E B O T  E X A M P L E S
#
#    www.pagebot.io
#    Licensed under MIT conditions
#
# -----------------------------------------------------------------------------
#
#    E01_DrawSpirals.py
#

from pagebot import getContext
from pagebot.constants import EXPORT
from pagebot.toolbox.color import noColor, blackColor
from pagebot.toolbox.transformer import path2FileName
from pagebot.toolbox.units import pt

X = 0
Y = 100
N = 8*8
Sx = 10
Sy = 10
Exy = 0.58
D = 0.5
FILENAME = path2FileName(__file__)

# Hardcoded constants.
W = H = 1000
M = 20
w = W - 2*M
h = H - 2*H

def drawSpiral(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    context.newPage(pt(W), pt(H))
    mx = W/2+X
    my = H/2+Y

    runs = False
    context.newPath()
    coords = (pt(mx), pt(my))
    context.moveTo(coords)
    s = '%s, %s' % coords
    context.text(s, coords)
    context.fill(noColor)
    context.stroke(blackColor)

    for n in range(0, int(N), 4):
        dx1 = n*Sx*D
        dy1 = n*Sy*D
        dx2 = (n+1)*Sx*D
        dy2 = (n+1)*Sy*D
        dx3 = (n+2)*Sx*D
        dy3 = (n+2)*Sy*D
        dx4 = (n+3)*Sx*D
        dy4 = (n+3)*Sy*D
        #dx5 = (n+4)*Sx*D
        #dy5 = (n+4)*Sy*D

        if not runs:
            context.moveTo((pt(mx), pt(my)))
        else:
            context.curveTo((pt(mx-dx1*Exy), pt(my-dy1)),
                (pt(mx-dx1), pt(my-dy1*Exy)), (pt(mx-dx1), pt(my)))
            context.curveTo((pt(mx-dx2), pt(my+dy2*Exy)),
                (pt(mx-dx2*Exy), pt(my+dy2)), (pt(mx), pt(my+dy2)))
            context.curveTo((pt(mx+dx3*Exy), pt(my+dy3)),
                (pt(mx+dx3), pt(my+dy3*Exy)), (pt(mx+dx3), pt(my)))
            context.curveTo((pt(mx+dx4), pt(my-dy4*Exy)), (pt(mx+dx4*Exy), pt(my-dy4)),
                (pt(mx), pt(my-dy4)))

        runs = True

    context.drawPath()
    context.saveImage(exportPath)

    '''
    FIXME: only works from inside DrawBot.
    #dict(name='ElementOrigin', ui='CheckBox', args=dict(value=False)),
    context.Variable(
      [dict(name='X', ui='Slider',
            args=dict(minValue=-W/2, value=0, maxValue=W/2)),
       dict(name='Y', ui='Slider',
            args=dict(minValue=-H/2, value=0, maxValue=H/2)),
       dict(name='N', ui='Slider',
            args=dict(minValue=8*2, value=8*8, maxValue=8*32)),
       dict(name='Sx', ui='Slider',
            args=dict(minValue=2, value=10, maxValue=40)),
       dict(name='Sy', ui='Slider',
            args=dict(minValue=2, value=10, maxValue=40)),
       dict(name='Exy', ui='Slider',
            args=dict(minValue=0.01, value=0.58, maxValue=1)),
       dict(name='D', ui='Slider',
            args=dict(minValue=0.1, value=0.5, maxValue=5))
      ], globals())
    '''

for contextName in ('DrawBot', 'Flat', 'Svg'):
    drawSpiral(contextName)
