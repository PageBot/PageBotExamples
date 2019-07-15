# -----------------------------------------------------------------------------
#
#     P A G E B O T
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

# Find the Roboto font that exist in PageBot resources.
f = findFont('Roboto-Bold')
# Create document with default 1 page.
doc = Document(w=pt(800), h=pt(190), originTop=False) 
# First page in the list is uneven (right side)
page = doc[1] 
# Create a new rectangle element with (x, y) conditions
newText('Hello World', x=30, y=0, 
    font=f, fontSize=140, textFill=0.2, parent=page)
# Export the document page as png, so it shows as web image.
doc.export('_export/HelloWorld.png') 
