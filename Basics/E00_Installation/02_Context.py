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
#    02_Contexts.py
#

from pagebot import getContext
context = getContext()
print(context)
context = getContext('DrawBot')
print(context)
context = getContext('Flat')
print(context)
context = getContext('Html')
print(context)
context = getContext('svg')
print(context)
