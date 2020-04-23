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
#     ReadWrite.py
#
#     Read/write the raw Sketch instance from a Sketch drawing.
#     Convert the data into a PageBot Document instance, through SketchContext
#     translation into Elements.
#
#     Equivalent classes on PageBot <--> SketchApp2Py
#     Publication       SketchApi/Sketch file
#     Document          SketchPage
#     Document.pages    SketchArtBoard[]
#     Page.elements     SketchArtBoard.layers

from pagebot.toolbox.units import pt
from pagebot.document import Document
from pagebotosx.contexts.drawbotcontext.drawbotcontext import DrawBotContext
from pagebot.constants import *
from pagebot.elements import *

try:
    import sketchapp2py
    from sketchcontext.context import SketchContext
except ImportError:
    print("""Needs installing of SketchContext and SketchApp2Py""")
    # https://github.com/PageBot/SketchContext
    # https://github.com/PageBot/SketchApp2Py

sketchPath = 'TestImage.sketch'

#context = SketchContext()
#sketchApi = context.read(sketchPath)
context = SketchContext(sketchPath) # Same as context.b.api

drawBotContext = DrawBotContext() # Used for exporting the document to PDF

# Create a Document instance from the current selected Sketch file.
# The copy create all elements, interpreting the Sketch file.
# Take over the Document measures from the various Sketchboards found.

doc = Document()
context.readDocument(doc)

isLayers = context.b.idLayers

page = doc[1]
for e in page.elements:
    layer = isLayers[e.sId]
    print(layer.frame)
    layer.frame.x += 140
    print(e.sId, e.name, layer.frame)

view = doc.view
view.padding = pt(30)
view.showCropMarks = True
view.showRegistrationMarks = True
view.showPadding = True
view.showFrame = True
view.showNameInfo = True
#view.showColorBars = True

doc.export('_export/TestImage.pdf')

context.save('_export/TestImageWrite.sketch')

