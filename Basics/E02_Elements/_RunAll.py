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
# 	  Run all exmples in thes directory, creating the output in _export
#     (Note that the content of the _export directory does not commit to Github)
#
import os

EXPORT_PATH = '_export'
if not os.path.exists(EXPORT_PATH):
	os.mkdir(EXPORT_PATH)

import E01_ElementPaddingConditions
import E02_ElementSideConditions
import E03_ElementPaddingPositions
import E04_TextSideConditions
import E05_ElementPaddingMargin
import E06_FloatElementsOnPage
import E07_Images
import E08_Shapes
import E09_TextAllBaselineConditions
import E10_TextAllPaddingConditions
import E11_TextAllSideConditions
import E12_TextBaselinePaddingMargin
import ElementBleedConditions
import ElementPaddingConditions2
