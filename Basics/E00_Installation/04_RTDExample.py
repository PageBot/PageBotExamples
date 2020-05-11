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
#    04_RTDExample.py
#

from pagebot.document import Document
from pagebot.elements import newRect
from pagebot.conditions import Center2Center, Middle2Middle
from pagebot.toolbox.units import pt
from pagebot.toolbox.color import color

W, H = pt(300, 200) # Get size units
doc = Document(w=W, h=H)
page = doc[1]
newRect(parent=page, fill=color('red'), size=pt(240, 140), showDimensions=True, conditions=[Center2Center(), Middle2Middle()])
page.solve()
doc.export('_export/RedSquare.png')
