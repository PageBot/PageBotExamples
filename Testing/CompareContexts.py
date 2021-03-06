#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T  E X A M P L E S
#
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     ComparePageBotDrawBot.py
#

import drawBot
import math, os, random
import inspect
from pagebot import getContext

flatContext = getContext('Flat')

attrs = []

for k in flatContext.__dict__.keys():
    if not (k in math.__dict__ or k in os.__dict__ or k in random.__dict__):
        attrs.append(k)

print(attrs)

'''
print('Not in PageBot')

base = DrawBotContext.__mro__[1]
d = DrawBotContext.__dict__
bd = base.__dict__

for a in attrs:
    if a not in d.keys() and a not in bd.keys():
        print('* %s' % a)

print('Not in DrawBot')

for k in DrawBotContext.__dict__.keys():
    if k not in attrs:
        print('* %s' % k)
'''
