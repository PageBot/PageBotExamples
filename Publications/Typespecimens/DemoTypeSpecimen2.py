
from pagebot.toolbox.units import *
from pagebot.toolbox.color import *
from pagebot.document import Document
from pagebot.constants import *
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.fonttoolbox.objects.font import findFont
from pagebot import getContext
from pagebot.contributions.filibuster.blurb import Blurb
context = getContext()

b = Blurb()
print(b.getBlurb('article'))

H, W = A4
PADDING = p(6)
H1_FONTSIZE = pt(36)
H2_FONTSIZE = pt(14)
P_FONTSIZE = pt(10)
WATERFALL_TEXT = 'Hamburgefontstiv'

COLS = 4
G = pt(12)
CW = (W-2*PADDING-(COLS-1)*G)/COLS
GRID_X = [(CW, G)]*4

# ---------------------------------------
doc = Document(w=W, h=H, gridX=GRID_X, autoPages=1, context=context)
view = doc.view
view.padding = inch(1)
view.showFrame = True
view.showRegistrationMarks = True
view.showCropMarks = True
view.showColorBars = True
view.showGrid = True

blurbHeadline = Blurb().getBlurb('design_ankeiler')
blurbArticle = Blurb().getBlurb('article')*2

def buildPage(page, font):
    page.padding = PADDING
    page.showPadding = True
    page.bleed = mm(3)

    # Title of the page, showing the name of the font.
    nameOfFont = font.info.familyName + ' ' + font.info.styleName
    style = dict(font=font, fontSize=H1_FONTSIZE, leading=H1_FONTSIZE, textFill=color(0.2))
    bs = context.newString(nameOfFont, style=style)
    newTextBox(bs, padding=0, h=H1_FONTSIZE*1.5, conditions=[Top2Top(), Fit2Width()], parent=page)

    # Waterfall until the bottom of the page.
    bs = context.newString('')
    for n in range(1000):
        tw, th = bs.size
        if th > page.ph - H1_FONTSIZE:
            break
        style = dict(font=font, fontSize=P_FONTSIZE-2, leading=P_FONTSIZE+n, textFill=0)
        bs += context.newString('%spt  ' % (P_FONTSIZE+n), style=style)        
    
        style = dict(font=font, fontSize=P_FONTSIZE+n, leading=P_FONTSIZE+n, textFill=0)
        bs += context.newString(WATERFALL_TEXT+'\n', style=style)
    newTextBox(bs, padding=0, h=H1_FONTSIZE, conditions=[Float2Top(), Left2Left(), Fit2Bottom()], w=page.pw/2, parent=page)
    
    style = dict(font=font, fontSize=H2_FONTSIZE, leading=H2_FONTSIZE*1.4)
    bs = context.newString(blurbHeadline+'\n', style=style)

    style = dict(font=font, fontSize=P_FONTSIZE, leading=P_FONTSIZE*1.4)
    bs += context.newString(blurbArticle, style=style)
    newTextBox(bs, h=page.ph, w=page.pw/2-pt(12), conditions=[Right2Right(), Top2Top()], parent=page)
# ------------------------------------

page = None
FONTS = (
    'Roboto-Regular',
    'Roboto-Bold',
)
for fontName in FONTS:
    if page is None:
        page = doc[1]
    else:
        page = page.next
    font = findFont(fontName)
    buildPage(page, font)
    page.solve()

doc.export('_export/OurTypeSpeciment.pdf')
