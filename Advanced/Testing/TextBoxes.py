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
#     TextBoxes.py
#
#     Tests pagebot text boxes.

from pagebot.document import Document
from pagebot.elements import *
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.units import pt
from pagebot.toolbox.color import noColor, color
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.constants import *
from pagebot.style import getRootStyle

# TODO: move to basics when finished.

H, W = A3
W = pt(W)
H = pt(H)
M = 50 

roboto = findFont('Roboto-Regular')
robotoBold = findFont('Roboto-Bold')
bungee = findFont('Bungee-Regular')
bungeeHairline = findFont('Bungee-HairlineRegular')
bungeeOutline = findFont('Bungee-OutlineRegular')
blurb = Blurb()
txt = blurb.getBlurb('news_headline', noTags=True)

def getBabelString(page):
    # Create a new BabelString with the DrawBot FormattedString inside.
    style=dict(font=bungee, fontSize=36, textFill=(1, 0, 0))
    bs = page.newString('This is a string', style=style)

    # Adding or appending strings are added to the internal formatted string.
    # Adding plain strings should inherit the existing style.
    bs += ' and more,'

    # Reusing the same style with different text fill color.
    style['textFill'] = 0.1, 0.5, 0.9
    style['font'] = bungeeHairline
    bs += page.newString(' more and', style=style)

    # Different color and weight.
    style['textFill'] = 0.5, 0, 1
    style['font'] = bungeeOutline
    bs += page.newString(' even more!', style=style)
    return bs


def test():
    doc = Document(w=W, h=H)
    doc.name = 'TextBoxes-%s' % doc.context.name
    print('# Testing text boxes in %s' % doc)

    page = doc[1]
    bs = getBabelString(page)

    w = W-2*M
    h = 2 * M
    x = M
    y = H - M - h

    tb = newTextBox(bs, x=x, y=y, w=w, h=2*M, parent=page,
            stroke=color(0.3, 0.2, 0.1, 0.5), style=dict(hyphenation=True,
                language='en', leading=200))

    style = dict(font=bungee, fontSize=pt(48), stroke=color(1, 0, 0))
    bs = page.newString(txt, style=style)
    h = 300
    y = H - 3*M - h

    #stroke=color(0.3, 0.2, 0.1, 0.5),
    tb = newTextBox(bs, x=M, y=y, w=W/2, h=h, parent=page, style=dict(hyphenation=True, language='en',
            leading=200))

    w, h = tb.getTextSize()
    print('Size: %s, %s' % (w, h))
    newRect(x=x, y=y, w=w, h=h, parent=page, stroke=color(1, 0, 0), strokeWidth=1)

    for baseline in tb.baselines:
        y = H - 3*M - baseline
        newLine(x=x, y=y, w=W/2, h=0, stroke=color(0.5), strokeWidth=0.5,
                parent=page)

    #doc.view.drawBaselines()
    #doc.export('_export/Strings.pdf')
    doc.build()

test()
