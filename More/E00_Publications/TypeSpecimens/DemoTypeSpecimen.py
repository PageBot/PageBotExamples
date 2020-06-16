
from pagebot.toolbox.units import *
from pagebot.toolbox.color import *
from pagebot.document import Document
from pagebot.constants import *
from pagebot.elements import *
from pagebot.conditions import *

H, W = A4
doc = Document(w=W, h=H, autoPages=1)
view = doc.view
view.padding = inch(1)
view.showFrame = True
view.showRegistrationMarks = True
view.showCropMarks = True
view.showColorBars = True

page = doc[1]
page.padding = p(6)
page.showPadding = True
page.bleed = mm(3)

newRect(parent=page, fill=color('red'),
w=page.w*0.6+page.bleedLeft, conditions=[Left2BleedLeft(), Top2SideTop()])
newRect(parent=page, fill=color('blue'), mt=20, conditions=[Left2Left(), Float2Top()])

print(page.solve())
doc.export('_export/OurTypeSpeciment.pdf')
