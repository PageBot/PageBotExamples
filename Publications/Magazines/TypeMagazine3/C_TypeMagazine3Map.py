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
#     C-TypeMagazine3 Map.py
#
#     Proof of concept to re-generate the existing InDesign layouts as PDF.
#
from map import magazine

# 4 columns, 7 rows.
magazine.exportMap(cols=1, maxSpread=28, showGrid=True, showPadding=True)
