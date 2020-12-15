#!/usr/bin/env python3 # -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#


# -----------------------------------------------------------------------------
#
#     E06_FontContent.py
#
#     Prints the values of the specified font for naming, info and features and
#     generate a simple 1000 x 1000 PDF, showing part of the glyph set.  This
#     is the simple demo version of the FontSpecimen.py that will generate a
#     full specimen of the font. It does not use Document and Element, drawing
#     directly using the context.

from pagebot import getContext
from pagebot.constants import EXPORT
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.color import color, noColor
from pagebot.toolbox.units import pt
from pagebot.toolbox.transformer import path2FileName

L = 50
W = H = 1000
GX = 11
GY = 11
M = 50
FONT_NAME = 'PageBot-Regular'
FILENAME = path2FileName(__file__)

def draw(contextName, verbose=False):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    f = findFont(FONT_NAME) # Get PageBot Font instance.

    if f is None:
        print('%s cannot be found' % FONT_NAME)
        return

    c = getContext(contextName)
    c.newDrawing(w=W, h=H)

    if verbose:
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

    c.stroke((0, 1, 0))
    c.strokeWidth(0.5)
    c.line((M, 0), (M, H))
    c.line((W-M, 0), (W-M, H))
    c.line((0, M), (W, M))
    c.line((0, H-M), (W, H-M))

    for yIndex in range(GY):
        for xIndex in range(GX):
            # Offset of drawing origin.
            if glyphIndex > len(f.info.glyphSet):
                break # Just do one page for sample demo.
            w = W - 2*M
            x = M + w / GX * xIndex
            h = H - 2*M
            y = M + h / GY * (yIndex + 1)
            c.marker(x, y)
            glyphName = f.info.glyphSet[glyphIndex-1]
            g = f[glyphName]
            c.drawGlyph(g, x=x, y=y, fontSize=60, fill=color(0.1), stroke=noColor)
            glyphIndex += 1

    c.saveImage(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
