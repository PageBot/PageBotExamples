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
#     A_Front.py
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

def compose_Front(magazine, part, doc):
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

            index += 1

    #print(part, doc)
