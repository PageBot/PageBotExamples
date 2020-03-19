#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     01 00-00-Type3-Template.py
#
#     Proof of concept to re-generate the existing InDesign layouts as PDF.
#
import os
from random import random # Used for random color palet.

from pagebot import getContext
context = getContext('DrawBot')

# Create random title and names
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.toolbox.color import color, blackColor
from pagebot.toolbox.dating import now

# Get function to find the Roboto family (in this case installed in the
# PageBot repository).
from pagebot.fonttoolbox.objects.family import getFamily
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.color import noColor, blackColor
# Creation of the RootStyle (dictionary) with all
# available default style parameters filled.
from pagebot.style import getRootStyle

# Document is the main instance holding all information
# about the document togethers (pages, styles, etc.)
from pagebot.document import Document
from pagebot.typesetter import Typesetter
from pagebot.composer import Composer

# Import element layout conditions.
from pagebot.conditions import *
from pagebot.elements import newRect, newTextBox, newImage, Galley
from pagebot.toolbox.units import units, p, pt, em, inch
from pagebot.constants import (GRID_COL, GRID_ROW, GRID_SQR, LEFT, RIGHT,
    CENTER, MIDDLE, TOP, RIGHT, INLINE, OUTLINE, ONLINE)

from map import magazine

# For clarity, most of the MakeABookCover.py example document is setup
# as a sequential excecution of Python functions. For complex documents
# this is not the best method. More functions and classes will be used in the
# real templates, which are available from the PageBotTemplates repository.

W, H = inch(8, 10.875)
BLEED_LEFT = p(1), 0, p(1), p(1) # 1 Pica bleed on top, left bottom
BLEED_RIGHT = p(1), p(1), p(1), 0 # 1 Pica bleed in top, right, bottom
GUTTER = p(2)
LM, RM = p(5, 6)
CW = (W - LM - RM - 3*GUTTER) / 4
CH = p(5.5)
BASELINE = pt(12)
BASELINE_START = pt(44)

CONTENT_PATH = 'Firsts.md'
#CONTENT_PATH = 'People-TEST.md'
TEMPLATE_PDF = '../../../Design_TYPE-3/Firsts_Layout-01_rb_TYPE-3.pdf'
EXPORT_PDF = True
EXPORT_PNG = True

startPage = 58
endPage = 73

CC = noColor #color(1, 0, 0)

# Export in folder that does not commit to Git. Force to export PDF.
EXPORT_PATH_PDF = '_export/%d-%02d-%02d-%02d-P%d-P%d-Type3-Firsts.pdf'
EXPORT_PATH_PNG = '_export/P%d-P%d-Type3-Firsts.png'

BOX_NAME = 'Article'
SHOW_TEMPLATE = True
SHOW_CONTENT = True

titleBold = boldFont = findFont('Upgrade-Bold')
titleSemibold = findFont('Upgrade-Semibold')
titleRegular = findFont('Upgrade-Regular')
titleFont = findFont('Upgrade-Thin')
lightFont = findFont('Upgrade-Light')
bookFont = findFont('Upgrade-Book')

headline = findFont('Upgrade-Medium')
headline2 = findFont('Upgrade-Regular')
headlineItalic = findFont('Upgrade-Italic')
bodyText = findFont('Proforma-Book')
bosyTextBold = findFont('Proforma-Semibold')
bodyTextItalic = findFont('Proforma-BookItalic')

headline = findFont('PageBot-Light')

styles = dict(
    h1=dict(name='h1', font=titleBold, fontSize=48),
    h2=dict(name='h2', font=titleBold, fontSize=36, uppercase=True, textFill=color(rgb=0x676A6A), leading=em(0.8)),
    h3=dict(name='h3', font=bookFont, fontSize=11, leading=em(1.3)),
    p=dict(name='p', font=titleSemibold, fontSize=12, leading=em(1.3)),
    b=dict(name='b', font=bosyTextBold, fontSize=12, leading=em(1.3)),
    i=dict(name='i', font=bodyTextItalic, fontSize=12, leading=em(1.3)),

    pnLeft=dict(name='pnLeft', font=titleBold, fontSize=pt(14), xTextAlign=LEFT),
    pnRight=dict(name='pnRIght', font=titleBold, fontSize=pt(14), xTextAlign=RIGHT),

    title=dict(name='title', font=titleFont, fontSize=pt(100)),
    titleBold=dict(name='titleBold', font=titleBold, fontSize=pt(62)),
    lead=dict(name='lead', font=titleBold, fontSize=pt(18)),
    function=dict(name='function', font=bookFont, fontSize=pt(11)),
    functionName=dict(name='functionName', font=titleBold, fontSize=pt(12)),

    designerName=dict(name='designerName', font=titleBold, fontSize=pt(36)),
    designAnswer=dict(name='designAnswer', font=titleSemibold, fontSize=pt(12)),
    typeTitleLeft=dict(name='typeTitleLeft', font=titleRegular, fontSize=pt(9), xTextAlign=LEFT,
        tracking=em(0.05)),
    typeTitleRight=dict(name='typeTitleRIght', font=titleRegular, fontSize=pt(9), xTextAlign=RIGHT,
        tracking=em(0.05)),

)

def setPageStyle(page, index):
    if page.isLeft:
        page.bleed = BLEED_LEFT
        page.padding = '3p1.5', LM, '4p1.5', RM
    else:
        page.bleed = BLEED_RIGHT
        page.padding = '3p1.5', RM, '4p1.5', LM
    page.gridX = (CW, GUTTER), (CW, GUTTER), (CW, GUTTER), (CW, 0)
    page.gridY = (CH, GUTTER), (CH, GUTTER), (CH, GUTTER), (CH, GUTTER), (CH, GUTTER), (CH, GUTTER), (CH, GUTTER), (CH, 0)

    #newTextBox(parent=page, name=BOX_NAME, fill=0.9, nextElementName=BOX_NAME, bleed=0,
    #    conditions=[Fit()])

    if SHOW_TEMPLATE:
        bgi = newImage(TEMPLATE_PDF, z=-10, parent=page, index=index//2)#, conditions=[Fit()])
        bgi.size = inch(W*2, H)
        if page.isRight:
            bgi.x -= W

    # Page numbers
    dy1 = BASELINE+pt(4)
    dy2 = BASELINE
    if page.isLeft:
        bs = context.newString('FALL 2018', style=styles['typeTitleRight'])
        newTextBox(bs, w=CW, h=page.pb-dy1, parent=page, conditions=[Bottom2SideBottom(), Right2Right()],
            bleed=0)
        bs = context.newString(page.pn[0], style=styles['pnLeft'])
        newTextBox(bs, w=CW, h=page.pb-dy2, parent=page, conditions=[Bottom2SideBottom(), Left2Left()],
            bleed=0)
    else:
        bs = context.newString('TYPE No. 3', style=styles['typeTitleLeft'])
        newTextBox(bs, w=CW, h=page.pb-dy1, parent=page, conditions=[Bottom2SideBottom(), Left2Left()],
            bleed=0)
        bs = context.newString(page.pn[0], style=styles['pnRight'])
        newTextBox(bs, w=CW, h=page.pb-dy2, parent=page, conditions=[Bottom2SideBottom(), Right2Right()],
            bleed=0)

    path = '../../../Art_TYPE-3/Firsts_images_TYPE-3/1. page-number-printed-1470.pdf'
    if page.pn[0] == startPage:
        pass
    elif page.pn[0] == startPage+1:
        pass
    else:
        pass

    page.solve()

def makeDocument():
    """Re-generate the original Type3-PeopleInType chapter as PDF output."""

    context = DrawBotContext()

    # Create new document with (w,h) and fixed amount of pages.
    # Make number of pages with default document size.
    # Initially make all pages default with template
    # One page, just the cover.
    doc = Document(w=W, h=H, title='Type Magazine #3', autoPages=endPage - startPage + 1,
        baselineGrid=BASELINE, baselineStart=BASELINE_START, style=styles,
        startPage=startPage, context=context)

    # Get the current view of the document. This allows setting of
    # parameters how the document is represented on output.
    view = doc.view
    view.w, view.h = W, H
    # Set view options. Full list is in elements/views/baseviews.py
    view.padding = 40 # Showing cropmarks and registration marks
                      # need >= 20 padding of the view.
    view.showRegistrationMarks = True
    view.showCropMarks = True
    view.showFrame = True
    view.showPadding = True
    view.showNameInfo = True
    view.showMetaInfo = False
    view.showTextOverflowMarker = False
    view.showOrigin = False # Show origin marker
    view.showElementOrigin = False # Don't show the origin of other elements.

    view.showGrid = [GRID_COL, GRID_ROW]
    view.showBaselines = True

    view.showSpreadPages = True
    view.showSpreadMiddleAsGap = False

    # PageBot article
    _, backgroundHeight = context.imageSize(TEMPLATE_PDF)
    backgroundIndex = 2
    for pn in range(startPage, endPage + 1):
        page = doc[pn]
        setPageStyle(page, backgroundIndex)
        backgroundIndex += 1

    if SHOW_CONTENT:
        page = doc[startPage]
        t = Typesetter(context, styles=styles, imageAsElement=True)
        galley = t.typesetFile(CONTENT_PATH, e=page)
        composer = Composer(doc)
        targets = dict(composer=composer,
            doc=doc,
            page=page,
            style=doc.styles,
            box=page.select('people'),
            newTextBox=newTextBox)

        composer.compose(galley, targets=targets, page=page)

    date = now()
    if EXPORT_PDF: # Export as PDF
        exportPath = EXPORT_PATH_PDF % (date.year, date.month, date.day, date.hour, startPage, endPage)
        doc.export(exportPath)
    if EXPORT_PNG: # Export as PNG without cropmarks for mapping purpose
         doc.view.padding = 0
         exportPath = EXPORT_PATH_PNG % (startPage, endPage)
         doc.export(exportPath)

makeDocument()
