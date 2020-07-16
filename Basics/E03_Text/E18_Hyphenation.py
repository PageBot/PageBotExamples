#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2017 Thom Janssen <https://github.com/thomgb>
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E40_Hyphenation.py

from pagebot.document import Document
from pagebot import getContext
from pagebot.constants import EXPORT
from pagebot.elements import *
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.transformer import path2FileName

bungee = findFont('Bungee-Regular')
txt = Blurb().getBlurb('article_ankeiler', noTags=True)
FILENAME = path2FileName(__file__)
w = 400 # change width to see other hyphenations
h = 400
W = 1200
H = 1500

def makeText(contextName):
    context = getContext(contextName)

    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    doc = Document(w=W, h=H, autoPages=1, context=context)
    page = doc[1]

    fontSize = pt(32)

    # hyphenationHead=4, hyphenationTail=3 currently not supported
    style = dict(font=bungee, fontSize=fontSize, hyphenation=True)
    bs = context.newString(txt, style=style)
    newText(bs, x=100, y=H-h-100, w=w, h=h, parent=page, borders=1, fill=color(0.3, 0.2, 0.1, 0.5))
    print(bs.language, bs.hyphenation)

    #style['hyphenationTail'] = 400
    style = dict(font=bungee, fontSize=fontSize, hyphenation=False)
    bs = context.newString(txt, style=style)
    newText(bs, x=100, y=H-100-2*h, w=w, h=h, parent=page, borders=1, fill=color(1, 1, 0))
    print(bs.language, bs.hyphenation)

    #style['hyphenation'] = False
    style = dict(font=bungee, fontSize=fontSize, hyphenation=True)
    bs = context.newString(txt, style=style)
    newText(bs, x=100, y=H-100-3*h, w=w, h=h, parent=page, borders=1, fill=color(1, 0, 1))
    print(bs.language, bs.hyphenation)

    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    makeText(contextName)
