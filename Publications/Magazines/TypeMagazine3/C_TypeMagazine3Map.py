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
#     C-TypeMagazine3 Map.py
#
#     Proof of concept to re-generate the existing InDesign layouts as PDF.
#
from map import magazine

# 4 columns, 7 rows.
magazine.exportMap(cols=1, maxSpread=28, showGrid=True, showPadding=True)
