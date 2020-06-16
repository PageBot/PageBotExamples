#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Find the font with a given name
#
# -----------------------------------------------------------------------------
#
from pagebot.document import Document
from pagebot.elements import newText
from pagebot.toolbox.units import pt
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.contexts import getContext
from pagebot.constants import CENTER, LEFT

W = pt(800) # Size of the document/page
H = pt(400)

for contextName in ('DrawBot', 'Flat'):
    context = getContext(contextName)

    # Find the Roboto font that exist in PageBot resources.
    font = findFont('PageBot-Regular') # PageBot version of TYPETR Upgrade
    fontSize = pt(140)

    # Create document with default 1 page.
    # The context is not stored in the document, but passed on to the doc.view
    doc = Document(w=W, h=H, context=context)

    # Get the view from the document, that contains the export view.context.
    print('Current context:', doc.view.context)

    # The first page in the list is uneven (right side)
    # This is different from “normal” Python lists, where the index starts at 0.
    page = doc[1]

    # Create a new Text element with (x, y) centered position.
    # In order to get it on the page, we define the parent.
    # Since the Text element does not have width defined, xAlign and xTextAlign
    # behave identical.
    e = newText('Hello World', x=W/2, y=H/2, font=font, fontSize=fontSize,
            textFill=0.2, xTextAlign=CENTER, showOrigin=True, parent=page)
    print('Element:', e)

    # Export the document page as PNG, so it shows as web image.
    #exportPath = '_export/00_HelloWorld-%s.png' % contextName
    exportPath = '_export/00_HelloWorld-%s.pdf' % contextName
    doc.export(exportPath)

