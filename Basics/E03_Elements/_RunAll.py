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

import AlignFloatElements
import Distance2Grid
import DrawRedRectCenterPage
import ElementBleedConditions
import ElementPaddingConditions
import ElementPaddingConditions2
import ElementPaddingMargin
import ElementPaddingPositions
import ElementSideConditions
import FloatElementsOnPage
import Images
import Shapes
import TextAllBaselineConditions
import TextAllPaddingConditions
import TextAllSideConditions
import TextBaselinePaddingMargin
import TextSideConditions
import TextSideConditions2
import TextSideWHConditions
import Texts
import UseBorders
import UseContainerElements
import UseDocWrap
import UseElementProperties
import UseShadow
