#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     JSON.py
#

import traceback
from random import random
from pagebot import getAllContexts, getResourcesPath
from pagebot.toolbox.color import Color
from pagebot.constants import A4Rounded
from pagebot.contexts.base.babelstring import BabelString
from pagebot import getContext
from pagebot.toolbox.units import pt
from pagebot.document import Document
from pagebot.fonttoolbox.objects.font import findFont
#H, W = A4Rounded
#W = pt(W)
#H = pt(H)

#f = Color(0, 0, 0)
#s = Color(1, 0, 0)

def loadJSON():
    pass

def testContexts():
    contexts = getAllContexts()
    print('All contexts: %s' % contexts)

    for i, c in enumerate(contexts):
        if i in (0, 1):
            try:
                testContext(c)
            except Exception as e:
                    print('Context errors', traceback.format_exc())

#testContexts()
loadJSON()
