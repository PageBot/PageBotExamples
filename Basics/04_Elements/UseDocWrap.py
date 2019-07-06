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
#     UseDocWrap.py
#
#     Container element that holds an entire other document, as if it was an image.
#     Difference is that the rendering takes place by swapping in embedded
#     document pages during rendering, while maintaining the watershed for styles.
#
from pagebot.elements import *
from pagebot.document import Document
from pagebot.toolbox.units import pt
from pagebot.conditions import *
from pagebot.toolbox.color import color, noColor

W = H = pt(100) # Size of documents to be embedded
CW = CH = pt(300) # Size of the document that will hold 4 DowWrap elements.
PADDING = pt(8)

embeddedDoc = Document(w=W, h=H)
# Fill 4 pages of the document.
elementParams = {
    1: (color(1, 0, 0), [Left2Left(), Top2Top()]),
    2: (color(1, 1, 0), [Right2Right(), Top2Top()]),
    3: (color(0, 0.5, 0), [Left2Left(), Bottom2Bottom()]),
    4: (color(0, 0, 0.5), [Right2Right(), Bottom2Bottom()]),
}
page = embeddedDoc[1]
for n in range(1, 5):
    page.padding = PADDING
    eColor, eConditions = elementParams[n]
    newRect(parent=page, fill=0.9, conditions=[Fit2Sides()])
    newRect(parent=page, fill=0.8, conditions=[Fit()])
    newRect(parent=page, name='Element%d' % n, 
        w=page.w/2, h=page.h/2, fill=eColor, conditions=eConditions)
    page.solve()
    if n != 4:
        page = page.next

# Just for illustrative reference, save the embedded document.
embeddedDoc.export('_export/UseDocWrap_EmbeddedDoc.pdf')

# Now create the main container document.
doc = Document(w=CW, h=CH) # Default creates just a single page.
view = doc.view
view.padding = pt(32)
view.showFrame = True
view.showPadding = True
view.showCropMarks = True

page = doc[1]
page.padding = PADDING
for n in range(1, 5):
    eColor, eConditions = elementParams[n]
    DocWrap(embeddedDoc, parent=page, pn=n, conditions=eConditions, 
        margin=pt(10), 
        showRegistrationMarks=True,
        showCropMarks=True, 
        viewCropMarkSize=pt(6),
        viewCropMarkDistance=pt(3)
    )
page.solve()

doc.export('_export/UseDocWrap.pdf')

