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
#     UseTextFlows.py
#
#     If a Text such as self.nextElement is defined as name for another text
#     box on the same page, then overflow of self will go into the other text
#     box.

from pagebot.constants import LEFT, TOP, BOTTOM
from pagebot.conditions import *
from pagebot.elements import *
from pagebot.document import Document
from pagebot.toolbox.color import color, blackColor, whiteColor, noColor
from pagebot.toolbox.units import pt, em
from pagebot import getContext
from pagebot.fonttoolbox.objects.font import findFont

# Document is the main instance holding all information about the document
# togethers (pages, styles, etc.)

context = getContext('DrawBot')

font = findFont('Roboto-Regular')

DoTextFlow = True
PagePadding = 30
PageSize = 600
BoxWidth = PageSize - 2*PagePadding

# Export in _export folder that does not commit in Git. Force to export PDF.
EXPORT_PATH = '_export/UseTextFlows.png'

def makeDocument():
    """Make a new document."""

    W, H = PageSize, PageSize/2

    # Create a new document, default to the defined page size.
    doc = Document(w=W, h=H, title='Text Flow', autoPages=2, context=context)

    view = doc.getView()
    print(view.viewId, doc.views)
    view.padding = 30 # Avoid showing of crop marks, etc. when value = 0
    view.showCropMarks = True
    view.showRegistrationMarks = True
    view.showFrame = True
    view.showPadding = True
    view.showOrigin = True
    view.showDimensions = False
    view.showElementInfo = False

    # Get list of pages with equal y, then equal x.
    #page = doc[1][0] # Get the single page from te document.
    page1 = doc[1] # Get page on pageNumber, first in row (this is only one now).
    page1.name = 'Page 1'
    page1.padding = PagePadding



    s = ''
    for n in range(30):
        s += '(Line %d) %s\n' % (n+1, 'AAA ' * 40)
    style = dict(font=font, fontSize=12, textFill=color('red'), leading=14, firstLineIndent=20)
    bs = context.newString(s, style=style)
    h1 = 120 # Fox on a given height, to show the text flowing to the e2 element.

    e1 = newText(bs,
        name='Text1',
        nextElement='Text2', # Overflow goes here.
        parent=page1, padding=4, x=100, w=BoxWidth, h=h1,
        mb=20, mr=10, # Conditions make the element move to top-left of the page.
        # And the condition that there should be no overflow, otherwise the text box
        # will try to solve it.
        conditions=[Left2Left(), Top2Top(), Overflow2Next()],
        # Position of the origin of the element. Just to show where it is.
        # Has no effect on the position conditions.
        yAlign=BOTTOM, xAlign=LEFT,
        leading=em(1.4), fontSize=pt(9),
        textFill=blackColor,
        fill=0.9, # Renders to color
        stroke=noColor,
        strokeWidth=pt(0.5)
    )
    e2 = newText('', # Empty box, will get the overflow from e1, if there is any.
        name='Text2', # Flow reference by element.name
        nextElement='ElasticText3', nextPage='Page 1',
        parent=page1, padding=4, x=100, w=BoxWidth, h=200,
        conditions=[Right2Right(), Float2Top(), Fit2Bottom(), Overflow2Next()], yAlign=TOP,
        fill=whiteColor, stroke=noColor,
    )
    # Get next page, to show flow running over page breaks.
    page2 = page1.next
    page2.name = 'Page 2'
    page2.padding = PagePadding

    e3 = newText('', # Empty box, will get the overflow from e2, if there is any.
        name='ElasticText3', # Flow reference by element.name
        parent=page2, padding=4, w=BoxWidth,
        conditions=[Right2Right(), Float2Top(), Fit2Bottom()],
        yAlign=TOP,
        fill=whiteColor, stroke=noColor)

    score = doc.solve() # Try to solve all pages.
    if score.fails:
        print(score.fails)

    return doc # Answer the doc for further doing.

d = makeDocument()
"""
d.context.Variable(
    [dict(name='DoTextFlow', ui='CheckBox', args=dict(value=True)),
     dict(name='BoxWidth', ui='Slider', args=dict(minValue=100, value=500, maxValue=PageSize)),
     dict(name='PagePadding', ui='Slider', args=dict(minValue=0, value=30, maxValue=100)),
     dict(name='PageSize', ui='Slider', args=dict(minValue=200, value=500, maxValue=PageSize)),
    #dict(name='ElementOrigin', ui='CheckBox', args=dict(value=False)),
    ], globals())
"""
d.export(EXPORT_PATH)

