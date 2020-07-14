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
#     E01_FilePaths.py
#
#     Shows how get PageBot file paths.  Not to be confused with BezierPaths
#     which are paths used for drawing vectores.
#
from pagebot import *
from pagebot.constants import A3, EXPORT
from pagebot.filepaths import getRootPath, getResourcesPath
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.units import pt
from pagebot.conditions import *
from pagebot.elements import *
from pagebot.document import Document
from pagebot.toolbox.units import pt
from pagebot.toolbox.transformer import path2FileName

H, W = A3
GUTTER = pt(12)
FILENAME = path2FileName(__file__)

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)

    # Make a Document instance for this size and context, intializing one page.
    doc = Document(w=W, h=H, context=context)

    # Get the page.
    page = doc[1]

    # Make a set of conditions for the element positions of this page.
    c = (Left2Left(), Fit2Right(), Float2Top())

    # Find the demo font, as supplied with the PageBot library installation.
    # This is a subset of TYPETR Upgrade Regular.
    f = findFont('PageBot-Regular')

    rootPath = getRootPath() # Location of this PageBot library
    style = dict(fontSize=14, font=f)
    msg = 'Root path is %s' % rootPath
    bs = context.newString(msg, style)
    t = makeText(bs, page, f, c)

    resourcesPath = getResourcesPath()
    msg = 'Resources path is %s' % resourcesPath
    bs = context.newString(msg, style)
    t = makeText(bs, page, f, c)

    if contextName == 'Flat':
        placedText = bs.cs.pt
        for i, (height, run) in enumerate(placedText.layout.runs()):
            print(i, height)
            for st, s in run:
                print(s)

    '''
    font = findFont('PageBot-Regular')
    msg = 'Default font path is %s' % font.path
    msg = '\n\t'.join(msg.split('/'))
    bs = context.newString(msg, style)
    c = (Right2Right(), Float2Top())
    e = makeText(bs, page, f, c)
    #print(e.w)
    #print(e.h)
    #print(e.bs.th)
    #print(e.pb)
    #e.w = page.pw / 2 - 2*GUTTER
    #e.mr = 0


    msg = 'PageBot font path is %s' % f.path
    msg = '\n\t'.join(msg.split('/'))
    bs = context.newString(msg, style)
    c = (Left2Left(), Float2Top())
    e = makeText(bs, page, f, c)
    e.w = page.pw / 2 - 2*GUTTER
    '''

    # Let the page solve all of its child element layout conditions.
    page.solve()
    r = newRect(x=t.x, y=t.y, w=t.w, h=t.h, parent=page, stroke=(0, 1, 0),
            strokeWidth=1, showOrigin=True)
    doc.export(exportPath)

def makeText(t, page, f, c):
    """Create a new text box with e give layout conditions
    and with page as parent."""
    t = newText(t, font=f, parent=page, conditions=c, #fill=0.9, stroke=(1, 0,0), strokeWidth=1,
        margin=GUTTER)
    t.showOrigin = True
    return t

#for contextName in ('Flat',):
for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
