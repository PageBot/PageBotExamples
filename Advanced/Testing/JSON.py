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
#     JSON.py
#

import traceback
import os.path
from pagebot import getContext
from pagebot.contexts.base.babelstring import BabelString
from pagebot.toolbox.color import Color
from pagebot.toolbox.units import pt
from pagebot.toolbox.transformer import json2Dict
from pagebot.document import Document
from pagebot.fonttoolbox.objects.font import findFont

W = 652
H = 850
W = pt(W)
H = pt(H)

#f = Color(0, 0, 0)
s = Color(1, 0, 0)

drawBotContext = getContext('DrawBot')
flatContext = getContext('Flat')
boldFontName = 'PageBot-Bold'
boldFont = findFont(boldFontName)
regularFontName = 'Roboto-Regular'
regularFont = findFont(regularFontName)

def loadJSON(context):
    p = os.path.abspath(__file__)
    d = os.path.dirname(p)
    src = '/jsondata/AMXP--119s014.json'
    p = d + src
    f = open(p, 'r')
    jsondata = f.read()
    jsondict = json2Dict(jsondata)

    context.newDrawing()
    context.newPage(w=W, h=H)
    title = ''
    addedvalue = ''
    description = ''
    location = ''
    prices = ''
    facilities = ''

    for lang in jsondict['translations']:
        for _, o in jsondict['translations'][lang]['objects'].items():
            for k, v in o.items():
                if k == 'name':
                    title = v
                elif k == 'desc':
                    description = v
                elif k == 'location':
                    location = v
                elif k == 'facilites':
                    facilities = v
                elif k == 'added-values':
                    addedvalue = v
                elif k == 'prices':
                    prices = v

        drawTitle(context, title)
        drawDescription(context, description)

        path = '_export/%s-%s-%s.pdf' % ('JSON', context.name, lang)
        context.saveImage(path)
        print('Saved %s' % path)

        # Just testing first language.
        break

def drawTitle(context, title):
    x = 60 
    y = H - 60
    style = {'font': boldFont.path, 'fontSize': 14}
    babelstring = context.newString(title, style=style)
    context.text(babelstring, pt(x, y))

def drawDescription(context, description):
    x = 60 
    y = H - 100
    w = 200
    h = 300
    box = (x, y, w, h)
    style = {'font': regularFont.path, 'fontSize': 12}
    bs = context.newString(description, style=style)#, w=100) # Scales to size?
    bs2 = context.textOverflow(bs, box)
    tb = context.textBox(bs, box)
    context.fill(None)
    context.stroke(s)
    context.rect(x, y, w, -h)

def drawLocation(context, location):
    x = 60 
    y = H - 400
    w = 200
    h = 300
    box = (x, y, w, h)
    style = {'font': regularFont.path, 'fontSize': 12}
    bs = context.newString(location, style=style)#, w=100)
    bs2 = context.textOverflow(bs, box)
    tb = context.textBox(bs, box)


loadJSON(drawBotContext)
loadJSON(flatContext)
