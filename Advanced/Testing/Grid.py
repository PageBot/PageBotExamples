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
#     Grid.py
#

from pagebot import getContext
from pagebot.document import Document
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.toolbox.units import pt, mm
from pagebot.toolbox.color import color, Color
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.style import getRootStyle

W = pt(300)
H = pt(300)

GRIDX = []
GRIDY = []

for i in range(1, 24):
    GRIDX.append((pt(10)))

for i in range(1, 24):
    GRIDY.append((pt(10)))

for contextName in ['DrawBot', 'Flat']:
    context = getContext(contextName)
    doc = Document(w=W, h=H, context=context, originTop=True)
    doc.name = 'Grid-%s'  % contextName
    doc.gridX = GRIDX
    doc.gridY = GRIDY
    print(' * %s' % doc.name)
    doc.view.showGrid = True
    #doc.view.showFrame = True
    doc.view.showPadding = True
    #doc.view.showMargin = True
    doc.view.showNameInfo = True
    doc.view.showOrigin = True
    doc.view.showDimensions = True
    doc.view.showRegistrationMarks = True
    #style = getRootStyle()
    #page = doc[1]
    #print(doc.view.padding)
    #print(doc.view.margin)
    doc.solve()
    doc.build()

    
