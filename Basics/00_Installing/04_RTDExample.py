from pagebot.document import Document
from pagebot.elements import newRect
from pagebot.conditions import Center2Center, Middle2Middle
from pagebot.toolbox.units import pt
from pagebot.toolbox.color import color

W, H = pt(300, 200) # Get size units
doc = Document(w=W, h=H, originTop=False)
page = doc[1]
newRect(parent=page, fill=color('red'), size=pt(240, 140), showDimensions=True, conditions=[Center2Center(), Middle2Middle()])
page.solve()
doc.export('_export/RedSquare.png')
