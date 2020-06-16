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
#     metrics.py
#
from pagebot.toolbox.units import inch, p, pt

W, H = inch(8, 10.875)
BLEED_LEFT = p(1), 0, p(1), p(1) # 1 Pica bleed on top, left bottom
BLEED_RIGHT = p(1), p(1), p(1), 0 # 1 Pica bleed in top, right, bottom
GUTTER = p(2)
ML, MR = p(5, 6)
CW = (W - ML - MR - 3*GUTTER) / 4
CH = p(5.5)
BASELINE = pt(12)
BASELINE_START = pt(44)

PADDING_LEFT = '3p1.5', ML, '4p1.5', MR
PADDING_RIGHT = '3p1.5', MR, '4p1.5', ML

GRIDX = (CW, GUTTER), (CW, GUTTER), (CW, GUTTER), (CW, GUTTER)
GRIDY = (CH, GUTTER), (CH, GUTTER), (CH, GUTTER), (CH, GUTTER), (CH, GUTTER), (CH, GUTTER), (CH, GUTTER), (CH, 0)
