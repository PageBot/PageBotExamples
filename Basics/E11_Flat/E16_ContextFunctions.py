#!/usr/bin/env python3
#
#     Copyright (c) 2017 Thom Janssen <https://github.com/thomgb>
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E16_FlatBabelDataFunctions.py
#
#     Prototyping the context functions for FlatContext
#     that are required by PageBot AbstractContext
#     FlatBabelData is defined in flatContext.py, used for
#     caching Flat text data in BabelString.cs

import os
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.loremipsum import loremipsum
from pagebot.contexts import getContext
from pagebot.toolbox.units import pt
from pagebot.document import Document

context = getContext('Flat')

# Get the PageFont instance
font = findFont('PageBot-Regular')
fontSize = pt(16)

style = dict(font=font, fontSize=fontSize)
txt = loremipsum()

bs = context.newString(txt, style)
print('BabelString runs:', len(bs.runs))
# Now this BabelString is "FlatContext" flavoured.
# This means that queries and functions will address
# the FlatContext for doing conversions and calculations.
print('FlatContext stores cached data in bs._cs as FlatBabelData:', bs.cs)
# The cache FlatBabelData.runs contain FlatRunData
print('bs.cs.runs[0]:', bs.cs.runs[0])
print('Flat.strike for this run bs.cs.runs[0].st:', bs.cs.runs[0].st)
# In the BabelString context cache, now htere is a dummy Flat.document and a Flat.page.
print('Dummy Flat.document and Flat.page:', bs.cs.doc, bs.cs.page)
print()

# Set the BabelString at a requested width
bs.w = 500
print('Request column width of the bs:', bs.w, ' Undefined height:', bs.h)
# Now there is a placed text, that we can query for its frame
print('Calculated column width:', bs.tw)
print('Placed text:', bs.cs.pt, bs.cs.pt.width, bs.cs.pt.height)
print('context.getTextSize(bs):', context.getTextSize(bs))
print('len(context.getTextLines(bs)):', len(context.getTextLines(bs)))
print()

bs.w = 1000
print('Request column width of the bs:', bs.w, ' Undefined height:', bs.h)
# Now there is a placed text, that we can query for its frame
print('Calculated column width:', bs.tw)
print('Placed text:', bs.cs.pt, bs.cs.pt.width, bs.cs.pt.height)
print('context.getTextSize(bs):', context.getTextSize(bs))
print('len(context.getTextLines(bs)):', len(context.getTextLines(bs)))
print()

print('Done')
