#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     www.pagebot.io
#     Licensed under MIT conditions
#
# -----------------------------------------------------------------------------
#
#     E21_UseContainerElements.py
#
#     Container element hold an ordered list of elements.
#     Each element knows its own position.
#

from pagebot import getContext
from pagebot.constants import EXPORT
from pagebot.document import Document
from pagebot.elements import newRect
from pagebot.toolbox.transformer import path2FileName

W = H = 1000
FILENAME = path2FileName(__file__)

def draw(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    doc = Document(w=W, h=H, context=context)
    page = doc[1]
    c = newRect(parent=page, name='myContainerElement',
        x=100, y=100, w=page.w/2, h=page.h/2, fill=(1, 0, 0))

    print('Container we made:'+str(c))
    print('No elements yet:'+str(c.elements)) # Currently no elements in the container
    child1 = newRect(parent=c, name='Child1', fill=(1, 1, 0)) # Make child containers with unique Id
    child2 = newRect(parent=c, name='Child2', fill=(1, 0, 1))
    # Get unique element eIds
    eId1 = child1.eId
    eId2 = child2.eId
    print('-- Now the container got 2 named child containers.')
    print('Elements:'+str(c.elements)) # Currently no elements in the container
    print('-- None of the children are placed on default position (0, 0, 0)')
    for e in c.elements:
        print(e.name, e.x, e.y, e.z)
    print('-- Place the Child1 element on a fixed position (x,y), z is undefined/untouched')
    child1.x = 20
    child1.y = 30
    child1.z = 100
    print(child1)
    print('-- Place the same Child2 element on another fixed position (x,y,z), a point tuple.')
    child2.point = (120, 30, 20)
    print(child2)
    print('-- The container behaves as a dictionary of child elements with e.eId as key.')
    print(c[eId1])
    print(c[eId2])
    page.solve()
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    draw(contextName)
