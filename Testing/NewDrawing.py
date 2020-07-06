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
#     Supporting DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     NewDrawing.py
#
from pagebot import getContext

W = 300
H = 400

def test(context):
    context.newPage(W, H)
    context.rect(0, 0, 100, 100)
    context.saveDrawing('_export/NewDrawing1-%s.pdf' % context.name)
    context.newDrawing(w=W, h=H)
    context.newPage(W, H)
    context.rect(100, 100, 40, 50)
    context.saveDrawing('_export/NewDrawing2-%s.pdf' % context.name)

for contextName in ('DrawBot', 'Flat'):
#for contextName in ('Flat',):
#for contextName in ('DrawBot',):
    context = getContext(contextName)
    test(context)

