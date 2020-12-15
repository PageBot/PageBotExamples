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
# Draw Wiggles using Drawbot:
# TODO: convert to PageBot script.
#
# Original script by Roberto Arista, you can find the related tutorial here:
# https://medium.com/@roberto_arista/how-to-draw-a-wiggle-between-two-points-with-python-and-drawbot-788006c18fb0

### Modules
from math import radians, atan2, sqrt, sin, cos
from collections import namedtuple


### Constants
BLACK = (0, 0, 0)
Point = namedtuple('Point', ['x', 'y'])


### Function & procedures
def calcAngle(pt1, pt2):
    return atan2((pt2.y - pt1.y), (pt2.x - pt1.x))


def calcDistance(pt1, pt2):
    return sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2)


def calcWiggle(pt1, pt2, waveLength, waveHeight, curveSquaring=.57):
    assert 0 <= curveSquaring <= 1, 'curveSquaring should be a value between 0 and 1: {}'.format(curveSquaring)
    assert waveLength > 0, 'waveLength smaller or equal to zero: {}'.format(waveLength)

    diagonal = calcDistance(pt1, pt2)
    angleRad = calcAngle(pt1, pt2)

    howManyWaves = diagonal//int(waveLength)
    waveInterval = diagonal/float(howManyWaves)
    maxBcpLength = sqrt((waveInterval/4.)**2+(waveHeight/2.)**2)
    bcpLength = maxBcpLength*curveSquaring
    bcpInclination = calcAngle(Point(0,0), Point(waveInterval/4., waveHeight/2.))

    wigglePoints = [pt1]
    prevFlexPt = pt1
    polarity = 1
    for waveIndex in range(0, int(howManyWaves*2)):
        bcpOutAngle = angleRad+bcpInclination*polarity
        bcpOut = Point(prevFlexPt.x+cos(bcpOutAngle)*bcpLength, prevFlexPt.y+sin(bcpOutAngle)*bcpLength)

        flexPt = Point(prevFlexPt.x+cos(angleRad)*waveInterval/2., prevFlexPt.y+sin(angleRad)*waveInterval/2.)

        bcpInAngle = angleRad+(radians(180)-bcpInclination)*polarity
        bcpIn = Point(flexPt.x+cos(bcpInAngle)*bcpLength, flexPt.y+sin(bcpInAngle)*bcpLength)

        wigglePoints.append((bcpOut, bcpIn, flexPt))

        polarity *= -1
        prevFlexPt = flexPt

    return wigglePoints

def drawCurvesSequence(wigglePoints):
    myBez = BezierPath()
    myBez.moveTo(wigglePoints[0])
    for eachBcpOut, eachBcpIn, eachAnchor in wigglePoints[1:]:
        myBez.curveTo(eachBcpOut, eachBcpIn, eachAnchor)
        print(eachBcpOut, eachBcpIn, eachAnchor)
    myBez.endPath()
    for contour in myBez:
        for seg in contour:
            print(seg)
    drawPath(myBez)


### Variables
pt1 = Point(0, 0)
pt2 = Point(100, 100)

### Instructions
size(400, 400)

oval(pt1.x-1, pt1.y-1, 2, 2)
oval(pt2.x-1, pt2.y-1, 2, 2)

stroke(*BLACK)
strokeWidth(.5)
fill(None)

wigglePoints = calcWiggle(pt1, pt2, 16, 36, .7)
drawCurvesSequence(wigglePoints)
