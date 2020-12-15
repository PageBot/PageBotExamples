#!/usr/bin/evn python
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#

#     www.pagebot.io
#     Licensed under MIT conditions
#


# -----------------------------------------------------------------------------
#
#     FittingTextWidth.py
#
from pagebot.document import Document
from pagebot.elements import newText
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.fonttoolbox.variablefontbuilder import getVarFontInstance
from pagebot.conditions import *

# Export in _export folder that does not commit in Git. Force to export PDF.
EXPORT_PATH = '_export/UseFittingTextWidth.pdf'


def fit():
    varFont = findFont('RobotoDelta-VF')
    print(varFont.axes)
    condensedFont = getVarFontInstance(varFont, dict(wdth=75, YTUC=528))
    wideFont = getVarFontInstance(varFont, dict(wdth=125, YTUC=528))
    boldFont = getVarFontInstance(varFont, dict(wght=900, GRAD=1))

    W, H = 500, 400
    PADDING = 8

    doc = Document(w=W, h=H)
    view = doc.view
    context = view.context

    page = doc[1] # Get page on pageNumber, first in row (this is only one now).
    page.padding = PADDING

    s = 'Variable'

    labelStyle = dict(font=varFont.path, fontSize=8, textFill=(1, 0, 0),
        leading=8)

    conditions1 = [Left2Left(), Top2Top()]
    conditions2 = [Left2Left(), Float2Top()]
    
    fontSize = 80
    style = dict(font=varFont.path, fontSize=fontSize, leading=fontSize)
    bs = context.newString(s, style=style)
    tw, th = bs.size
    newText(bs, w=W-2*PADDING, h=th*1.2, parent=page,
        conditions=conditions1)
    labelS = context.newString('Original var-font %0.2fpt' % (bs.fontSize), style=labelStyle)
    newText(labelS, parent=page,
        conditions=conditions2)

    style = dict(font=condensedFont.path, fontSize=fontSize, leading=fontSize)
    bs = context.newString(s, style=style)
    tw, th = bs.size
    newText(bs, w=W-2*PADDING, h=th*1.2, parent=page, conditions=conditions2)
    labelS = context.newString('Wide %0.2fpt %s' % (bs.fontSize, wideFont.info.location), style=labelStyle)
    newText(labelS, parent=page, conditions=conditions2)

    style = dict(font=wideFont.path, fontSize=fontSize, leading=fontSize)
    bs = context.newString(s, style=style)
    tw, th = bs.size
    newText(bs, w=W-2*PADDING, h=th*1.2, parent=page, conditions=conditions2)
    labelS = context.newString('Wide %0.2fpt %s' % (bs.fontSize, wideFont.info.location), style=labelStyle)
    newText(labelS, parent=page, conditions=conditions2)

    style = dict(font=boldFont.path, fontSize=fontSize, leading=fontSize)
    bs = context.newString(s, style=style)
    tw, th = bs.size
    newText(bs, w=W-2*PADDING, h=th*1.2, parent=page, 
        conditions=conditions2)
    labelS = context.newString('Bold %0.2fpt %s' % (bs.fontSize, boldFont.info.location), style=labelStyle)
    newText(labelS, parent=page, conditions=conditions2)
    
    page.solve()
    doc.export(EXPORT_PATH)

fit()
