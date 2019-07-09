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
from pagebot.elements import newRect
from pagebot.conditions import Center2Center, Middle2Middle
from pagebot.toolbox.units import pt
from pagebot.toolbox.color import color

W, H = pt(500, 400) # Get size units
# Create document with default 1 page.
doc = Document(w=W, h=H, originTop=False) 
# First page in the list is uneven (right side)
page = doc[1] 
# Create a new rectangle element with position conditions
newRect(parent=page, fill=color('red'), size=pt(200),
    # Show measure lines on the element.
    showDimensions=True, 
    conditions=[Center2Center(), Middle2Middle()])
# Make the page apply all conditions.
page.solve() 
# Export the document page as png, so it shows as web image.
doc.export('_export/RedSquare.png') 
