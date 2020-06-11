#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T  E X A M P L E S
#
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     Shapes.py
#
#     Tests pagebot text boxes.

from pagebot import getContext
from pagebot.conditions import *
from pagebot.document import Document
from pagebot.elements import *
from pagebot.fonttoolbox.objects.font import findFont, Font
from pagebot.toolbox.units import pt, upt
from pagebot.toolbox.color import noColor, color
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.constants import *
from pagebot.style import getRootStyle
from pagebot.filepaths import getResourcesPath

H, W = A3
W = pt(W)
H = pt(H)
M = 50

'''
robotoRegular = findFont('Roboto-Regular')
pageBotBold = findFont('PageBot-Bold')
pageBotRegular = findFont('PageBot-Regular')
robotoBold = findFont('Roboto-Bold')
bungeeRegular = findFont('Bungee-Regular')
bungeeHairline = findFont('Bungee-HairlineRegular')
bungeeOutline = findFont('Bungee-OutlineRegular')
'''

def test(context):
    print("creating doc")
    doc = Document(w=W, h=H, context=context)
    doc.name = 'Shapes-%s' % doc.context.name
    page = doc[1]
    print('# Testing shapes in %s' % doc)

    #path = '%s/shapes/%s' % (getResourcesPath(), 'cookbot10.jpg')
    #newImage(path, x=0, y=50, z=0, w=300, h=300, parent=page, padding=8, scaleImage=False)
    #newRect(x=0, y=50, z=0, w=500, h=500)
    #conditions=[Left2SideLeft(), Float2SideTop()])
    black = color(0)

    style = dict(fill=black)
    #coords = ((0, 0), (100, 100))
    newRect(x=0, y=0, w=100, h=100, parent=page, style=style)
    newCircle(x=200, y=100, r=100, parent=page, style=style)
    newOval(x=400, y=100, w=100, h=50, parent=page, style=style)
    coords = ((0, 0), (100, 100), (20, 200), (40, 500))
    #newPolygon(coords, parent=page, style=style)
    #newOval(

    print('Starting doc build')
    doc.build()
    EXPORT_PATH = '_export/Shapes-%s.pdf' % context.name
    doc.export(EXPORT_PATH)

#for contextName in ('Flat',):
for contextName in ('DrawBot', 'Flat'):
    context = getContext(contextName)
    test(context)
