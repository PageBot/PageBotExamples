#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     Documents.py
#
#     Pagebot documents tests. Should become unit tests when finished.
from random import random
import traceback

from pagebot import getContext
from pagebot.document import Document
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.units import pt
from pagebot.toolbox.color import noColor, color
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.constants import *
#from pagebot.contexts.basecontext.babelstring import BabelString
#from pagebot.contexts.flat.flatstring import FlatString
#from pagebotosx.contexts.drawbot.drawbotstring import DrawBotString

W, H = A5
H = pt(H)
W = pt(W)
M = 100
SQ = 50
s = 36

roboto = findFont('Roboto-Regular')
robotoBold = findFont('Roboto-Bold')
bungee = findFont('BungeeHairline-Regular')

blurb = Blurb()
txt = blurb.getBlurb('news_headline', noTags=True)

def testDocument(context):
    doc = Document(w=W, h=H, context=context)
    print(' - Document in %s is %s' % (context, doc))
    return doc

def testPages(doc):
    page = doc[1]
    print(' - %s' % 'Current page: %s' % page)
    nextPage = page.next
    print(' - %s' % 'Next page: %s' % nextPage)
    print(' - %s' % type(page))
    print(' - %s' % doc.pages)
    new_page = newPage()
    print(' - new page %s' % new_page)
    print(' - %s' % doc.pages)

def testElements(context, page):
    """
    Functions to be tested:

    def newView(viewId, **kwargs):
    def newPage(**kwargs):
    def newTemplate(**kwargs):
    def newPlacer(**kwargs):
    def newColumn(**kwargs):
    def newTextBox(bs='', **kwargs):
    def newText(bs='', **kwargs):
    def newRect(**kwargs):
    def newQuire(**kwargs):
    def newArtboard(**kwargs):
    def newGroup(**kwargs):
    def newOval(**kwargs):
    def newCircle(**kwargs):
    def newLine(**kwargs):
    def newPolygon(points=None, **kwargs):
    def newRuler(**kwargs):
    def newPageBotPath(**kwargs):
    def newPaths(paths=None, **kwargs):
    def newImage(path=None, **kwargs):
    def newTable(cols=1, rows=1, **kwargs):
    def newGalley(**kwargs):
    """

    # Conditions.
    c = [Right2Right(), Float2Top(), Float2Left()]

    from pagebot.elements.views import viewClasses

    # Testing newView().

    for viewID in viewClasses:
        view = newView(viewID)
        print(' - %s' % view)

    # Testing newPage().

    new_page = newPage()
    print(' - new page %s' % new_page)

    oval = newOval(w=SQ, h=SQ, parent=page, conditions=c, fill=(1, 0, 0), stroke=0)
    print(' - new oval %s' % oval)

    circle = newCircle(w=SQ, h=SQ, parent=page, conditions=c, fill=(1, 0, 0), stroke=0)
    print(' - new circle %s' % circle)

    for n in range(10):
        col = color(random()*0.5 + 0.5, 0, 0.5)
        newRect(w=SQ, h=SQ, mr=4, mt=4, parent=page, fill=col, conditions=c)

    # Testing new Line)
    # FIXME: no output in Flat.

    for n in range(10):
        newLine(x=100, y=n*100, parent=page, stroke=0)

    testTextBox(context, page)

    score = page.solve()
    print(' - %s' % score)


def testTextBox(context, page):

    style = dict(font=bungee, fontSize=pt(32), baselineShift=6)
    bs = context.newString(txt, style=style)

    tb = newTextBox(bs, context=context, x=M, y=H-10*M, w=W/2, h=300,
            parent=page, stroke=color(0.3, 0.2, 0.1, 0.5),
            style=dict(hyphenation=True, language='en', leading=200))


def build(doc):
    doc.build() # Export?

def export(context):
    context.saveDrawing('_export/Test-Documents-%s.pdf' % context.name)

def test():
    objs = {}
    testContexts = {}

    for contextName in ('DrawBot', 'Flat'):
        testContexts[contextName] = getContext(contextName)

    for contextName, context in testContexts.items():
        print('* %s' % contextName)
        objs[contextName] = {}
        print(' - Units: %s' % context.units)

        doc = testDocument(context)
        objs[contextName]['doc'] = doc

    for contextName, context in testContexts.items():
        doc = objs[contextName]['doc']
        testPages(doc)

    for contextName, context in testContexts.items():
        print(contextName)
        doc = objs[contextName]['doc']

        # TODO: maybe make this work?
        #page = doc.pages[-1]
        page = doc.pages[1][0]
        print(' - %s' % page)
        print(' - %s' % type(page))

        try:
            testElements(context, page)
        except:
            'Error running testElements for context %s' % context
            print(traceback.format_exc())

    for contextName, context in testContexts.items():
        doc = objs[contextName]['doc']
        try:
            build(doc)
            export(context)
        except:
            msg = '!!!Error buiding and exporting context %s' % context
            print(msg)
            print(traceback.format_exc())
            break

test()
