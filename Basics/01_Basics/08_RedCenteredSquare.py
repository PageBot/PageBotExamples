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
page = doc[1] # First page in the list is uneven (right side)
# Create a new rectangle element with position conditions
newRect(parent=page, fill=color('red'), size=pt(200),
        showDimensions=True, # Show measure lines on the element.
    conditions=[Center2Center(), Middle2Middle()])
page.solve() # Make the page apply all conditions.
doc.export('_export/RedSquare.png') # Export the document page.
    