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
# -----------------------------------------------------------------------------
#
#     TextBoxes.py
#
#     Tests pagebot text boxes.

from pagebot import getContext
from pagebot.document import Document
from pagebot.elements import *
from pagebot.fonttoolbox.objects.font import findFont, Font
from pagebot.toolbox.units import pt, upt
from pagebot.toolbox.color import noColor, color
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.constants import *
from pagebot.style import getRootStyle
from pagebot.contexts.base.babelstring import getFontPath

# TODO: move to basics when finished.

H, W = A3
W = pt(W)
H = pt(H)
M = 50 

robotoRegular = findFont('Roboto-Regular')
pageBotBold = findFont('PageBot-Bold')
pageBotRegular = findFont('PageBot-Regular')
robotoBold = findFont('Roboto-Bold')
bungeeRegular = findFont('Bungee-Regular')
bungeeHairline = findFont('Bungee-HairlineRegular')
bungeeOutline = findFont('Bungee-OutlineRegular')

def drawBaselines(x0, y0, w, baselines, lineHeight, descender, page):
    baseH0 = 0

    for i, baseline in enumerate(baselines):
        y = y0 - baseline
        baseH = baseline - baseH0
        baseH0 = baseline
        newLine(x=x0, y=y, w=w, h=0, stroke=color(0.5), strokeWidth=0.5,
                parent=page)

        if i == 0:
            newRect(x=x0, y=y, w=20, h=lineHeight, fill=color(1, 0, 0, 0.5),
                    parent=page)
            newRect(x=x0, y=y, w=20, h=descender, fill=color(0, 1, 0, 0.5),
                    parent=page)

def test(context):
    print("creating doc")
    doc = Document(w=W, h=H, context=context)
    doc.name = 'TextBoxes-%s' % doc.context.name
    print('# Testing text boxes in %s' % doc)

    page = doc[1]
    #s = getString(page)
    blurb = Blurb()
    txt = blurb.getBlurb('stylewars_bluray')

    i = len(txt.split('. ')[0]) + 1

    style = {'font': bungeeRegular, 'fontSize': 24, 'lineHeight': 24}
    s = page.newString(txt[0:i], style=style)

    style = {'font': bungeeOutline, 'fontSize': 24, 'lineHeight': 24}
    s += page.newString(txt[i:], style=style)

    fontPath = getFontPath(style)
    font = Font(fontPath)
    upem = font.getUpem()
    fontSize = style.get('fontSize')
    ascender = font.getAscender()
    descender = font.getDescender()
    descender = ((fontSize / float(upem)) * descender)
    lineHeight = style.get('lineHeight')

    w = W/2 - 2*M
    h = 460 #H - 2*M
    x = M
    y = H - M - h

    sc = color(0.3, 0.2, 0.1, 0.5)
    tb = newTextBox(s, x=x, y=y, w=w, h=h, parent=page, stroke=sc)
    y0 = H - M
    drawBaselines(x, y0, w, tb.baselines, lineHeight, descender, page)

    # Get the rest of the text.
    txt = tb.getOverflow()
    style = {'font': robotoRegular, 'fontSize': 24, 'lineHeight': 24}
    s = page.newString(txt, style=style)
    fontPath = getFontPath(style)
    font = Font(fontPath)
    upem = font.getUpem()
    fontSize = style.get('fontSize')
    ascender = font.getAscender()
    descender = font.getDescender()
    descender = ((fontSize / float(upem)) * descender)
    lineHeight = style.get('lineHeight')

    h = 500 
    x = W / 2
    y = M 
    w = W / 2 - M
    sc = color(0.3, 0.2, 0.1, 0.5)
    tb = newTextBox(s, x=x, y=y, w=w, h=h, parent=page, stroke=sc)
    y0 =  M + h
    drawBaselines(x, y0, w, tb.baselines, lineHeight, descender, page)

    print('Starting doc build')
    doc.build()

for contextName in ('DrawBot', 'Flat'):
#for contextName in ('DrawBot',):
#for contextName in ('Flat',):
    context = getContext(contextName)
    test(context)
