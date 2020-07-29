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
from pagebot.toolbox.units import px, em
from pagebot.toolbox.color import color, noColor
from pagebot.constants import InstagramSquare, MAX_IMAGE_WIDTH
from pagebot.typesetter import Typesetter

context = getContext()

"""
from pagebot.document import Document
from pagebot.conditions import * # Import all conditions for convenience.
from pagebot.elements import *
import flat
"""

# Example image that has nice areas to put text as example.
imagePath = getResourcesPath() + '/images/pagebot.png'
EXPORT_PATH = '_export/05_ImageClipping-%s.pdf' % context.name
MD_PATHS = ['DDS-home.md']

h2Style = dict(font='Upgrade-Medium', fontSize=px(120), leading=em(1), textFill=color(1))
h3Style = dict(font='Upgrade-Regular', fontSize=px(90), leading=em(1), textFill=color(1))
h4Style = dict(font='Upgrade-Semibold', fontSize=px(90), leading=em(1), textFill=color(1))
styles = dict(
    h2=h2Style,
    h3=h3Style,
    h4=h4Style,
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
                bs4 += context.newString(run.s.strip(), h4Style)
    elif e.isImage:
        if not None in (bs2, bs3, bs4):            
            bannerData.append((bs2, bs3, bs4, e.path, e.alt))
            bs2 = bs3 = bs4 = None


# Now we have all content, we can create the pages, one per post
page = doc[1]
for bs2, bs3, bs4, imagePath, alt in bannerData:
    #print(bs2, bs3, bs4, imagePath)
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



def imageClipping(contextName):
    context = getContext(contextName)

    # Example image that has nice areas to put text as example.
    imagePath = getResourcesPath() + '/images/pagebot.png'
    EXPORT_PATH = '_export/05_ImageClipping-%s.pdf' % contextName

    W = pt(400) # Document size
    H = pt(400)
    PADDING = pt(24) # Page padding on all sides
    BLEED = pt(6)

    # Create a new document with 1 page. Set overall size and padding.
    doc = Document(w=W, h=H, title=EXPORT_PATH, padding=PADDING, context=context)
    # Get the default page view of the document and set viewing parameters
    view = doc.view
    view.padding = pt(30)
    view.showFrame = True
    view.showPadding = True
    view.showColorBars = False
    view.showCropMarks = True
    view.showRegistrationMarks = True
    view.showNameInfo = True # Showing page info and title on top of the page.

    # Get the page
    page = doc[1]
    # Make image box as child element of the page and set its layout conditions.
    # The image is portrait, so fitting vertical makes the image fit in the
    # padding box of the page.
    conditions = [Fit2Height(), Center2Center()]
    im = newImage(imagePath, parent=page, conditions=conditions,
            showOrigin=True)

    page = page.next
    # Fitting the image by width, it does not fit vertically anymore.
    conditions = [Fit2Width(), Middle2Middle()]
    im = newImage(imagePath, parent=page, conditions=conditions,
            showOrigin=True)

    page = page.next
    # Fitting the image by width, it does not fit vertically anymore.
    # Adding a mask as sibling, we can clip the image on the page padding.
    conditions = [Fit2Width(), Middle2Middle()]
    im = newImage(imagePath, parent=page, conditions=conditions,
            showOrigin=True)
    conditions =[Fit()]
    mask = newMask(parent=page, conditions=conditions, # Fit page padding
            showOrigin=True)

    page = page.next
    # Fitting the image by width, it does not fit vertically anymore.
    # The Mask can be any size and position on the page.
    conditions = [Fit2Width(), Middle2Middle()]
    im = newImage(imagePath, parent=page, conditions=conditions,
            showOrigin=True)
    conditions = [Right2Right(), Top2Top()]
    mask = newMask(parent=page, conditions=conditions,
            w=page.pw/2, h=page.ph/2, showOrigin=True)

    page = page.next
    page.bleed = BLEED # Set all bleed sides to the same value
    # Fitting the image by width, it does not fit vertically anymore.
    # Making the image bleed on page width.
    conditions = [Left2BleedLeft(), Fit2BleedRight(), Middle2Middle()]
    im = newImage(imagePath, parent=page, conditions=conditions,
            showOrigin=True)
    conditions = [Right2Right(), Top2Top()]

    page = page.next
    page.bleed = BLEED # Set all bleed sides to the same value
    # Fitting the image by width, it does not fit vertically anymore.
    # Making the image bleed on page width.
    # Now the mask needs to follow the bleed fit too.
    conditions = [Left2BleedLeft(), Fit2BleedRight(), Middle2Middle()]
    im = newImage(imagePath, parent=page, conditions=conditions,
            showOrigin=True)
    # Fit the mask on top half of the page, including bleed
    conditions = [Left2BleedLeft(), Fit2BleedRight(), Top2BleedTop()]
    mask = newMask(parent=page, conditions=conditions,
            w=page.w/2+2*BLEED, h=page.h/2+BLEED, showOrigin=True)

    doc.solve()

    # Export the document to this PDF file.
    doc.export(EXPORT_PATH)
