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

bs = context.newString(txt)

doc.export()
print('Done', EXPORT_PATH)