#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E00_FontContent.py
#
#     Prints the values of the specified font for naming, info and features and
#     generate a simple 1000 x 1000 PDF, showing part of the glyph set.  This
#     is the simple demo version of the FontSpecimen.py that will generate a
#     full specimen of the font. It does not use Document and Element, drawing
#     directly using the context.

from pagebot import getContext
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.color import color, noColor
from pagebot.toolbox.units import pt


def draw(contextName):
    c = getContext(contextName)

    EXPORT_PATH = '_export/E00_FontContent-%s.pdf' % contextName

    L = 50
    W = H = 1000
    GX = GY = 11
    M = 50

    FONT_NAME = 'PageBot-Regular'
    #FONT_NAME = 'Amstelvar-Roman-VF'

    f = findFont(FONT_NAME) # Get PageBot Font instance of Variable font.

    if f is None:
        print('%s cannot be found' % FONT_NAME)
    else:
        # Names and text fields
        print('-- Names', '-'*L)
        print('Full name:', f.info.fullName)
        print('Family name:', f.info.familyName)
        print('Style name:', f.info.styleName)
        print('PS name:', f.info.psName)
        print('Designer:', f.info.designer)
        print('Description:', f.info.description)
        print('Trademark:', f.info.trademark)
        #(Metrics)
        print('-- Metrics', '-'*L)
        print('Ascender:', f.info.ascender)
        print('Typo Ascender:', f.info.typoAscender)
        print('capHeight:', f.info.capHeight)
        print('xHeight:', f.info.xHeight)
        print('Descender:', f.info.descender)
        print('Typo Descender:', f.info.typoDescender)
        print('Line gap:', f.info.lineGap)
        print('superscriptXSize:', f.info.superscriptXSize)
        print('OS/2 Width class:', f.info.widthClass)
        print('OS/2 Weight class:', f.info.weightClass)
        print('subscriptXOffset:', f.info.subscriptXOffset)
        print('strikeoutPosition:', f.info.strikeoutPosition)
        print('SubscriptXSize:', f.info.subscriptXSize)
        print('superscriptYOffset:', f.info.superscriptYOffset)
        print('strikeoutSize:', f.info.strikeoutSize)
        print('subscriptYSize:', f.info.subscriptYSize)
        print('superscriptYSize:', f.info.superscriptYSize)
        print('italicAngle:', f.info.italicAngle)
        print('unitsPerEm:', f.info.unitsPerEm)
        #(GPOS)
        print('-- GPOS', '-'*L)
        print('gposFeatures:', f.info.gposFeatures)
        #(GSUB)
        print('-- GSUB', '-'*L)
        print('gsubFeatures:', f.info.gsubFeatures)
        # Glyph content of the font
        print('-- Glyhps sorted by name', '-'*L)
        #print('Char set:', f.info.charSet)
        print('Glyph set:', f.info.glyphSet)

        glyphIndex = 1

        for yIndex in range(GY):
            for xIndex in range(GX):
                # Offset of drawing origin
                if glyphIndex > len(f.info.glyphSet):
                    break # Just do one page for sample demo.
                c.save()
                c.translate(M+(W-2*M)/GX*xIndex, H-M-(H-2*M)/GY*(yIndex+1))
                g = f[f.info.glyphSet[glyphIndex-1]]
                c.drawGlyph(g, x=0, y=0, fontSize=60, fill=color(0.1), stroke=noColor)
                glyphIndex += 1
                c.restore()

        c.saveImage(EXPORT_PATH)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
