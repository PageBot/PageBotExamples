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
#     Supporting DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     flatcontext.py
#
# Compares pure Flat and FlatContext functionality.

 # Only runs under Flat
from flat import rgb, font, shape, strike, document
from pagebot.fonttoolbox.objects.font import findFont
from pagebot import getContext
from pagebot.toolbox.color import blackColor, color
from pagebot.filepaths import getResourcesPath
from pagebot.toolbox.units import pt
from pagebot.conditions import *
from pagebot.elements import newText
import os, os.path

WIDTH = 400
HEIGHT = 200
FONTSIZE = 24
LEADING = 36
FONTNAME = 'PageBot-Regular'

def testFlatContext():
    context = getContext('Flat')

    # PageBot implementation, to be used for strings and styles.
    pagebotFont = findFont(FONTNAME)
    pagebotFill = color((180.0 / 255, 0, 125.0 / 255))
    pagebotStroke = color(100.0 / 255, 180.0 / 255, 0)

    # Native flat implementation of fonts and colors.
    flatFont = font.open(pagebotFont.path)
    flatFill = rgb(180, 0, 125)
    flatStroke = rgb(100, 180, 0)

    # Stroke width is the same.
    strokeWidth = 1

    ''' Creates a document. '''

    # Creating a Flat document.
    flatDoc = document(WIDTH, HEIGHT, 'pt')
    flatPage = flatDoc.addpage()

    # Pagebot equivalent.
    #context.newDrawing(WIDTH, HEIGHT)
    pbPage = context.newPage(WIDTH, HEIGHT)
    # print(pbPage)

    ''' Draws a figure. '''

    # Flat.
    figure = shape().fill(flatFill).stroke(flatStroke).width(strokeWidth)
    r = figure.rectangle(50, HEIGHT - 50, 20, 20)
    flatPage.place(r)

    # Pagebot.
    context.fill(pagebotFill)
    context.stroke(pagebotStroke)
    context.strokeWidth(strokeWidth)
    context.rect(50, 50, 20, 20)

    #print(p.items[0].item.style.width)
    #print(context.pages[0].items[0].item.style.width)

    #s = context.pages[0].items[0]

    #print(s.item.style.fill)
    #print(s.item.style.stroke)
    #print(s.item.style.join)
    #print(s.item.style.limit)

    ''' Draws text. '''

    msg = 'Hello world!'

    # Flat.

    header = strike(flatFont).color(flatStroke).size(FONTSIZE, LEADING, units='pt')
    t = header.text(msg)
    placedText = flatPage.place(t).frame(100, 100, 380, 80)

    # Pagebot.
    style = dict(font=pagebotFont, fontSize=FONTSIZE, textFill=pagebotStroke,
            leading=LEADING)
    bs = context.newString(msg, style=style)
    #context.text('bla', (50, 100)) # TODO: also for native flat.
    context.text(bs, (100, 100))

    #print(headline.style.size)
    #print(headline.style.leading)
    #print(headline.style.color.r)
    #print(headline.style.color.g)

    # Now for conditions and elements.
    c = (Left2Left(), Fit2Right(), Float2Top())
    style = dict(fontSize=14, font=pagebotFont)
    msg = 'Testing textBox'
    print(msg)
    bs = context.newString(msg, style=style)
    print(type(bs))

    newText(bs, font=pagebotFont, parent=pbPage, conditions=c, fill=0.9,
            margin=4)
    #print(p.items)

    ''' Exports file. '''

    im = flatPage.image(kind='rgb')


    # TODO:
    #imagePath = getResourcesPath() + '/images/peppertom_lowres_398x530.png'
    #size = context.imageSize(imagePath)
    #print(size)

    if not os.path.exists('_export'):
        os.mkdir('_export')

    #print('Exporting native')
    flatDoc.pdf('_export/native-flat.pdf')
    #im.png('_export/native-flat.png')
    #im.jpeg('_export/native-flat.jpg')
    #p.svg('_export/native-flat.svg')
    #print(context.doc)

    context.saveDrawing('_export/pagebot-flat.pdf')
    #print('Exporting pagebot')
    #context.saveDrawing('_export/pagebot-flat.png')
    #context.saveDrawing('_export/pagebot-flat.jpg')
    #context.saveDrawing('_export/pagebot-flat.svg')

testFlatContext()
