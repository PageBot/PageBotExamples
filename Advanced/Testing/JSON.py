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
from pagebot.elements import newTextBox

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
LINE = 12
TEXTSIZE = 12
HEADSIZE = 14

def loadJSON(context):
    doc = Document(w=W, h=H, originTop=False, context=context)
    view = doc.getView()
    view.showPadding = True
    view.showDimensions = True
    view.showOrigin = True

    page = doc[1]
    page.solve()

    path = '_export/doc-%s.pdf' % doc.context.name
    doc.export(path)


    '''
    base = os.path.abspath(__file__)
    d = os.path.dirname(base)
    src = '/jsondata/AMXP--119s014.json'
    p = d + src
    f = open(p, 'r')
    jsondata = f.read()
    jsondict = json2Dict(jsondata)
    content = jsondict['content']

    context.newDrawing()
    context.newPage(w=W, h=H)
    src = ''

    for k, v in content.items():
        src = 'jsondata/' + v['assets'][0]['src']
        break

    #context.image(src, p=pt(0, 0), w=pt(200), h=pt(300))
    context.fill(None)
    context.stroke(s)

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

        """
        # dh is added offset from top page edge.
        dh = drawTitle(context, title, 0)
        dh = drawDescription(context, description, dh)
        dh = drawLocation(context, location, dh)
        """

        path = '_export/%s-%s-%s.pdf' % ('JSON', context.name, lang)
        context.saveImage(path)
        print('Saved %s' % path)

        # Just testing first language.
        break
    '''

def drawTitle(context, title, dh):
    x = 60 
    y = 60
    dh += y
    y0 = H - dh
    style = {'font': boldFont.path, 'fontSize': HEADSIZE}
    babelstring = context.newString(title, style=style)
    context.text(babelstring, pt(x, y0))
    p0 = (x, y0)
    p1 = (x + 100, y0)
    context.line(p0, p1)
    return dh

def drawDescription(context, description, dh):
    x = 60 
    y = H - dh - LINE
    w = 200
    h = 300
    box = (x, y, w, h)
    style = {'font': regularFont.path, 'fontSize': 12, 'leading': 14}
    bs = context.newString(description, style=style)#, w=100) # Scales to size?

    # TODO: calculate overflow.
    #tb = context.textBox(bs, box)
    #tb = newTextBox(bs, box, context=context)
    context.rect(x, y, w, -h)
    #bs2 = context.textOverflow(bs, box)
    #print('Overflow: %s' % bs2)
    #lines = context.textLines(bs, box)

    y1 = y - LINE
    p0 = (x, y1)
    p1 = (x + w, y1)
    context.line(p0, p1)
    return dh + h + LINE

def drawLocation(context, location, dh):
    x = 60 
    y = H - dh - LINE
    w = 200
    h = 3 * LINE
    box = (x, y, w, h)
    style = {'font': regularFont.path, 'fontSize': 12, 'leading': 12}
    bs = context.newString(location, style=style)#, w=100)
    bs2 = context.textOverflow(bs, box)
    tb = context.textBox(bs, box)
    context.rect(x, y, w, -h)
    drawLines(context, x, y - LINE, w, 2)
    return dh + h + LINE

def drawLines(context, x, y, w, n):
    for i in range(n):
        y0 = y - (i * LINE * 1.4)
        print(y0)
        p0 = (x, y0)
        p1 = (x + w, y0)
        context.line(p0, p1)

loadJSON(drawBotContext)
loadJSON(flatContext)
