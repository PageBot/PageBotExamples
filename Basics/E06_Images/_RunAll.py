#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#

#     www.pagebot.io
#     Licensed under MIT conditions
#


# -----------------------------------------------------------------------------
#
# 	  Run all exmples in thes directory, creating the output in _export
#     (Note that the content of the _export directory does not commit to Github)
#
import os

EXPORT_PATH = '_export'
if not os.path.exists(EXPORT_PATH):
	os.path.mkdir(EXPORT_PATH)

import E01_CacheScaledImage
import E02_ScaleAnImage
import E03_ImageAlignment
import E04_ImageElements
import E05_ImageCondition
import E06_ImageClipping
import E07_ImageClippingValues
