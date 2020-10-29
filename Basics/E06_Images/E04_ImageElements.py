#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
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
#     E04_ImageElements.py
#
#     This script generates a page with random color squares, indicating where their position is.
#

from pagebot.filepaths import getResourcesPath
from pagebot.contexts import getContext
from pagebot.constants import TOP, BOTTOM, EXPORT
from pagebot.conditions import *
from pagebot.elements import *
from pagebot.document import Document
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt
from pagebot.toolbox.transformer import path2FileName

PADDING = 30
W = H = 1000
FILENAME = path2FileName(__file__)

def draw(contextName):
    '''
    The getRootStyle() function answers a standard Python dictionary, where all
    PageBot style entries are filled by their default values. The root style is
    kept in RS as reference for the ininitialization of all elements. Each element
    uses the root style as copy and then modifies the values it needs. Note that
    the use of style dictionaries is fully recursive in PageBot, implementing a
    cascading structure that is very similar to what happens in CSS.
    '''
    context = getContext(contextName)
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    path = getResourcesPath() + '/images/cookbot10.jpg'
    doc = Document(w=W, h=H, title='Color Squares', autoPages=1, context=context)
    view = doc.getView()
    # Don't show crop marks, etc.
    view.padding = 0
    view.showOrigin = True

    # Get list of pages with equal y, then equal x.
    page = doc[1]
    page.name = 'This is a demo page for floating child elements'
    page.padding = PADDING

    img = newImage(path, padding=0,
                   parent=page,
                   conditions=(Top2Top(),
                               Fit2Width(),
                               ),
                   yAlign=TOP,
                   fill=color(0, 1, 0, 0.3),
                   stroke=color(1, 0, 0),
                   scaleImage=True)

    newImage(path, padding=0,
                   parent=page,
                   conditions=(Bottom2Bottom(),
                               Fit2Width(),
                               ),
                   yAlign=BOTTOM,
                   fill=color(1, 0, 0, 0.3),
                   stroke=color(0, 0, 1),
                   scaleImage=False)

    page.solve()
    print('Original size:', img.iw, img.ih)
    print('Resized:', img.w, img.h)
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
