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
from pagebot.conditions import *
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
    #doc = Document(w=W, h=H, originTop=True, context=context)
    view = doc.getView()
    view.showPadding = True
    view.showDimensions = True
    view.showOrigin = True

    page = doc[1]
    page.solve()

    path = '_export/doc-%s.pdf' % doc.context.name
    doc.export(path)


    base = os.path.abspath(__file__)
    d = os.path.dirname(base)
    src = '/jsondata/AMXP--119s014.json'
    p = d + src
    f = open(p, 'r')
    jsondata = f.read()
    jsondict = json2Dict(jsondata)
    content = jsondict['content']
    src = ''

    for k, v in content.items():
        src = 'jsondata/' + v['assets'][0]['src']
        break

    #context.image(src, p=pt(0, 0), w=pt(200), h=pt(300))
    #context.fill(None)
    #context.stroke(s)

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

        tb = addTitle(page, context, title, 0)
        print(tb)
        """
        # dh is added offset from top page edge.
        dh = drawDescription(context, description, dh)
        dh = drawLocation(context, location, dh)
        """

        # Just testing first language for now.
        break

def addTitle(page, context, title, dh):
    style = {'font': boldFont.path, 'fontSize': HEADSIZE}
    babelstring = context.newString(title, style=style)
    tb = newTextBox(babelstring, parent=page, w=W/2,
            conditions=[Right2RightSide(), Top2Top()])
    return tb

loadJSON(drawBotContext)
loadJSON(flatContext)
