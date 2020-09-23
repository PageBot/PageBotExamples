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
#     E03_Fonts.py
#
#     Shows how to get fonts.
#
from pagebot import *
from pagebot.constants import A3, EXPORT
from pagebot.document import Document
from pagebot.elements import *
from pagebot.toolbox.units import *
from pagebot.conditions import *
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.fonttoolbox.fontpaths import *
from pagebot.fonttoolbox.objects.family import getFamilyPaths, findFamily, getFamily
from pagebot.toolbox.transformer import path2FileName
from pagebot.toolbox.loremipsum import  loremipsum

H, W = A3
H = pt(H)
W = pt(W)
MAX_PER_PAGE = 5
MAX_PAGES = 20
P = pt(48)
FILENAME = path2FileName(__file__)
LOREMIPSUM = loremipsum()

def verboseFam(fam):
    print(fam)
    if fam:
        stylesDict = fam.getStyles()
        for key, value in stylesDict.items():
            print(' - %s' % key)
            for v in value:
                print('   - %s' % v.path)

def draw(contextName):
    """Shows all fonts that are shipped with PageBot."""
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    doc = Document(w=W, h=H, autoPages=1, context=context)
    page = doc[1]
    page.padding = P

    c1 = (Left2Left(), Fit2Right(), Float2Top()) # Group condition
    c2 = (Left2Left(), Float2Top()) # Title condition
    c3 = (Right2Right(), Float2Top()) # Speciment condition

    families = getFamilyPaths()
    pbf = getPageBotFontPaths()

    fam = getFamily('Bungee')
    assert fam is not None
    #verboseFam(fam)

    fam = getFamily('PageBot')
    assert fam is not None
    #verboseFam(fam)

    fam = findFamily('Roboto')
    assert fam is not None
    #verboseFam(fam)

    #print('Number of families found: %d' % len(families))
    fontPaths = getFontPaths()
    #print('Number of fonts found: %d' % len(fontPaths))
    tfp = getTestFontsPath()
    pbFonts = getPageBotFontPaths()
    #print('Number of fonts shipped with PageBot: %d' % len(pbFonts))
    font = findFont('Roboto-Black')
    #print('The Font object from the pagebot.fonttoolbox.objects module: %s' % font)
    #print('It has %d glyphs.' % len(font))
    i = 0
    boxHeight = 150

    x1 = (W - 2*P) / 4
    w0 = (W - 2*P) / 4
    w1 = (W - 2*P) / 4 * 3

    for pbFont in sorted(pbFonts.keys()):
        f = findFont(pbFont)
        if f is not None and not f.name.startswith('Amstel'):
            i += 1
            g = newGroup(parent=page, conditions=c1, showFrame=True, strokeWidth=1, stroke=(0, 1, 0), w=W, h=pt(boxHeight))
            newText('%s\n' % pbFont, parent=g, conditions=c2, fontSize=16, border=1, stroke=(1, 0, 0), strokeWidth=1, fill=(0, 1, 0), w=pt(w0), h=pt(boxHeight))
            t = newText(LOREMIPSUM, parent=g, conditions=c3, font=f, fontSize=pt(48), stroke=(0, 0, 1), strokeWidth=1, w=pt(w1), h=pt(boxHeight), x=pt(x1))
        if i == MAX_PER_PAGE:
            page = page.next
            page.padding = P
            i = 0

    doc.solve()
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
