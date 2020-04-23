#!/usr/bin/evn python
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
#     FitRandomVariableGlyph.py
#
from pagebot.document import Document
from pagebot.elements import newText
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.fonttoolbox.variablefontbuilder import getVarFontInstance
from pagebot.conditions import *

# Export in _export folder that does not commit in Git. Force to export PDF.
EXPORT_PATH = '_export/FitRandomVariableGlyph.pdf'


def fit():
    varFont = findFont('RobotoDelta-VF')
    print(varFont.axes)
    condensedFont = getVarFontInstance(varFont, dict(wdth=75, YTUC=528))
    wideFont = getVarFontInstance(varFont, dict(wdth=125, YTUC=528))
    boldFont = getVarFontInstance(varFont, dict(wght=900, GRAD=1))

    W, H = 500, 500
    PADDING = 56
    COL = 40
    
    doc = Document(w=W, h=H)
    view = doc.view
    context = view.context

    page = doc[1] # Get page on pageNumber, first in row (this is only one now).
    page.padding = PADDING

    s = 'a'

    fontSize = 32

    for ix in range(10):
        for iy in range(10):

            instance = getVarFontInstance(varFont, dict(wdth=75, YTUC=528))
                
            style = dict(font=instance, fontSize=fontSize, leading=fontSize)
            bs = context.newString(s, style=style)
            tw, th = bs.size
            newText(bs, x=page.pl+ix*COL, y=page.pb+iy*COL, w=COL, h=COL, parent=page)

    doc.export(EXPORT_PATH)

fit()
