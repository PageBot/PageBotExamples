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
#     GlyphPaths.py
#

import traceback
from random import random
from pagebot import getContext, getAllContexts, getResourcesPath
from pagebot.constants import A4Rounded
from pagebot.contexts.basecontext.babelstring import BabelString
from pagebot.document import Document
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.color import Color
from pagebot.toolbox.units import pt

H, W = A4Rounded
W = pt(W)
H = pt(H)

f = Color(0, 0, 0)
s = Color(1, 0, 0)

def testContexts():
    contexts = getAllContexts()

    for i, c in enumerate(contexts):
        if i in (0, 1):
            #print(c)
            try:
                testContext(c)
            except Exception as e:
                    print('Context errors', traceback.format_exc())

def getRandom():
    x = (W - 100) * random()
    y = (H - 100) * random()
    return x, y

def testContext(context):
    sq = 100
    x = 0
    y =  4*sq

    doc = Document(w=W, h=H, context=context, autoPages=1)
    context.frameDuration(1)
    context.newDrawing()
    context.newPage(w=W, h=H)
    context.fill(f)
    context.stroke(s)

    font = findFont('Roboto-Black')
    glyphName = 'Q'
    glyph = font[glyphName]
    context.translate(2*sq, sq)
    context.scale(0.1)
    context.drawGlyphPath(glyph)
    path = '_export/GlyphPaths-%s.pdf' % context.name
    context.saveImage(path)
    print('Saved %s' % path)

testContexts()
