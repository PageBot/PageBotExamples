#!/usr/bin/env python
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
#     A_Firsts.py
#
#     Proof of concept to re-generate the existing InDesign layouts as PDF.
#
from pagebot.elements import *
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.units import inch, em, pt
from pagebot.toolbox.color import color
from pagebot.constants import LEFT, RIGHT
from pagebot.conditions import *

from metrics import *

SHOW_TEMPLATE = True

TEMPLATE_PDF = '../../../Design_TYPE-3/Noordzij_Layout-02_rb_TYPE-3.pdf'
TEMPLATE_PDF = '../Dropbox/Production_TYPE-3/2_Layouts__TYPE-3/People_Layout-01_rb_TYPE-3.pdf'
TEMPLATE_PDF = '/Users/petr/Dropbox/Production_TYPE-3/2_Layouts__TYPE-3/People_Layout-01_rb_TYPE-3.pdf'

titleBold = findFont('Upgrade-Bold')
titleSemibold = findFont('Upgrade-Semibold')
titleRegular = findFont('Upgrade-Regular')
titleFont = findFont('Upgrade-Thin')
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
    h2=dict(name='h2', font=titleBold, fontSize=36, uppercase=True, textFill=color(rgb=0x676A6A)),
    h3=dict(name='h3', font=headline2, fontSize=16),
    p=dict(name='p', font=bodyText, fontSize=12, leading=em(1.4)),
    b=dict(name='b', font=bosyTextBold, fontSize=12, leading=em(1.4)),
    i=dict(name='i', font=bodyTextItalic, fontSize=12, leading=em(1.4)),
    
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

def composeBase(magazine, part, doc, page, index):
    # Page numbers
    dy1 = BASELINE+pt(4)
    dy2 = BASELINE
    if page.isLeft:
        bs = doc.context.newString('FALL 2018', style=styles['typeTitleRight'])
        newTextBox(bs, w=magazine.cw, h=page.pb-dy1, parent=page, conditions=[Bottom2SideBottom(), Right2Right()], 
            bleed=0)
        bs = doc.context.newString(page.pn[0], style=styles['pnLeft'])
        newTextBox(bs, w=magazine.cw, h=page.pb-dy2, parent=page, conditions=[Bottom2SideBottom(), Left2Left()], 
            bleed=0)
    else:
        bs = doc.context.newString('TYPE No. 3', style=styles['typeTitleLeft'])
        newTextBox(bs, w=magazine.cw, h=page.pb-dy1, parent=page, conditions=[Bottom2SideBottom(), Left2Left()], 
            bleed=0)
        bs = doc.context.newString(page.pn[0], style=styles['pnRight'])
        newTextBox(bs, w=magazine.cw, h=page.pb-dy2, parent=page, conditions=[Bottom2SideBottom(), Right2Right()], 
            bleed=0)
  
def composePeopleTitleLeft(magazine, part, doc, page, index):
    newTextBox(parent=page, x=page.pl, y=page.pb, w=page.pw, h=page.ph, fill=(0, 0, 1, 0.5))

def composePeopleTitleRight(magazine, part, doc, page, index):
    newTextBox(parent=page, x=page.pl, y=page.pb, w=page.pw, h=page.ph, fill=(0, 1, 1, 0.5))

def composePeopleTitle(magazine, part, doc, page, index):
    newTextBox(parent=page, x=page.pl, y=page.pb, w=page.pw, h=page.ph, fill=(1, 0, 1, 0.5))

def compose_People(magazine, part, doc):
    """This function builds the elements and layout of the People article
    in TypeMagazine3.
    """
    index = 2
    for page in part.elements:
        page = page.copy()
        page.size = doc.size
        doc.appendPage(page)
        if page.isPage:
            if page.isLeft:
                page.padding = PADDING_LEFT
            else:
                page.padding = PADDING_RIGHT

            if SHOW_TEMPLATE:
                bgi = newImage(TEMPLATE_PDF, z=-10, parent=page, index=index//2)#, conditions=[Fit()])
                bgi.size = page.w*2, page.h
                if page.isRight:
                    bgi.x -= page.w

            composeBase(magazine, part, doc, page, index)
            index += 1

    #print(part, doc)
