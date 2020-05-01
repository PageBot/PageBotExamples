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
#     01_BabelStringsContexts.py
#
#     Show the working on BabelStrings in a defined context.
#     Construct the export file name from this source.
#     Not using a Document instance, directly drawing on the context.
#

from pagebot import getContext
from pagebot.contexts.flatcontext.flatcontext import FlatContext
from pagebot.toolbox.units import pt, em
from pagebot.toolbox.color import color


W, H = pt(600, 300)
M = pt(100)

contexts = (
    ('DrawBot', getContext('DrawBot')),
    #('Flat', getContext('Flat'))
)

for contextId, context in contexts:

    # Make export path from this filename, and dependent on the context.
    exportPath = '_export/01_BabelStringContexts-%s.pdf' % contextId
    
    # Create a page and set y on top margin.
    context.newPage(W, H)
    y = H - M
    style = dict(textFill=color(0, 0, 1), leading=em(1.4), fontSize=36) 
    bs = context.newString('Context: %s\n' % contextId, style=style)
    context.drawText(bs, (100, y, bs.tw, bs.th)) # Get size from unwrapped string.
    y -= 36

    # Create formatted string, with default settings of font, fontSize and textFill color
    style = dict(textFill=color(spot=300), leading=em(1.4), fontSize=18) 
    bs = context.newString('This is a formatted BabelString of class %s\n' % context.__class__.__name__, style)
    print(bs.__class__.__name__)
    context.drawText(bs, (100, y, bs.tw, bs.th))

    y -= 50

    # Add string with formatting style dict
    bs += context.newString('Add an other string with color/size/leading format',
        style=dict(textFill=color(1, 0, 0), fontSize=20, leading=em(1.4)))
    print('BabelString:', bs)
    context.drawText(bs, (100, y, bs.tw, bs.th))

    # Save the context as PDF document
    context.saveImage(exportPath)

