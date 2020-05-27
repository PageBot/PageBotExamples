#!/usr/bin/env python3
#     Copyright (c) 2017 Thom Janssen <https://github.com/thomgb>
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E20_TextPositionByContext.py
#

import os
from pagebot.contexts import getContext
from pagebot.document import Document
from pagebot.elements import *
from pagebot.toolbox.loremipsum import loremipsum
from pagebot.toolbox.units import pt
from pagebot.fonttoolbox.objects.font import findFont

W = H = pt(800)
padding = pt(30)

EXPORT_PATH = '_export/20_TextPositionByContext%s.pdf'
if not os.path.exists('_export'):
	os.mkdir('_export')

contexts = (
	getContext('DrawBot'),
	getContext('Flat'),
)
style = dict(font='PageBot-Regular', fontSize=pt(24))

for context in contexts:
	doc = Document(w=W, h=H, context=context)
	page = doc[1]
	page.padding = padding
	bs = context.newString(loremipsum(), style)
	newText(bs, parent=page, x=padding, y=padding, w=page.pw, h=page.ph)

	doc.export(EXPORT_PATH % context.name)

print('Done', EXPORT_PATH)
