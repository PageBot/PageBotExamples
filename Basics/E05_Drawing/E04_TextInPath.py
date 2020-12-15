#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#
#    P A G E B O T  E X A M P L E S
#
#    www.pagebot.io
#    Licensed under MIT conditions
#
# -----------------------------------------------------------------------------
#
#    E04_TextInPath.py
#
#    Example from http://www.drawbot.com/content/text/drawingText.html
#    FIXME: Currently only works in DrawBotContext, need to implement with
#    PageBot BezierPath.
#

from pagebot.contexts import getContext
from pagebot.constants import *
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.transformer import path2FileName

FILENAME = path2FileName(__file__)

def makeDrawing(contextName):
    '''
    Traceback (most recent call last):
  File "./E04_TextInPath.py", line 72, in <module>
    makeDrawing(contextName)
  File "./E04_TextInPath.py", line 36, in makeDrawing
    path = context.BezierPath()
  File "/Users/michiel/VirtualEnvironments/pagebot/lib/python3.8/site-packages/pagebot/contexts/basecontext/basecontext.py", line 1206, in BezierPath
    return self.b.BezierPath(path=path, glyphSet=glyphSet)
AttributeError: module 'flat' has no attribute 'BezierPath'
    '''

    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    font = findFont(DEFAULT_FONT)
    path = context.BezierPath()
    context.fill(1)
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
    boxWidth = context.width() - indent * 2
    boxHeight = context.height() - indent * 2
    # calculate a scale based on the given path bounds and the box
    s = min([boxWidth / float(w), boxHeight / float(h)])
    # translate to the middle
    context.translate(context.width()*.5, context.height()*.5)
    # set the scale
    context.scale(s)
    # tanslate the negative offset, letter could have overshoot
    context.translate(-minx, -miny)
    # translate with half of the width and height of the path
    context.translate(-w*.5, -h*.5)
    # draw the path
    context.drawPath(path)
    # set a font
    context.font(font.path)
    # set a font size
    context.fontSize(5)
    # set white as color
    # draw some text in the path
    context.text("abcdefghijklmnopqrstuvwxyz", path)
    context.saveImage(exportPath)

for contextName in ('DrawBot', 'Flat'):
    makeDrawing(contextName)
