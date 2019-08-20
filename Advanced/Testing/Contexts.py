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
#     Contexts.py
#

import traceback
from random import random
from pagebot import getAllContexts, getResourcesPath
from pagebot.toolbox.color import Color
from pagebot.constants import A4Rounded
from pagebot.strings.babelstring import BabelString
from pagebot import getContext
from pagebot.toolbox.units import pt
from pagebot.document import Document

H, W = A4Rounded
W = pt(W)
H = pt(H)

f = Color(0, 1, 0)
s = Color(1, 0, 0)

def testContexts():
    contexts = getAllContexts()
    print('All contexts: %s' % contexts)

    for i, c in enumerate(contexts):
        if i in (0, 1):
            #print(c)
            testContext(c)

def getRandom():
    x = (W - 100) * random()
    y = (H - 100) * random()
    return x, y

def testContext(context):
    print('Context', context)

    doc = Document(w=W, h=H, context=context, autoPages=1)


    '''
    print('# Context attributes')

    for key, value in context.__dict__.items():
        print(' * %s: %s' % (key, value))

    print('# Document attributes')
    for key, value in doc.__dict__.items():
        print(' * %s: %s' % (key, value))
    '''


    try:
        sq = 100
        context.frameDuration(1)
        context.newDrawing()
        context.newPage(w=W, h=H)
        context.fill(f)
        context.stroke(s)
        x = 0
        y = 0
        #context.rect(x, y, pt(sq), pt(sq))
        y += sq

        #context.oval(x, y, pt(sq), pt(sq))
        y += sq

        context.circle(x, y, pt(sq))
        y += sq
        '''

        bla = context.newString('BabelString No Style')
        print('String is BabelString', isinstance(bla, BabelString))
        context.text(bla, pt(x, y))
        y += sq
        context.text('plain string', pt(x, y))
        y += sq

        style = {'font': 'Helvetica', 'textFill': f}
        bla = context.newString('Babel String with Style', style=style)
        context.text('bla2', pt(x, y))
        y += sq

        context.text(bla, pt(x, y))
        x = sq
        y = sq

        path = getResourcesPath() + "/images/cookbot1.jpg"
        context.image(path, p=pt(0, 0), w=pt(100), h=pt(100))

        '''

        # TODO:
        # - test Bézier path
        # - test glyph path
        # - test elements
        # ...
        path = '_export/%s.pdf' % context.name
        context.saveImage(path)
        print('Saved context to %s' % path)
    except Exception as e:
    	    print('Context errors', traceback.format_exc())

def showContexts():
	context = getContext() # Creates a DrawBot context on Mac, Flat on others
	print('Context is', context)

	context = getContext() # Still DrawBot, takes the buffered DEFAULT_CONTEXT.
	print('DrawBot context?', context)

	context = getContext(contextType='Flat') # Force Flat.
	print('Flat context?', context)

	context = getContext(contextType='Flat') # Buffered in DEFAULT_CONTEXT this time.
	print('Flat context?', context)
	#context = getContext(contextType='HTML')
	#print('HTML context?', context)
	#context = getContext(contextType='InDesign')
	#print('InDesign context?', context)
	#context = getContext(contextType='IDML')
	#print('IDML context?', context)
	#context = getContext(contextType='SVG')
	#print(context)

#showContexts()
testContexts()
