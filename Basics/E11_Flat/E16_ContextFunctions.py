#
#     Copyright (c) 2017 Thom Janssen <https://github.com/thomgb>
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E16_ContextFunctions.py
#
#     Prototyping the context functions for FlatContext
#     that are required by PageBot AbstractContext

import os
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.loremipsum import loremipsum
from pagebot.contexts import getContext
from pagebot.toolbox.units import pt
from pagebot.document import Document

context = getContext('Flat')

W = H = pt(1000)

EXPORT_PATH = '_export/16_ContextFunctions.pdf'
if not os.path.exists('_export'):
	os.mkdir('_export')

# Get the PageFont instance
font = findFont('PageBot-Regular')
fontSize = pt(24)

style = dict(font=font, fontSize=fontSize)
txt = loremipsum()

doc = Document(w=W, h=H, context=context)
page = doc[1]

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
# Set the BabelString at a requested width
bs.w = 500
print('Request width of the bs:', bs.w)
# And there is a placed text, that we can query for its frame
print(bs.tw)
print('Placed text:', bs.cs.pt, bs.cs.pt.width, bs.cs.pt.height)

doc.export()
print('Done', EXPORT_PATH)