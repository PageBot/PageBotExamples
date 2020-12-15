#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#


# -----------------------------------------------------------------------------
#
#     E00_VariableElements.py
#

from pagebot import getContext
from pagebot.constants import EXPORT
from pagebot.conditions import *
from pagebot.document import Document
from pagebot.elements.variablefonts.variablecircle import VariableCircle
from pagebot.elements.variablefonts.variablecube import VariableCube
from pagebot.elements.variablefonts.variablescatter import VariableScatter
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.transformer import path2FileName

FILENAME = path2FileName(__file__)
W = H = 1000
vfFont = findFont('RobotoDelta_v2-VF')

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    doc = Document(w=W, h=H, context=context)
    page = doc[1]
    page.padding = 10
    conditions = (Right2Right(), Float2Top(), Float2Left())
    options = dict(parent=page, showOrigin=True, showDimensions=True,
            showElementInfo=True, showFlowConnections=True,
            conditions=conditions, stroke=0, strokeWidth=0.5, w=400, h=400)

    VariableCircle(vfFont, **options)
    VariableScatter(vfFont, **options)
    VariableCube(vfFont, **options)
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
