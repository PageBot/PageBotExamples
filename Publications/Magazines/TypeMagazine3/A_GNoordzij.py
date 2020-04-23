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
#     A_Gerrit_Noordzij.py
#
#     Proof of concept to re-generate the existing InDesign layouts as PDF.
#
from pagebot.elements import *
from pagebot.toolbox.units import inch

from metrics import *

SHOW_TEMPLATE = True

TEMPLATE_PDF = '../../../Design_TYPE-3/Noordzij_Layout-02_rb_TYPE-3.pdf'
TEMPLATE_PDF = '../Dropbox/Production_TYPE-3/2_Layouts__TYPE-3/People_Layout-01_rb_TYPE-3.pdf'
TEMPLATE_PDF = '/Users/petr/Dropbox/Production_TYPE-3/2_Layouts__TYPE-3/People_Layout-01_rb_TYPE-3.pdf'

def compose_Gerrit_Noordzij(magazine, part, doc):
    """This function builds the elements and layout of the Gerrit Noordzij article
    in TypeMagazine3.
    """
    if SHOW_TEMPLATE:
        index = 0
        for page in part.elements:
            page.size = doc.size
            doc.appendPage(page)
            if page.isPage:
                bgi = newImage(TEMPLATE_PDF, z=-10, parent=page, index=index//2)#, conditions=[Fit()])
                bgi.size = page.w*2, page.h
                if page.isRight:
                    bgi.x -= page.w
                index += 1

    #print(part, doc)
