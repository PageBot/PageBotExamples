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
from pagebot.contexts.basecontext.babelstring import BabelString
from pagebot.toolbox.color import Color
from pagebot.toolbox.units import pt
from pagebot.toolbox.transformer import json2Dict
from pagebot.document import Document
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.elements import newTextBox, newImage

W = 652
H = 850
W = pt(W)
H = pt(H)
PADDING = pt(83, 42, 19, 33)
ACC_GUTTER = pt(32) # Distance between accommodations
IMG_GUTTER = pt(3) # Vertical distance between images
COL_GUTTER = pt(12) # Distance between columns

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
    doc = Document(w=W, h=H, context=context)
    view = doc.getView()
    view.showPadding = True
    view.showDimensions = True
    view.showOrigin = True

    page = doc[1]

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

    for k, v in content.items():
        src = 'jsondata/' + v['assets'][0]['src']
        break

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

        addTitle(page, context, title)
        addDescription(page, context, description)
        addImage(page, context, src)
        """
        # dh is added offset from top page edge.
        dh = drawDescription(context, description, dh)
        dh = drawLocation(context, location, dh)
        """

        # Just testing first language for now.
        break

    page.solve()
    path = '_export/doc-%s.pdf' % doc.context.name
    doc.export(path)

def addTitle(page, context, title):
    style = {'font': boldFont.path, 'fontSize': HEADSIZE}
    bs = context.newString(title, style=style)
    newTextBox(bs, parent=page, w=W/2, conditions=[Right2SideRight(),
        Top2Top()])

def addDescription(page, context, description):
    style = {'font': regularFont.path, 'fontSize': 12, 'leading': 14}
    bs = context.newString(description, style=style)
    newTextBox(bs, parent=page, w=W/2, conditions=[Right2SideRight(),
        Top2Top()])

def addImage(page, context, src):
    newImage(src,
        parent=page,
        w=(W-COL_GUTTER)/2,
        h=(H-IMG_GUTTER)/2,
        conditions=[Left2SideLeft(), Float2SideTop()],
        mt=IMG_GUTTER,
        scaleImage=False,
    )


loadJSON(drawBotContext)
loadJSON(flatContext)
