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
#     TextBoxConditionalAlign.py
#
#     If a TextBox as self.nextElement defined as name for another text box on the
#     same page, then overflow of self will go into the other text box.

from pagebot import getContext
from pagebot.constants import *
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.conditions import *
from pagebot.elements import *
from pagebot.document import Document
from pagebot.toolbox.color import color, noColor, blackColor
from pagebot.toolbox.units import pt

c = getContext()
P = 100 # Page padding and box size
G = 6 # gutter
W = H = 6*P + 5*G

# Export in _export folder that does not commit in git. Force to export PDF.
EXPORT_PATH = '_export/useTextBoxConditionalAlign.pdf'

font = findFont('Roboto-Regular')

# Create a new document, default to the defined page size.
doc = Document(w=W, h=H, autoPages=2, context=c)

style = dict(font=font, fontSize=pt(8), xTextAlign=CENTER)

for pn, g, g2, p in ((1, G, G/2, P), (2, 0, 0, W/6)): # With and without gutter

    page = doc[pn] # get page on pageNumber, first in row (this is only one now).
    page.padding = p+g
    page.showPadding = True

    # Corners 

    # Top left,  aligned with page side and page padding
    bs = c.newString('Left2SideLeft\nTop2SideTop', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, padding=G, conditions=(Left2SideLeft(), Top2SideTop()))
    bs = c.newString('Left2Left\nTop2Top', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, padding=G, conditions=(Left2Left(), Top2Top()))
    bs = c.newString('Left2Left\nTop2SideTop', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, padding=G, conditions=(Left2Left(), Top2SideTop()))
    bs = c.newString('Left2SideLeft\nTop2Top', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, padding=G, conditions=(Left2SideLeft(), Top2Top()))

    # Top right, aligned with page side and page padding
    bs = c.newString('Right2Right\nTop2Top', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, padding=G, conditions=(Right2Right(), Top2Top()))
    bs = c.newString('Right2SideRight\nTop2Top', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, padding=G, conditions=(Right2SideRight(), Top2Top()))
    bs = c.newString('Right2SideRight\nTop2SideTop', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, padding=G, conditions=(Right2SideRight(), Top2SideTop()))
    bs = c.newString('Right2Right\nTop2SideTop', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, padding=G, conditions=(Right2Right(), Top2SideTop()))

    # Bottom right, aligned with page side and page padding
    bs = c.newString('Right2Right\nBottom2Bottom', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, padding=G, conditions=(Right2Right(), Bottom2Bottom()))
    bs = c.newString('Right2SideRight\nBottom2Bottom', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, padding=G, conditions=(Right2SideRight(), Bottom2Bottom()))
    bs = c.newString('Right2SideRight\nBottom2SideBottom', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, padding=G, conditions=(Right2SideRight(), Bottom2SideBottom()))
    bs = c.newString('Right2Right\nBottom2SideBottom', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, padding=G, conditions=(Right2Right(), Bottom2SideBottom()))

    # Bottom left, aligned with page side and page padding
    bs = c.newString('Left2SideLeft\nBottom2SideBottom', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, padding=G, conditions=(Left2SideLeft(), Bottom2SideBottom()))
    bs = c.newString('Left2Left\nBottom2Bottom', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, padding=G, conditions=(Left2Left(), Bottom2Bottom()))
    bs = c.newString('Left2Left\nBottom2SideBottom', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, padding=G, conditions=(Left2Left(), Bottom2SideBottom()))
    bs = c.newString('Left2SideLeft\nBottom2Bottom', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, padding=G, conditions=(Left2SideLeft(), Bottom2Bottom()))

    # Centers

    # Top center, aligned with page side and page padding
    bs = c.newString('Right2Center\nTop2SideTop', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, mr=g2, padding=G, conditions=(Right2Center(), Top2SideTop()))
    bs = c.newString('Left2Center\nTop2SideTop', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, ml=g2, padding=G, conditions=(Left2Center(), Top2SideTop()))
    bs = c.newString('Right2Center\nTop2Top', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, mr=g2, padding=G, conditions=(Right2Center(), Top2Top()))
    bs = c.newString('Left2Center\nTop2Top', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, ml=g2, padding=G, conditions=(Left2Center(), Top2Top()))

    # Bottom center, aligned with page side and page padding
    bs = c.newString('Right2Center\nBottom2SideBottom', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, mr=g2, padding=G, conditions=(Right2Center(), Bottom2SideBottom()))
    bs = c.newString('Left2Center\nBottom2SideBottom', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, ml=g2, padding=G, conditions=(Left2Center(), Bottom2SideBottom()))
    bs = c.newString('Right2Center\nBottom2Bottom', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, mr=g2, padding=G, conditions=(Right2Center(), Bottom2Bottom()))
    bs = c.newString('Left2Center\nBottom2Bottom', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, ml=g2, padding=G, conditions=(Left2Center(), Bottom2Bottom()))

    # Left center, aligned with page side and page padding
    bs = c.newString('Left2SideLeft\nBottom2Middle', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, mb=g2, padding=G, conditions=(Left2SideLeft(), Bottom2Middle()))
    bs = c.newString('Left2SideLeft\nTop2Middle', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, mt=g2, padding=G, conditions=(Left2SideLeft(), Top2Middle()))
    bs = c.newString('Left2Left\nBottom2Middle', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, mb=g2, padding=G, conditions=(Left2Left(), Bottom2Middle()))
    bs = c.newString('Left2Left\nTop2Middle', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, mt=g2, padding=G, conditions=(Left2Left(), Top2Middle()))

    # Right center, aligned with page side and page padding
    bs = c.newString('Right2SideRight\nBottom2Middle', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, mb=g2, padding=G, conditions=(Right2SideRight(), Bottom2Middle()))
    bs = c.newString('Right2SideRight\nTop2Middle', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, mt=g2, padding=G, conditions=(Right2SideRight(), Top2Middle()))
    bs = c.newString('Right2Right\nBottom2Middle', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, mb=g2, padding=G, conditions=(Right2Right(), Bottom2Middle()))
    bs = c.newString('Right2Right\nTop2Middle', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, mt=g2, padding=G, conditions=(Right2Right(), Top2Middle()))

    # Middle 4
    bs = c.newString('Right2Center\nBottom2Middle', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, mr=g2, mb=g2, padding=G, conditions=(Right2Center(), Bottom2Middle()))
    bs = c.newString('Left2Center\nBottom2Middle', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, ml=g2, mb=g2, padding=G, conditions=(Left2Center(), Bottom2Middle()))
    bs = c.newString('Right2Center\nTop2Middle', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, mr=g2, mt=g2, padding=G, conditions=(Right2Center(), Top2Middle()))
    bs = c.newString('Left2Center\nTop2Middle', style=style)
    newTextBox(bs, parent=page, fill=0.8, stroke=0, w=p, h=p, ml=g2, mt=g2, padding=G, conditions=(Left2Center(), Top2Middle()))

doc.solve()

doc.export(EXPORT_PATH)

