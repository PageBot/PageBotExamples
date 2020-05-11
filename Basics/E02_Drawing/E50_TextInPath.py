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
#     E30_SierpinskiSquare.py
#
#    Example from http://www.drawbot.com/content/text/drawingText.html
#    Currently only works in DrawBotContext
#

from pagebot.contexts import getContext
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.constants import *

context = getContext('DrawBot')
font = findFont(DEFAULT_FONT)

# FIXME: don't use DrawBot functions.
#from drawBot import BezierPath, width, height, translate, scale, drawPath, \
#        font, fontSize, fill, textBox, saveImage

path = context.b.BezierPath()
# draw some text
# the text will be converted to curves
path.text("a", font=font.path, fontSize=500)
# set an indent
indent = 50
# calculate the width and height of the path
minx, miny, maxx, maxy = path.bounds()
w = maxx - minx
h = maxy - miny
# calculate the box where we want to draw the path in
boxWidth = context.b.width() - indent * 2
boxHeight = context.b.height() - indent * 2
# calculate a scale based on the given path bounds and the box
s = min([boxWidth / float(w), boxHeight / float(h)])
# translate to the middle
context.b.translate(context.b.width()*.5, context.b.height()*.5)
# set the scale
context.b.scale(s)
# tanslate the negative offset, letter could have overshoot
context.b.translate(-minx, -miny)
# translate with half of the width and height of the path
context.b.translate(-w*.5, -h*.5)
# draw the path
context.b.drawPath(path)
# set a font
context.b.font(font.path)
# set a font size
context.b.fontSize(5)
# set white as color
context.b.fill(1)
# draw some text in the path
context.b.textBox("abcdefghijklmnopqrstuvwxyz"*30000, path)
context.b.saveImage('_export/E50_TextInPath.pdf')
