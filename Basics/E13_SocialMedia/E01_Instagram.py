#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E01_Instagram.py
#
#     Take the content from a MarkDown file, typically one that contains website content.
#     Find the titles of events in a (h2, h3, h4, image) pattern
#     Generate Instagram images for each event.
#
from pagebot import getContext
from pagebot.filepaths import getResourcesPath
from pagebot.publications.instagram import InstagramPost
from pagebot.toolbox.units import px, em, pt
from pagebot.toolbox.color import color, noColor
from pagebot.constants import InstagramSquare, CinemaWide, MAX_IMAGE_WIDTH
from pagebot.base.typesetter import Typesetter

context = getContext()

"""
from pagebot.document import Document
from pagebot.conditions import * # Import all conditions for convenience.
from pagebot.elements import *
import flat
"""

# Example image that has nice areas to put text as example.
imagePath = getResourcesPath() + '/images/pagebot.png'
EXPORT_PATH = '_export/01_Instagram-%s.pdf' % context.name
MD_PATHS = ['DDS-home.md']

h2Style = dict(font='Upgrade-Medium', fontSize=pt(80), leading=em(1), textFill=color(1))
h3Style = dict(font='Upgrade-Regular', fontSize=pt(40), leading=em(1), textFill=color(1))
h4Style = dict(font='Upgrade-Semibold', fontSize=pt(40), leading=em(1), textFill=color(1))
supStyle = dict(font='Upgrade-Semibold', fontSize=pt(40), leading=em(1), textFill=color(1,0,0))
styles = dict(
    h2=h2Style,
    h3=h3Style,
    h4=h4Style,
    sub=supStyle,
)
instagram = InstagramPost(styles=styles)
w, h = InstagramSquare
doc = instagram.newDocument(name='Instagram', w=w, h=h, context=context)

# By default, the typesetter produces a single Galley with content and code blocks.    
t = Typesetter(context, maxImageWidth=MAX_IMAGE_WIDTH)
mdPath = MD_PATHS[0] # Only make instagram posts from the home page.
t.typesetFile(mdPath)

# Header styles
pad = px(50)
tPad = px(25)

# Filter all h2/h3/image combinations, to make instagram banners.
bannerData = []
bs2 = bs3 = bs4 = None
for e in t.galley.elements:
    if e.isText:
        for run in e.bs.runs:
            if bs2 is None and run.style.get('name') == 'h2':
                bs2 = context.newString(run.s.strip(), h2Style)
                bs3 = bs4 = None
            elif bs3 is None and run.style.get('name') == 'h3':
                bs3 = context.newString(run.s.strip(), h3Style)
                bs4 = context.newString('', h4Style)
            elif run.style.get('name') == 'h4':
                bs4 += context.newString(run.s.strip(), h4Style)
            elif run.style.get('name') == 'sup':
                bs4 += context.newString(run.s.strip(), supStyle) + ' '
    elif e.isImage:
        if not None in (bs2, bs3, bs4):            
            bannerData.append((bs2, bs3, bs4, e.path, e.alt))
            bs2 = bs3 = bs4 = None


# Now we have all content, we can create the pages, one per post
page = doc[1]
# For now direct output, as long as vertical position of text is not accurate
for bs2, bs3, bs4, imagePath, alt in bannerData:
    context.newPage(page.w, page.h)
    bs4.s = bs4.s.split('•')[0].replace('th', ', ')

    iw, ih = context.imageSize(imagePath)
    if iw > ih:
        iw, ih = None, h
    else:
        iw, ih = w, None
    if 'x=center' in alt:
        xAlign = CENTER
        x = w/2
    else:
        xAlign = None
        x = 0
    sc = h/ih
    x = y
    context.size(sc)
    context.image(imagePath, x)
    newImage(path=imagePath, parent=page, x=x, y=0, w=iw, h=ih, xAlign=xAlign)

    if bs2 is not None:
        tw, th = context.textSize(bs2, w=w-2*pad-2*tPad)
        newRect(x=pad, y=h-th-2*tPad, fill=color(rgb='red', a=0.8), w=w-2*pad, h=th+2*tPad, parent=page)
        newText(bs2, x=pad+tPad, y=h-2*tPad, w=w-2*pad-2*tPad, parent=page)

    if bs3 is not None:
        tw, th = context.textSize(bs3, w=w-2*pad-2*tPad)
        newRect(x=pad, y=h/2-3.5*tPad, fill=color(rgb='darkblue', a=0.8), w=w-2*pad, h=th+2*tPad, parent=page)
        newText(bs3, x=pad+tPad, y=h/2, w=w-2*pad-2*tPad, parent=page)

    if bs4 is not None:
        tw, th = context.textSize(bs4, w=w-2*pad-2*tPad)
        newRect(x=pad, y=0, fill=color(rgb='blue', a=0.8), w=w-2*pad, h=th+2*tPad, parent=page)
        newText(bs4, x=pad+tPad, y=2*tPad, w=w-2*pad-2*tPad, parent=page)

    page = page.next


