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
# -----------------------------------------------------------------------------
#
#     E07_Images.py
#
#     Tests pagebot text boxes.
#

from pagebot import getContext
from pagebot.conditions import *
from pagebot.constants import *
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.document import Document
from pagebot.elements import *
from pagebot.filepaths import getResourcesPath
from pagebot.fonttoolbox.objects.font import findFont, Font
from pagebot.style import getRootStyle
from pagebot.toolbox.units import pt, upt
from pagebot.toolbox.color import noColor, color
from pagebot.toolbox.transformer import path2FileName
W = pt(W)
H = pt(H)
M = 50
FILENAME = path2FileName(__file__)

robotoRegular = findFont('Roboto-Regular')
pageBotBold = findFont('PageBot-Bold')
pageBotRegular = findFont('PageBot-Regular')
robotoBold = findFont('Roboto-Bold')
bungeeRegular = findFont('Bungee-Regular')
bungeeHairline = findFont('Bungee-HairlineRegular')
bungeeOutline = findFont('Bungee-OutlineRegular')

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    doc = Document(w=W, h=H, context=context)
    page = doc[1]
    print('# Testing images in %s' % doc)
    path = '%s/images/%s' % (getResourcesPath(), 'cookbot10.jpg')
    newImage(path, x=0, y=50, z=0, w=300, h=300, parent=page, padding=8, scaleImage=False)
    #newRect(x=0, y=50, z=0, w=500, h=500)
    #conditions=[Left2SideLeft(), Float2SideTop()])
    doc.build()
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)

