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
#     MakeSamplePhotoBook.py
#
from pagebot import getContext
from pagebot.publications.books import PhotoBook

context = getContext('DrawBot')
bk = PhotoBook()
doc = bk.makeSample(context)
doc.export('_export/PhotoBookSample.pdf')

