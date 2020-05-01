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
#     E30_GlyphAnalyzer.py
#
#     Implements a PageBot font classes to get info from a TTFont.
#     Show the values that the GlyphAnalyzer get derive from font and glyph outline.
#
#	  The GlyphAnalyzer tries to collect structure from a glyph, that it not
#     readily available in the font.info, such as stem widths, bars and diagonals.
#     The analyzer can be compared with “auto-hinters” that try to figure out
#     the same kind of information from an outline.
#   
from pagebot.fonttoolbox.objects.font import findFont
from pagebot import getContext

GLYPH_NAME = 'B'

context = getContext()
font = findFont('Georgia')
print(font.analyzer) 
print(font.analyzer.name) 
glyph = font[GLYPH_NAME]
ga = glyph.analyzer
print(ga)
print('Glyph horizontals width:', ga.width, ga.glyph.width, glyph.width)
print('Glyph bounding box:', ga.boundingBox)
# X position of vertical lines also includes sides of serifs.
print('x-position of verticals:', sorted(ga.verticals.keys()))
# Y position of horizontal lines
print('y-position of horizontals:', sorted(ga.horizontals.keys()))
print(ga.stems)
