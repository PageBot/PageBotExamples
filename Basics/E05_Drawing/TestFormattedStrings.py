#!/usr/bin/env python3
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
#     DB_TestFormattedStrings.py
#
import sys
from pagebot import getContext
from pagebot.toolbox.units import pt
from pagebot.toolbox.color import blackColor, noColor, color

context = getContext()

# Make BabelString,
bs = context.newString('Book Cover', style=dict(font='Georgia', fontSize=pt(50)))
print('Text size book cover: (%f, %f)' % context.textSize(bs))

# Empty string.
bs = context.newString('')

# Contains a DrawBot FormattedString.
aa = bs.s

print(type(aa))
aa.append("123", font="Helvetica", fontSize=100, fill=color(1, 0, 0))
aa.fontSize(80)
aa.append("Book Cover", font="Georgia", fill=color(0, 1, 0))
print(aa)
print('Text size: (%f, %f)' % textSize(aa))

print('Ascender: %f' % aa.fontAscender())
print('Descender: %f' % aa.fontDescender())
print('Difference: %f' % (aa.fontAscender() - aa.fontDescender()))

context.stroke(blackColor)
context.fill(noColor)
w, h = context.textSize(aa)
context.rect(pt(100), pt(100), pt(w), pt(h))
context.fill(blackColor)
context.fontSize(pt(80))
context.text(bs, (100, 100))

