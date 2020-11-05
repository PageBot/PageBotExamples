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
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E00_VariableCircle.py
#

from pagebot import getContext
from pagebot.constants import EXPORT
from pagebot.document import Document
from pagebot.elements.variablefonts.variablecircle import VariableCircle
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.transformer import path2FileName

FILENAME = path2FileName(__file__)
W = H = 500
vfFont = findFont('RobotoDelta_v2-VF')

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    doc = Document(w=W, h=H, context=context)
    page = doc[1]
    page.padding = 40
    vc = VariableCircle(vfFont, parent=page, x=40, y=40, w=page.pw)
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
