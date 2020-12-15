#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#

#     www.pagebot.io
#     Licensed under MIT conditions
#


# -----------------------------------------------------------------------------
#
#     E03_BabelStringMetrics.py
#
#     Show some principles of FlatContext usage.

from pagebot import getContext
from pagebot.document import Document
from pagebot.constants import A3, TOP, EXPORT
from pagebot.conditions import *
from pagebot.elements import *
from pagebot.toolbox.units import *
from pagebot.toolbox.color import noColor, color
from pagebot.toolbox.transformer import path2FileName

FILENAME = path2FileName(__file__)

def draw(contextName):
    context = getContext(contextName)
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)

    # Landscape A3.
    H, W = A3
    SQ = 150
    P  = 50

    doc = Document(w=W, h=H, context=context)
    page = doc[1]
    # Sets the page padding, not equal to test vertical position.
    page.padding = P, P, 2*P, P
    style = dict(font='PageBot-Regular', fontSize=pt(100), textFill=color(0))#, w=800)
    bs = context.newString('ABCD', style)#, w=800)
    bs.add('EFGH', dict(fontSize=200, textFill=color(0, 1, 0)))
    tw, th = bs.textSize
    newText(bs, x=P, y=P, parent=page)#, conditions=Fit())
    newLine(x=P, y=P, w=tw, h=0, stroke=0, parent=page)#, conditions=Fit())

    '''
    #print(bs.topLineXHeight)
    print(bs.w)
    #print(bs.topLineXHeight)
    bs.add('IJKL', dict(fontSize=300))

    # Parent of the element is the current page.
    e = newText(bs, w=SQ, h=SQ, parent=page, conditions=Fit())
    print(bs.w)
    x, y, w, h = e.x, e.y, e.w, e.h
    newRect(parent=page, w=w, h=h, x=x, y=y, fill=None, stroke=color(0, 0, 1),
            strokeWidth=0.5)



    #print(e.bs)
    #print(e.bs.cs) # FormattedString (DrawBot), <FlatBabelData (Flat)

    for line in bs.lines:
        for run in line.runs:
            print(' * run', run)
    '''

    # Solve conditions of all placed elements on the page
    page.solve()

    view = doc.view
    view.showPadding = True
    doc.export(exportPath)


for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
