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
#     NewDrawing.py
#
from pagebot import getContext

def test(context):
    context.newPage(200, 200)
    context.rect(0, 0, 100, 100)
    context.newPage(300, 300)
    context.newDrawing()
    context.newPage(400, 400)
    context.rect(100, 100, 40, 50)
    context.saveDrawing('_export/NewDrawing-%s.pdf' % context.name)

for contextName in ('DrawBot', 'Flat'):
#for contextName in ('Flat',):
#for contextName in ('DrawBot',):
    context = getContext(contextName)
    test(context)

