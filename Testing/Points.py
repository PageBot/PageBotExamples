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
#     Points.py
#

from pagebot.contexts.basecontext.basepath import BasePath
from pagebot.document import Document
from pagebot.toolbox.units import *

# TODO: find out how to remove overlap on text.
# Maybe avoid using text but load font in path?

def test(context):

    doc = Document(w=800, h=600, autoPages=1, context=context)
    page = doc[1] # Get the single page from te document.
    path = BasePath(context)
    point = pt(100), p(5)
    path.beginPath()
    path.moveTo(point)
    point = 100, 50
    path.lineTo(point)
    path.curveTo(pt(100, 200), pt(200, 200), pt(200, 100))
    path.closePath()
    print(path.points)
    print(len(path))
    #context.newPage(w=800, h=600)
    #context.drawPath(p)
    doc.export()


if __name__ == '__main__':
    from pagebot import getContext

    for contextName in ('DrawBot', 'Flat'):
        context = getContext(contextName)
        test(context)
