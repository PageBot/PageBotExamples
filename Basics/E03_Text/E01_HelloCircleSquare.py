#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E01_HelloCircleSquare.py
#
from random import random
from pagebot import getContext

for contextName in ('DrawBot', 'Flat'):
    context = getContext(contextName)

    for extension in ('png', 'jpg', 'pdf'):
        exportPath = '_export/01_HelloCircleSquare-%s.%s' % (contextName, extension)

        context.newPage(1000, 1000)
        for n in range(150):
            # FIXME: transparancy does not work in FlatContext
            context.fill((random(), 0, random(), 0.5 + random()*0.2))
            ch = random()
            x = 20 + random()*800
            y = 20 + random()*800
            if ch < 0.2:
                context.oval(x, y, 80, 80 )
            elif ch < 0.4:
                context.rect(x, y, 80, 80 )
            else:
                bs = context.newString('Hello world on %d,%d' % (x, y),
                                 style=dict(fontSize=24))
                context.drawString(bs, (x, y))

        context.saveImage(exportPath)

print('Done')