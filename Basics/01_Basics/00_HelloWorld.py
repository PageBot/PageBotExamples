# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
# -----------------------------------------------------------------------------
#

from pagebot.document import Document
from pagebot.elements import newText
from pagebot.toolbox.units import pt
from pagebot.fonttoolbox.objects.font import findFont

def helloWorld(context):
    # Find the Roboto font that exist in PageBot resources.
    f = findFont('Roboto-Bold')
    # Create document with default 1 page.
    doc = Document(w=pt(800), h=pt(190), context=context)
    # The context is not stored in the document, but passed on to the doc.view
    # Get the view from the document, that contains the export view.context.
    view = doc.view 
    print(view.context)
    # First page in the list is uneven (right side)
    # This is different from “normal” Python list, where the index starts at 0.
    page = doc[1]
    # Create a new Text element with (x, y) conditions
    e = newText('Hello World', x=30, y=0, font=f, fontSize=140, textFill=0.2, parent=page)
    print(e)
    
    # Export the document page as png, so it shows as web image.
    doc.export('_export/HelloWorld-%s.png' % view.name)

if __name__ == '__main__':
    from pagebot import getContext

    for contextName in ('DrawBot', 'Flat'):
        context = getContext(contextName)
        helloWorld(context)
