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

W = 300
H = 300

GRIDX = []
GRIDY = []

SQ = 10

for i in range(1, int(W / SQ) + 1):
    GRIDX.append((pt(SQ)))

for i in range(1, int(H / SQ) + 1):
    GRIDY.append((pt(SQ)))

for contextName in ['DrawBot', 'Flat']:
    context = getContext(contextName)
    doc = Document(w=W, h=H, padding=30, context=context, originTop=False)
    doc.name = 'Grid-%s'  % contextName
    page = doc[1]
    page.padding = (SQ, SQ, SQ, SQ)
    doc.gridX = GRIDX
    doc.gridY = GRIDY
    print(' * %s' % doc.name)
    doc.view.showGrid = True
    doc.view.showOrigin = True
    doc.view.showDimensions = True
    doc.view.showNameInfo = True
    #doc.view.showColorBars = True
    #doc.view.showFrame = True
    #doc.view.showPadding = True
    #doc.view.showMargin = True
    #doc.view.showRegistrationMarks = True
    #style = getRootStyle()
    #print(doc.view.padding)
    #print(doc.view.margin)
    #print(page.view.padding)
    print(doc.view.padding)
    doc.solve()
    doc.build()

    
