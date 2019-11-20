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
from pagebot.toolbox.units import pt
from pagebot.toolbox.color import color, Color
from pagebot.fonttoolbox.objects.font import findFont

W = 300
H = 300

for contextName in ['DrawBot', 'Flat']:
    context = getContext(contextName)
    doc = Document(w=W, h=H, context=context, originTop=True)
    doc.name = 'Grid-%s'  % contextName
    print(' * %s' % doc.name)
    doc.view.showGrid = True
    doc.view.showFrame = True
    doc.view.showPadding = True
    doc.view.showNameInfo = True
    doc.view.showOrigin = True
    doc.view.showDimensions = True
    page = doc[1]
    #context.newDrawing()
    #context.newPage(W, H)
    #path = '_export/Grid-%s.pdf' % context.name
    #context.saveImage(path)
    print(doc._originTop)
    doc.solve()
    doc.build()

    
