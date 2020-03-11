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
    doc.name = 'Images-%s' % doc.context.name
    page = doc[1]
    print('# Testing images in %s' % doc)

    path = '%s/images/%s' % (getResourcesPath(), 'cookbot10.jpg')
    newImage(path, x=0, y=50, z=0, w=500, h=500, parent=page, fill=0.7, padding=8, scaleImage=False)
            #conditions=[Left2SideLeft(), Float2SideTop()])

    print('Starting doc build')
    doc.build()
    EXPORT_PATH = '_export/Images-%s.pdf' % context.name
    doc.export(EXPORT_PATH)

for contextName in ('DrawBot', 'Flat'):
    context = getContext(contextName)
    test(context)
