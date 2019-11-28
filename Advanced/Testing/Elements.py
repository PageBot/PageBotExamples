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
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     TODO: Floating on second line does not seem to work currently

from pagebot.conditions import *
from pagebot import getContext
from pagebot.elements.element import Element

context = getContext()
#context = getContext('Flat')
context.newDrawing()
context.newPage()
e = Element(w=500, h=500, context=context)
print(' * Testing in %s' % context.name)
print(e)
print(e.childClipPath)
e1 = Element(parent=e, x=0, y=0, w=50, h=80)

# Flat not getting correct results due to missing boolean operators.
print(len(e.childClipPath)) # 7
print(len(e1.childClipPath)) # 7
print(e.childClipPath.points)
print(e1.childClipPath.points)
#[(50.0, 0.0), (500.0, 0.0), (500.0, 500.0), (0.0, 500.0), (0.0, 80.0), (50.0, 80.0), (50.0, 0.0)]
e = Element(w=500, h=500, context=context)
e1 = Element(parent=e, w=100, h=100, conditions=[Left2Left(), Top2Top()])
e2 = Element(parent=e, w=100, h=100, conditions=(Left2Left(), Bottom2Bottom()))
score = e.solve()
print(e.childClipPath.points)
#[(100.0, 0.0), (500.0, 0.0), (500.0, 500.0), (0.0, 500.0), (0.0, 100.0), (100.0, 100.0), (100.0, 0.0)]
print(e.childClipPath.__class__.__name__)
'PageBotPath'

