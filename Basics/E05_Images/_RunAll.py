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

# Simple image position, scaling and layout
import E00_ImagePosition
import E01_CacheScaledImage
import E01_ImageCondition
import E01_ImageElements
import E02_ImageAlignment

# Clipping images on bezierPath shapes.
import E05_ImageClipping

# Filters
#import E07_ImageObjectFilters