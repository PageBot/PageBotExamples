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
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     03_Fonts.py
#
#     Shows how to get fonts.
#
from pagebot import *
from pagebot.constants import A3
from pagebot.document import Document
from pagebot.elements import *
from pagebot.toolbox.units import *
from pagebot.conditions import *
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.fonttoolbox.fontpaths import *
from pagebot.fonttoolbox.objects.family import getFamilyPaths

W, H = A3
MAX_PAGES = 20
P = pt(48)

def showAll():
    context = getContext('Flat')
    doc = Document(w=W, h=H, originTop=False, autoPages=1, context=context)
    page = doc[1]
    page.padding = P
    
    c1 = (Left2Left(), Fit2Right(), Float2Top()) # Group condition
    c2 = (Left2Left(), Float2Top()) # Title condition    
    c3 = (Right2Right(), Float2Top()) # Speciment condition

    families = getFamilyPaths()
    #print(families['Roboto'])
    fontPaths = getFontPaths()
    print('Number of fonts found: %d' % len(fontPaths))
    tfp = getTestFontsPath()
    pbFonts = getPageBotFontPaths()
    print('Number of fonts shipped with PageBot: %d' % len(pbFonts))
    #print(sorted(pbFonts.keys()))
    font = findFont('Roboto-Black')
    print('The Font object from the pagebot.fonttoolbox.objects module: %s' % font)
    print('Number of glyphs: %d' % len(font))
    i = 0

    for pbFont in sorted(pbFonts.keys()):
        if 'Bungee' in pbFont or 'PageBot' in pbFont: # Filter some of the PageBot fonts.
            f = findFont(pbFont)
            if f is not None:
                i += 1
                g = newGroup(parent=page, conditions=c1, padding=7, borderTop=1, strokeWidth=0)
                newText('%s\n' % pbFont, parent=g, conditions=c2, fontSize=16, strokeWidth=0)
                newText('ABCDEabcde012345', parent=g, conditions=c3, font=f, fontSize=pt(44), strokeWidth=0)
        if i > 10:
            page = page.next
            page.padding = P
            i = 0
                
    doc.solve()
    doc.export('_export/Fonts.pdf')

showAll()
