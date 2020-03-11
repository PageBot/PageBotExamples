#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     Images.py
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
from pagebot.contexts.base.babelstring import getFontPath
from pagebot import getResourcesPath

H, W = A3
W = pt(W)
H = pt(H)
M = 50

robotoRegular = findFont('Roboto-Regular')
pageBotBold = findFont('PageBot-Bold')
pageBotRegular = findFont('PageBot-Regular')
robotoBold = findFont('Roboto-Bold')
bungeeRegular = findFont('Bungee-Regular')
bungeeHairline = findFont('Bungee-HairlineRegular')
bungeeOutline = findFont('Bungee-OutlineRegular')

def test(context):
    print("creating doc")
    doc = Document(w=W, h=H, context=context)
    doc.name = 'TextBoxes-%s' % doc.context.name
    page = doc[1]
    print('# Testing images in %s' % doc)

    path = getResourcesPath() + 'cookbot10.jpg'
    newImage(path, z=0, w=100, parent=page, fill=0.7, padding=8,
            conditions=(Right2Right(), Float2Top()))

    print('Starting doc build')
    doc.build()

for contextName in ('DrawBot', 'Flat'):
    context = getContext(contextName)
    test(context)
