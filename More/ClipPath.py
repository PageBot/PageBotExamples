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
#     06_ClipPath.py
#
#     Shows how to get different types of contexts.
#     This example works on context level of direct drawing
#     not using the typical Element-based layout of PageBot.

from pagebot import getContext

def setClipPath():
    context = getContext()
    context.fill((0, 1, 1))
    context.rect(80, 80, 400, 400)
    path = context.newPath()
    path.moveTo((100, 100))
    path.lineTo((100, 150))
    path.lineTo((200, 200))
    path.lineTo((200, 150))
    path.lineTo((100, 150))
    path.closePath()

    # This changes the clip path:

    context.save()
    context.clipPath(path)
    context.fill((1, 0, 0, 0.9))
    context.rect(150, 150, 600, 600)
    context.restore()

    context.fill((1, 1, 0, 0.8))
    context.rect(400, 20, 300, 400)

setClipPath()
