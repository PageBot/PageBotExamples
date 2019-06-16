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
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     04_Units.py
#     See pagebot.toolbox.units for example docstring too.
#
from pagebot.toolbox.units import Unit, mm, px, pt, fr, em, perc, col, units

def useUnits():
    # 2mm, 2
    for v in mm(2), px(5), pt(5), em(12, base=10), perc(12.5, base=400), col(1/4, base=mm(200), g=mm(4)):
        # Showing the unit as instance and as rendered value
        print('As unit:', v, 'As raw value:', v.rv, 'As pt:', v.pt, ) 
    # TODO: etc...

useUnits()
