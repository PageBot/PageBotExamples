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
#     Shows how get Roboto file paths.  Not to be confused with BezierPaths
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
from pagebot.toolbox.units import pt, em
from pagebot.toolbox.transformer import path2FileName

H, W = A3
GUTTER = pt(12)
FILENAME = path2FileName(__file__)
font = findFont('Roboto-Regular')
fontSize = 14
leading = em(1.4)
#leading = 1.4

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)

    # Make a Document instance for this size and context, intializing one page.
    doc = Document(w=W, h=H, context=context)

    # Get the page.
    page = doc[1]
    page.padding = 20
    view = doc.getView()
    view.showPadding = True

    # Make a set of conditions for the element positions of this page.
    c = (Left2Left(), Float2Top(), Fit2Right())

    # Find the demo font, as supplied with the Roboto library installation.
    # This is a subset of TYPETR Upgrade Regular.

    rootPath = getRootPath() # Location of this Roboto library
    style = dict(fontSize=fontSize, font=font, leading=leading)
    msg = 'Root path is %s' % rootPath
    bs = context.newString(msg, style)
    topText1 = makeText(bs, page, font, c)

    resourcesPath = getResourcesPath()
    msg = 'Resources path is %s' % resourcesPath
    bs = context.newString(msg, style)
    topText2 = makeText(bs, page, font, c)

    '''
    if contextName == 'Flat':
        placedText = bs.cs.pt
        for i, (height, run) in enumerate(placedText.layout.runs()):
            print(i, height)
            for st, s in run:
                print(s)
    '''

    msg = 'Default font path is %s' % font.path
    msg = '\n • '.join(msg.split('/'))
    bs = context.newString(msg, style)
    c = (Right2Right(), Float2Top())
    column1 = makeText(bs, page, font, c)

    # Forces column width, so second column isn't pushed away.
    column1.w = page.pw / 2 - 2*GUTTER
    column1.mr = 0

    msg = 'Roboto font path is %s' % font.path
    msg = '\n • '.join(msg.split('/'))
    bs = context.newString(msg, style)
    c = (Left2Left(), Float2Top())
    column2 = makeText(bs, page, font, c)
    column2.w = page.pw / 2 - 2*GUTTER

    # Let the page solve all of its child element layout conditions.
    page.solve()

    y = column1.y - column1.h + fontSize
    r = newRect(x=column1.x, y=y, w=column1.w, h=column1.h, parent=page, stroke=(0, 1, 0),
           strokeWidth=1, showOrigin=True)
    y = column2.y - column2.h + fontSize
    r = newRect(x=column2.x, y=y, w=column2.w, h=column2.h, parent=page, stroke=(1, 0, 0),
           strokeWidth=1, showOrigin=True)
    doc.export(exportPath)

def makeText(t, page, f, c):
    """Create a new text box with e give layout conditions
    and with page as parent."""
    t = newText(t, font=f, parent=page, conditions=c, stroke=(0, 0, 1), strokeWidth=1,
        margin=GUTTER)
    t.showOrigin = True
    return t

#for contextName in ('Flat',):
for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
