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
	os.path.mkdir(EXPORT_PATH)

import E00_BabelString
import E00_Text
import E00_TextA1
import E00_TextA3Box
import E00_TextA3BoxGrid
import E00_TextAlignment
import E00_TextAlignment2
import E00_TextBoxAlignment
import E00_TextLinesAlignment
import E00_TextMarginPadding
import E00_TextPosition
import E08_CJKBabelString

import E10_BabelStringContexts
#import E10_BabelStringFromSketch
import E10_BabelStringTabs

import E30_ContextTextLines
import E30_ElasticText
import E30_HyphenatedColumn

import E70_AlterGlyphCoordinates
import E70_FindFonts
