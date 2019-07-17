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

from pagebotcocoa.contexts.drawbot.context import DrawBotContext
from pagebot.contexts.flat.context import FlatContext
#from pagebot.contexts.indesigncontext import InDesignContext
#from pagebot.contexts.htmlcontext import HtmlContext
#from pagebot.contexts.svgcontext import SvgContext
#from pagebot.contexts.idmlcontext import IdmlContext
from pagebot.document import Document
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.strings.babelstring import BabelString
from pagebotcocoa.contexts.drawbot.string import DrawBotString
from pagebot.contexts.flat.flatstring import FlatString
from pagebot.toolbox.units import pt
from pagebot.toolbox.color import noColor, color
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.constants import *
from random import random

W, H = A5
H = pt(H)
W = pt(W)
M = 100
s = 36

roboto = findFont('Roboto-Regular')
robotoBold = findFont('Roboto-Bold')
bungee = findFont('BungeeHairline-Regular')

blurb = Blurb()
txt = blurb.getBlurb('news_headline', noTags=True)

testContexts = (
    (DrawBotContext(), '_export/testDrawBotString.pdf'),
    #(FlatContext(), '_export/testFlatString.pdf'),
    #(InDesignContext(), '_export/testInDesignString.pdf'),
    #(HtmlContext(), '_export/testHtmlString.pdf'),
    #(InDesignContext(), '_export/testInDesignString.pdf'),
    #(IdmlContext(), '_export/testIdmlString.pdf')
)

def testDocument(context):
    doc = Document(w=W, h=H, context=context)
    print('# Document in %s is %s' % (context, doc))
    return doc

def testPages(doc):
    page = doc[1]
    print('Current page: %s' % page)
    nextPage = page.next
    print('Next page: %s' % nextPage)
    print(type(page))
    print(doc.pages)

def testUnits(context):
    print('Units: %s' % context.units)


def testElements(page):
    conditions = [Right2Right(), Float2Top(), Float2Left()]

    for n in range(10):
        newLine(x=100, y=n*100, parent=page, stroke=0)

    '''
    for n in range(10):
        newRect(w=40, h=42, mr=4, mt=4, parent=nextPage,
                fill=color(random()*0.5 + 0.5, 0, 0.5),
                conditions=conditions)
    score = nextPage.solve()
    #print(score)
    '''

def build(doc):
    doc.build() # Export?

def test():
    for context, path in testContexts:
        doc = testDocument(context)
        testUnits(context)
        testPages(doc)
        # TODO: maybe make this work?
        #page = doc.pages[-1]
        page = doc.pages[1]
        print(page)
        print(type(page))
        #testElements(page)
        build(doc)

test()
