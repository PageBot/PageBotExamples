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

# -----------------------------------------------------------------------------
#
#     Texts.py
#
#     Tests pagebot texts.

from pagebot import getContext
from pagebot.constants import *
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.document import Document
from pagebot.elements import *
from pagebot.fonttoolbox.objects.font import findFont, Font, getFontPath
from pagebot.style import getRootStyle
from pagebot.toolbox.units import pt, upt
from pagebot.toolbox.color import noColor, color
from pagebot.toolbox.transformer import path2FileName

H, W = A3
W = pt(W)
H = pt(H)
M = 50
FILENAME = path2FileName(__file__)

robotoRegular = findFont('Roboto-Regular')
pageBotBold = findFont('PageBot-Bold')
pageBotRegular = findFont('PageBot-Regular')
robotoBold = findFont('Roboto-Bold')
bungeeRegular = findFont('Bungee-Regular')
bungeeHairline = findFont('Bungee-HairlineRegular')
bungeeOutline = findFont('Bungee-OutlineRegular')

def drawBaselines(x0, y0, w, baselines, s, page):
    print(s.style)
    #fontPath = getFontPath(s.style)
    #font = Font(fontPath)
    font = s.style['font']
    infoLine = 1
    baseH0 = 0
    upem = font.getUpem()
    fontSize = s.style.get('fontSize')
    ascender = font.getAscender()
    ascender = ((fontSize / float(upem)) * ascender)
    descender = font.getDescender()
    descender = ((fontSize / float(upem)) * descender)
    #lineHeight = s.lineHeight
    #print(lineHeight)
    #print('style %s' % s.style['font'])
    #print('ascdesc  %s' % (ascender - descender))
    #print('diff  %s' % (fontSize - (ascender - descender)))

    for i, baseline in enumerate(baselines):
        y = y0 - baseline
        # Calculates baseline offsets between each line.
        baseH = baseline - baseH0

        # Prints distances from top between lines.
        #print(baseH)
        baseH0 = baseline
        #newLine(x=x0, y=y, w=w, h=0, stroke=color(0.5), strokeWidth=0.5,
        #        parent=page)

        if i == infoLine:
            dx = 20
            x = x0
            #newRect(x=x, y=y, w=dx, h=lineHeight, fill=color(1, 0, 0, 0.5),
            #        parent=page)
            x += dx
            newRect(x=x, y=y + descender, w=dx, h=fontSize, fill=color(1, 1, 0, 0.5),
                    parent=page)

            x += dx
            newRect(x=x, y=y, w=dx, h=descender, fill=color(0, 1, 0, 0.5),
                    parent=page)
            newRect(x=x, y=y, w=dx, h=ascender, fill=color(0, 0, 1, 0.5),
                    parent=page)

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    doc = Document(w=W, h=H, context=context)

    doc.name = 'Textes-%s' % doc.context.name
    print('# Testing text boxes in %s' % doc)

    page = doc[1]
    page.showOrigin = True
    page.showDimensions = True
    #s = getString(page)
    blurb = Blurb()
    txt = blurb.getBlurb('stylewars_bluray')

    # First sentence.
    sentences = txt.split('. ')

    # Adds a string with a style.
    style = {'font': bungeeRegular, 'fontSize': 24, 'leading': em(1.5)}
    t0 = sentences[0] + '. '

    s = context.newString(t0, style=style)

    # Adds another string with a different style.
    t1 = '. '.join(sentences[1:])
    style = {'font': bungeeOutline, 'fontSize': 24, 'leading': em(1.5)}
    s += context.newString(t1, style=style)

    w = W/2 - 2*M
    h = 460 #H - 2*M
    x = M
    y = H - M - h

    sc = color(0.3, 0.2, 0.1, 0.5)
    tb = newText(s, x=x, y=y, w=w, h=h, parent=page)
    #tb = newText(s, x=x, y=y, w=w, h=h, parent=page, stroke=sc)
    y0 = H - M
    drawBaselines(x, y0, w, tb.baselines, s, page)

    '''
    # Get the rest of the text.
    txt = tb.getOverflow()
    style = {'font': pageBotBold, 'fontSize': 24, 'leading': 1.5}
    s = context.newString(txt, style=style)

    w = W/2 - 2*M
    h = 240 #H - 2*M
    x = M
    y = M

    tb = newText(s, x=x, y=y, w=w, h=h, parent=page, stroke=sc)
    y0 = M + h
    drawBaselines(x, y0, w, tb.baselines, s, page)

    # Get the rest of the text.
    txt = tb.getOverflow()
    style = {'font': robotoRegular, 'fontSize': 24, 'leading': 1.5}
    s = context.newString(txt, style=style)

    h = 500
    x = W / 2
    y = M
    w = W / 2 - M
    tb = newText(s, x=x, y=y, w=w, h=h, parent=page, stroke=sc)
    y0 =  M + h
    drawBaselines(x, y0, w, tb.baselines, s, page)
    '''

    print('Starting doc build')
    doc.build()

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
