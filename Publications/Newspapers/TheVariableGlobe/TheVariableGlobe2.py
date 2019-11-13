# -*- coding: UTF-8 -*-
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
# =============================================================================
#
#     TheVariableGlobe.py
#
from copy import copy

from pagebot import getContext
# Blob random text for contenxt.
from pagebot.contributions.filibuster.blurb import Blurb
# Import the generic Document class. There is also specialized Publication classes 
# inheriting from Document, but for educational purpose, we'll use the generic class.
from pagebot.document import Document 
# Get constants needed for this Newspaper page.
from pagebot.constants import (Broadsheet, GRID_SQR, BASE_LINE, BASE_INDEX_RIGHT, 
    CENTER, LEFT, GRID_COL, GRID_COL_BG, GRID_ROW_BG)
from pagebot.conditions import *
# Import the measure units that we need
from pagebot.toolbox.units import inch, pt, mm, em
# Import color stuff
from pagebot.toolbox.color import blackColor, color
# Import all types of page elements that we may need.
from pagebot.elements import * 
# Font findings functions
from pagebot.fonttoolbox.objects.font import findFont, getInstance
from pagebot.toolbox.dating import now

context = getContext()

# =============================================================================
#    Specialized components
# .............................................................................

class TopHead(Rect):
    def __init__(self, **kwargs):
        Rect.__init__(self, **kwargs)
        newTextBox(parent=self, name='TopHeadQuote', mr=G, h=RH, w=CW3,
            conditions=(Left2Left(), Top2Top()))
        newTextBox(parent=self, name='TopHeadImage', mr=G, h=RH, w=CW1, 
            conditions=(Right2Right(), Float2Top(), Float2Left()))
        newTextBox(parent=self, name='TopHeadDate', h=RH, w=CW1,
            conditions=(Right2Right(), Top2Top(), Float2Left()))
    
# =============================================================================
#    Random text generator
# .............................................................................

blurb = Blurb()

# =============================================================================
#    Building switches
# .............................................................................

SHOW_TOPHEAD = True # Headline on top of title
SHOW_TITLE = True # Main title of the newspaper
SHOW_ARTICLE1 = True
SHOW_BACKGROUND = True

# =============================================================================
#    Measures
# .............................................................................
#W, H = Broadsheet # Split paper size in document width and height
W, H = pt(819, 1176) # Dutch Volksrant tabloid size.

U = pt(10)
G = pt(11)
PL = pt(35) # Page padding left
PR = pt(28)
PT = 4*U # Page padding top
PB = pt(48) # Page badding bottom
PADDING_LEFT = PT, PR, PB, PL
PADDING_RIGHT = PT, PL, PB, PR
BASELINE = mm(3.45) # Overall baseline grid, talem from background baseline

# Grid definitions
CC = 5 # Column count
CW = (W-PL-PR+G)/CC-G # Column width (without gutter)
CW1 = CW
CW2 = 2*CW + G
CW3 = 3*CW + 2*G
CW4 = 4*CW + 3*G
CW5 = 5*CW + 4*G

RC = 7 # Row count
RH = BASELINE * RC # Row height (without gutter) depending on row count and page height

gridX = [] # Create the column grid
for colIndex in range(CC):
    gridX.append((CW, G))
gridY = [] # Create the row grid
for rowIndex in range(RC):
    gridY.append((RH, G))

# For copyright reasons the template PDF cannot be added to the Open Source repository 
TEMPLATE_PATH = '_local/2018-09-04_De_Volkskrant_-_04-09-2018.pdf'
#TEMPLATE_PAGE = '_local/2018-09-14_De_Volkskrant_-_14-09-2018.pdf'
PAGE_COUNT = 2 #context.numberOfImages(TEMPLATE_PATH)

# =============================================================================
#    Text content 
#    For this example defined as strings. Should from from MarkDown file instead.
# .............................................................................

TITLE = 'The Variable Globe'

# =============================================================================
#    Fonts and Variable instances.
# .............................................................................

bodyFont = findFont('RobotoDelta-VF')
#print(bodyFont.axes) # Uncomment to see axes and values for this VF
location = dict(wght=700)
boldFont = bodyFont.getInstance(location)
headFont = findFont('AmstelvarAlpha-VF')
#print(headFont.axes) # Uncomment to see axes and values for this VF
# Create bold/title font as Variable location
kerning = {('V','a'): -100}
location = dict(wght=700, XTRA=350)
headBoldFont = headFont.getInstance(location, kerning=kerning)
location = dict(wght=650, XTRA=260)
headBoldCFont = titleFont = headFont.getInstance(location, kerning=kerning)

if 0:
    # Print the available axis names with the (min, default, max) values.
    print('Variable axes for bodyFont: ', bodyFont.axes)
    print('Variable axes for headFont: ', headFont.axes) 
    print('Generated instances not longer has axes, e.g. headBoldFont:', headBoldFont.axes)

# =============================================================================
#    Styles (comparable to InDesign paragraph and character styles)
# .............................................................................

# Define types of border below text boxes 
border = dict(strokeWidth=pt(1), stroke=blackColor)

# Create the styles
topHeadStyle = dict(font=bodyFont, fontSize=pt(16), xTextAlign=LEFT, hyphenation=False)
topHeadBoldStyle = copy(topHeadStyle)
topHeadBoldStyle['font'] = headBoldFont
titleStyle = dict(font=titleFont, fontSize=pt(64), xTextAlign=CENTER, hyphenation=False)
# Textline under the newspaper title
subTitleStyle = dict(font=bodyFont, fontSize=pt(9), xTextAlign=LEFT)
# Article headline
headline1Style = dict(font=headBoldFont, fontSize=pt(32), leading=em(1.1), textFill=0, xTextAlign=CENTER, hyphenation=False)
# Article main text
mainStyle = dict(font=bodyFont, fontSize=pt(9), leading=BASELINE, textFill=0)
dateStyle = dict(font=bodyFont, fontSize=pt(9), leading=BASELINE, textFill=0)
urlStyle = dict(font=boldFont, fontSize=pt(9), leading=BASELINE, textFill=0)

#=============================================================================
#    Create the document and define the viewing parameters
# .............................................................................
doc = Document(w=W, h=H, originTop=False, gridX=gridX, gridY=gridY, 
    baselineGrid=BASELINE, autoPages=PAGE_COUNT)
# Set the viewing parameters
view = doc.view
view.padding = inch(0.5)
view.showCropMarks = True
view.showRegistrationMarks = True
view.showNameInfo = True
view.showGrid = [GRID_COL, GRID_ROW_BG] # Defaults to showing GRID_
view.showBaselines = [BASE_LINE, BASE_INDEX_RIGHT]
view.showFrame = True
view.showPadding = True
view.showColorBars = False # Set to True for color calibration bars.

# =============================================================================
#    Add background image from existing newspaper.
#    This assumes that our document has the same size/proportions 
#    as the background image.
#    And overlay transparant gray layer to see template as shaded    
# .............................................................................

opaque = 0.7

for pn in range(1, PAGE_COUNT+1):
    page = doc[pn]
    if page.isLeft:
        page.padding = PADDING_LEFT # Set 4 padding values all at once.
    else:
        page.padding = PADDING_RIGHT # Set 4 padding values all at once.
    
    if SHOW_BACKGROUND:
        # Put them on z-position != 0, to avoid the condition floating hooking on them.
        # E.g. Float2Top() layout conditions only look at elements with the same z-value.
        newImage(TEMPLATE_PATH, w=W, h=H, z=-10, index=pn, parent=page)
        newRect(fill=(1, 1, 1, opaque), w=W, h=H, z=-10, parent=page)

# =============================================================================
#    Get the first page from the doc
# .............................................................................

pageIndex = 1 # Select the page index from the PDF to use as background image. 
page = doc[pageIndex]
page.showBaselines = True

# =============================================================================
#    Top-left headline above newspaper title. Bold name with designer quote
# .............................................................................
if SHOW_TOPHEAD:
    e = TopHead(parent=page, h=RH, 
        conditions=[Left2Left(), Fit2Width(), Top2Top()])
    e.solve()
    
    txt = blurb.getBlurb('name')
    bs = context.newString(txt+': ', style=topHeadBoldStyle)
    txt = blurb.getBlurb('design_article_title').capitalize()
    if not txt.endswith('.'):
        txt += '.'
    bs += context.newString('“'+txt+'”', style=topHeadStyle)
    txt = ' P:%d' % choice(range(80))
    bs += context.newString(txt, style=topHeadBoldStyle)
    paddingTop = inch(1)
    #tw, th = context.textSize(bs, w=CW3)
    e.select('TopHeadQuote').bs = bs
    
    # Date box
    date = now()
    dateString = '%s %s %s %s' % (date.fullDayName.upper(), date.day, date.fullMonthName.upper(), date.year)
    urlString = '\n%s.com' % ( TITLE.replace(' ',''))
    bs = context.newString(dateString, style=dateStyle) #, w=CW1)
    bs += context.newString(urlString, style=urlStyle)
    e.select('TopHeadDate').bs = bs


urlStyle

if SHOW_TITLE:
    # Title of the newspaper. Calculate the size from the give usable page.pw width.
    bs = context.newString(TITLE, style=titleStyle, w=page.pw)
    tw, th = bs.size # Get the (width, height) if the created string.
    #print('Calculated fitting title size: ', bs.fittingFontSize)
    titleBox= newTextBox(bs, parent=page, h=th, borderBottom=border,
        conditions=(Left2Left(), Fit2Width(), Float2Top()))
    titleBox.solve()
    # Title subline of the newspaper
    txt = blurb.getBlurb('design_article_title').capitalize()
    bs = context.newString(txt, style=subTitleStyle)
    tw, th = bs.size
    titleSublineBox = newTextBox(bs, parent=page, h=4*BASELINE, borderBottom=border, pt=th/2,
        conditions=(Left2Left(), Fit2Width(), Float2Top()))


if SHOW_ARTICLE1:
    # Main article as group of 3 text boxes
    main1 = newRect(parent=page, w=CW3, mt=G, fill=0.95, conditions=(Left2Left(), Float2Top()))

    txt = blurb.getBlurb('design_theory').capitalize()
    bs = context.newString(txt, style=headline1Style)
    tw, th = bs.size
    head1 = newTextBox(bs, name='head1', parent=main1, conditions=(Left2Left(), Fit2Width(), Float2Top()))

    txt = blurb.getBlurb('article_content')
    bs = context.newString(txt, style=mainStyle)
    newTextBox(bs, name='main11', h=1200, w=CW1, parent=main1,
        conditions=(Left2Left(), Float2Top()))
    txt = blurb.getBlurb('article_content')
    bs = context.newString(txt, style=mainStyle)
    newTextBox(bs, name='main12', h=1200, w=CW1, parent=main1, fill=0.95,
        conditions=(Right2Right(), Float2Top()))
'''
if 1:
    # Main article as group of 3 text boxes
    main2 = newRect(parent=page, w=CW4, mt=G, fill=0.8, conditions=(Left2Left(), Float2Top()))

    bs = context.newString('Headline main 2', style=headline1Style)
    tw, th = bs.size
    newTextBox(bs, name='head2', parent=main2, conditions=(Left2Left(), Fit2Width(), Float2Top()))

    bs = context.newString('Aaaa ' * 120, style=mainStyle)
    newTextBox(bs, name='main21', h=400, w=CW2, parent=main2, fill=0.8, mt=3*G,
        conditions=(Left2Left(), Float2Top()))
    bs = context.newString('Aaaa ' * 120, style=mainStyle)
    newTextBox(bs, name='main22', h=400, w=CW2, parent=main2, fill=0.8, mt=3*G, 
        conditions=(Right2Right(), Float2Top()))

'''
doc.solve() # Drill down to solve all elements conditions.

# =============================================================================
#    Export to PDF or other file formats
# .............................................................................

doc.export('_export/TheVariableGlobe.pdf')

