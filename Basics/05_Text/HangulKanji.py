#!/usr/bin/evn python
# encoding: utf-8
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
#     HangulKanji.py

from pagebot import getContext
from pagebot.document import Document
from pagebot.elements import *
from pagebot.toolbox.units import pt
from pagebot.toolbox.color import color

context = getContext('DrawBot')
fontSize = pt(100)
W, H = pt(1000, 1000)

s = """글자가 일상이 된다 산돌커뮤니케이션 ABCD123 Latin すべての文化集団は，独自の言語，文字，書記システムを持つ．それゆえ，個々の書記システムをサイバースペースに移転することは. ABCD123 Latin included"""

doc = Document(w=W, h=H, context=context)
page = doc[1]

fsr = context.newString(s, style=dict(font='Verdana', fontSize=fontSize))
fsb = context.newString(s, style=dict(font='Verdana-Bold', fontSize=fontSize))
fsbRed = context.newString(s, style=dict(font='Verdana', fill=color(1, 0, 0),
    fontSize=fontSize))

newText(fsr, x=100, y=600, w=820, h=300, parent=page)
newText(fsb, x=100, y=400, w=820, h=300, parent=page)
newText(fsbRed, x=100, y=200, w=820, h=300, parent=page)
newText(fsr, x=100, y=0, w=820, h=330, parent=page)

doc.export('_export/TestKanjiFormattedString.pdf')
