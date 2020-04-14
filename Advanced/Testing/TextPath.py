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
#     TextPath.py
#

#from pagebot.fonttoolbox.objects.font import findFont
from pagebot.fonttoolbox.objects.font import findFonts
from pagebot.contexts.basecontext.basepath import BasePath
from pagebot.document import Document

# TODO: find out how to remove overlap on text.
# Maybe avoid using text but load font in path?

def test(context):

    doc = Document(w=800, h=600, autoPages=1, context=context)
    font = findFonts(('Robo', 'Con', 'Bol', 'Ita'))[0]
    page = doc[1] # Get the single page from te document.


    '''
    path = BezierPath()
    path.rect(x=50, y=100, w=900, h=500)
    path.text('Difference', font=fontName, fontSize=200, offset=(105, 200))
    path.removeOverlap()

    text('Hello world', (100, 650))

    drawPath(path)
    '''

    style = dict(font=font, fontSize=100)
    p = BasePath(context, style=style)
    print(p)
    p.text('H')
    context.drawPath(p)


if __name__ == '__main__':
    from pagebot import getContext

    for contextName in ('DrawBot', 'Flat'):
        context = getContext(contextName)
        test(context)
