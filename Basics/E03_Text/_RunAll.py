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

import E01_BabelString
import E02_Text
import E03_TextA1
import E04_TextA2
import E05_TextA2Lines
import E06_TextA3Box
import E07_Hkpx
import E08_CJKBabelString
import E09_TextA3BoxGrid
import E10_BabelStringTabs
import E11_TextAlignment
import E12_TextAlignment2
import E13_TextBoxAlignment
import E14_TextLinesAlignment
import E15_TextMarginPadding
import E16_TextPosition
import E17_ElasticText
import E18_Hyphenation
import E19_HyphenatedColumn
import E20_UseProofing
