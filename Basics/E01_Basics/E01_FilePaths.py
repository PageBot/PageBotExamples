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
    c = (Float2Left(), Float2Top())
    # FIXME: causes single line textboxes to have too much bottom padding in Flat.
    # Fit2Right()

    # Find the demo font, as supplied with the Roboto library installation.
    # This is a subset of TYPETR Upgrade Regular.

    rootPath = getRootPath() # Location of this Roboto library
    style = dict(fontSize=fontSize, font=font, leading=leading)
    msg = 'Root path is %s' % rootPath
    bs = context.newString(msg, style)
    w = W / 2 - 2*GUTTER
    h = H / 2 - 2*GUTTER
    topText1 = makeText(bs, page, font, c, w=w, h=h)

    resourcesPath = getResourcesPath()
    msg = 'Resources path is %s' % resourcesPath
    bs = context.newString(msg, style)
    topText2 = makeText(bs, page, font, c, w=w, h=h)

    msg = 'Default font path is %s' % font.path
    msg = '\n • '.join(msg.split('/'))
    bs = context.newString(msg, style)
    #c = (Right2Right(), Float2Top())
    column1 = makeText(bs, page, font, c, w=w, h=h)

    # Forces column width, so second column isn't pushed away.
    #column1.w = page.pw / 2 - 2*GUTTER
    #column1.mr = 0

    msg = 'Roboto font path is %s' % font.path
    msg = '\n • '.join(msg.split('/'))
    bs = context.newString(msg, style)
    #c = (Left2Left(), Float2Top())
    column2 = makeText(bs, page, font, c, w=w, h=h)

    # Let the page solve all of its child element layout conditions.
    page.solve()
    doc.export(exportPath)

def makeText(t, page, f, c, w=None, h=None):
    """Create a new text box with e give layout conditions
    and with page as parent."""
    t = newText(t, font=f, w=w, h=h, parent=page, conditions=c, strokeWidth=1,
        margin=0, showFrame=True, showDimensions=True, showOrigin=True)
    #t.showOrigin = True
    return t

#for contextName in ('Flat',):
for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
