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
#     QuadraticPaths.py
#

from pagebot.constants import A4Rounded
from drawBot import BezierPath as DrawBotBezierPath
from pagebot.contexts.basecontext.basebezierpath import BaseBezierPath
from pagebot.contexts.basecontext.bezierpath import BezierPath
from pagebot import getAllContexts
from pagebot.toolbox.units import pt

H, W = A4Rounded
W = pt(W)
H = pt(H)

def testQuadraticPath(path):
    # Replicates FontTools BasePen test.

    #path.moveTo((0, 0))
    path.qCurveTo((0, 0), (0, 100), (100, 100), (100, 0), None)
    path.closePath()

def printQuadraticPath(path):

    for contour in path.contours:
        for i, segment in enumerate(contour):
            print("#%s: %s" % (i, segment))

    print(path.points)

def testQuadraticPaths():
    path = DrawBotBezierPath()
    testQuadraticPath(path)
    nsPath = path._path

    print("NSPath")
    count = nsPath.elementCount()
    points = []


    print("DrawBot: <BezierPath>")
    printQuadraticPath(path)

    contexts = getAllContexts()

    c = contexts[1]
    print(c)
    path = c.newPath()
    path.qCurveTo((0, 0), (0, 100), (100, 100), (100, 0), None)
    path.closePath()
    #printQuadraticPath(path)

    '''

    for i, c in enumerate(contexts):
        if i in (0, 1):
            path = c.newPath()
            print(path)
            testQuadraticPath(path)
            printQuadraticPath(path)
    '''

testQuadraticPaths()
