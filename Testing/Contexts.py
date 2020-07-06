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
#     Contexts.py
#

import traceback
from random import random
from pagebot import getAllContexts
from pagebot.filepaths import getResourcesPath
from pagebot.toolbox.color import Color
from pagebot.constants import A4Rounded
from pagebot.contexts.basecontext.babelstring import BabelString
from pagebot import getContext
from pagebot.toolbox.units import pt
from pagebot.document import Document
from pagebot.fonttoolbox.objects.font import findFont
H, W = A4Rounded
W = pt(W)
H = pt(H)

f = Color(0, 0, 0)
s = Color(1, 0, 0)

def testContexts():
    contexts = getAllContexts()
    print('All contexts: %s' % contexts)

    for i, c in enumerate(contexts):
        if i in (0, 1):
            #print(c)
            try:
                testContext(c)
            except Exception as e:
                    print('Context errors', traceback.format_exc())

def printAttributes(doc, context):
    print('# Context attributes')

    for key, value in context.__dict__.items():
        print(' * %s: %s' % (key, value))

    print('# Document attributes')
    for key, value in doc.__dict__.items():
        print(' * %s: %s' % (key, value))


def testContext(context):
    # TODO:
    # - test elements
    # - test shadow, gradient,
    # ...

    sq = 100
    x = 0
    y = 0
    print('Context', context)
    doc = Document(w=W, h=H, context=context, autoPages=1)
    context.frameDuration(1)
    context.newDrawing()
    context.newPage(w=W, h=H)

    context.text('default size string without style', pt(x, y))
    y += sq

    context.fontSize(sq)
    context.text('%spt size string without style' % sq, pt(x, y))
    y += sq

    bs = context.newString('BabelString No Style')

    print(bs.style)
    #print(bs.style.get('font'))
    #print(bs.style.get('fontSize'))
    #print(bs.style.get('fallbackFont'))
    context.strokeWidth(1)

    w0, h0 = context.textSize(bs)
    context.text(bs, pt(x, y))
    print('String size is %dx%d' % (w0, h0))
    y += sq

    fontName = 'Roboto-Black'
    font = findFont(fontName)
    style = {'font': font.path, 'textFill': f}
    bs = context.newString('Babel String with Style', style=style)

    print(bs.style)
    #print(bs.style.get('font'))
    #print(bs.style.get('fallbackFont'))
    context.text(bs, pt(x, y))
    w0, h0 = context.textSize(bs)
    print('String size is %dx%d' % (w0, h0))

    x = 2 * sq
    y = 0

    path = getResourcesPath() + "/images/cookbot1.jpg"
    # Sloooow.
    #context.image(path, p=pt(x, y), w=pt(100), h=pt(100))

    y += sq

    context.fill(f)
    context.stroke(s)
    context.rect(x, y, pt(sq), pt(sq))
    y += sq

    context.circle(x+0.5*sq, y+0.5*sq, 0.5*pt(sq))
    y += sq

    context.oval(x, y, pt(sq), 0.5*pt(sq))
    y += sq

    glyphName = 'Q'
    glyph = font[glyphName]
    context.translate(2*sq, sq)
    context.scale(0.1)
    context.drawGlyphPath(glyph)

    path = '_export/%s-%s.pdf' % ('Contexts', context.name)
    context.saveImage(path)
    print('Saved %s' % path)

testContexts()
