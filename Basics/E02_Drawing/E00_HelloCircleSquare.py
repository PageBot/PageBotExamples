#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E00_HelloCircleSquare.py
#

import sys
from random import random
from pagebot import getContext
from pagebot.toolbox.units import *
from pagebot.toolbox.color import color

context = getContext('DrawBot')

for p in range(10):
    context.newPage(pt(1000), pt(1000))
    for n in range(50):
        col = color(random(), 0, random(), 0.5 +random()*0.2)
        context.fill(col)
        ch = random()
        x = 20 + random()*800
        y = 20 + random()*800
        

        if ch < 0.2:
            context.oval(pt(x), pt(y), pt(80), pt(80))
        elif ch < 0.4:
            context.rect(pt(x), pt(y), pt(80), pt(80))
        else:
            context.fontSize(pt(24))
            context.drawString('Hello world on %d,%d' % (x, y), (x, y))
            
context.saveImage('_export/E00_HelloCircleSquare.gif')

