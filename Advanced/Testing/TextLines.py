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
#     TextLines.py
#

from pagebot import getContext
from pagebot.contributions.filibuster.blurb import Blurb

H = 850
W = 652

blurb = Blurb()
context = getContext('DrawBot')
context.newDrawing()
context.newPage(W, H)

b = blurb.getBlurb('stylewars_documentary')
s = context.newString(b)
lines = s.getTextLines(w=100)
for line in lines:
    for run in line.textRuns:
        print(run)

context.text(s, (0, 0))

path = '_export/TextLines-%s.pdf' % context.name
context.saveImage(path)
