# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting usage of DrawBot, www.drawbot.com
#     Supporting usage of Flat, https://github.com/xxyxyz/flat
# -----------------------------------------------------------------------------
#
#     BertholdTypeSpecimen.py
#
#     This scripts generates a look-alike revival type specimen with an interpretation
#     of the classic Berthold specimen pages.
#     Special challenge is to use the capital-size system of Berthold in mm and 
#     the calculation of real values for the table and drawing the rulers.
#
#     For educational purpose in using PageBot, almost every line of code has been commented.
#

import os # Import standard libary for accessing the file system.
from random import choice, shuffle # Used for random selection of sample words

from pagebot import getContext # Decide if running in DrawBot or Linux-Flat
from pagebot.constants import * # Import some measure and alignments constants.
from pagebot.document import Document # Overall container class of any PageBot script
from pagebot.fonttoolbox.objects.font import findFont # Access to installed fonts
from pagebot.elements import newRect, newTextBox, newImage # Used elements in this specimen
from pagebot.conditions import * # Import layout conditions for automatic layout.
from pagebot.contributions.filibuster.blurb import Blurb

from pagebot.toolbox.transformer import path2FontName # Convenient CSS color to PageBot color conversion
from pagebot.toolbox.hyphenation import wordsByLength # Use English hyphenation dictionary as word selector
from pagebot.toolbox.units import inch, pt, em, p
from pagebot.toolbox.color import color, blackColor

context = getContext()

SHOW_GRID = True
SHOW_TEMPLATE = False
SHOW_FRAMES = True

sampleFont = findFont('Upgrade-Regular')
 
blurb = Blurb()
    
# Basic page metrics.
U = pt(9) # Page layout units, to unite baseline grid and gutter.
W, H = pt(590, 842) # Copy size from original Berthold specimen scan.
# Hard coded padding sizes derived from the scan.
PADDING_LEFT = pt(90, 42, 42, 40) # Page padding top, right, bottom, left
PADDING_RIGHT = pt(90, 40, 42, 42) # Page padding top, right, bottom, left
L = 2*U # Baseline leading
GUTTER = U # Default gutter = 2pace between the columns
# Hard coded column sizes derived from the scan.
CW = (W - PADDING_LEFT[3] - PADDING_LEFT[1] - 2*GUTTER)/3
# Construct the grid pattern. 
# Last value None means that there is no gutter running inside the right padding.
GRID_X = ((CW, GUTTER), (CW, GUTTER), (CW, 0))

CC = color(1, 1, 1, 0.6)

# Classic Berthold type specimen
# Path to the scan, used to show at first page of this document.
BERTHOLD_PATH = 'resources/BertholdBodoniOldFace#152.pdf'

# Sample glyphs set in bottom right frame. Automatic add a spacing between all characters.
GLYPH_SET = ' '.join(u'ABCDEFGHIJKLMNOPQRSTUVWXYZ&$1234567890abcdefghijklmnopqrstuvwxyz.,-‘:;!?')

# Export in _export folder that does not commit in Git. Force to export PDF.
if SHOW_GRID:
    EXPORT_PATH_PDF = '_export/Berthold-Grid.pdf' 
    EXPORT_PATH_PNG = '_export/Berthold-Grid.png' 
else:
    EXPORT_PATH_PDF = '_export/Berthold-%s.pdf' % FAMILIES[0].name 
    EXPORT_PATH_PNG = '_export/Berthold-%s.png' % FAMILIES[0].name 

# Some parameters from the original book
PAPER_COLOR = color(rgb=0xFEFEF0) # Approximation of paper color of original specimen.
RED_COLOR = color(rgb=0xAC1E2B) # Red color used in the original specimen

def getCapitalizedWord(l):
    u"""Select a random word from the hyphenation dictionary for this language."""
    if not l in WORDS and l < 100: # If the length does not exist, try larger
        return getCapitalizedWord(l+1)[:-1]
    return choice(WORDS[l]).capitalize()

def getCapWord(l):
    return getCapitalizedWord(l).upper()
    
def getShortWordText():
    u"""Answer all words of 3, 4, 5, 6 and shuffle them in a list."""
    shortWords = ' '.join(SHORT_WORDS[:40])
    shuffle(SHORT_WORDS)
    return shortWords.lower().capitalize()
    
def buildSpecimenPages(doc, family, pn):
    """Build the specimen for the family, one page per style."""
    for font in family.getFonts():
        pn = buildSpecimenPage(doc, family, font, pn)
        if pn >= MAX_PAGES:
            break
    return pn
   
def makePage1(page, font):
    # Title as 2-letter abbreviation of the family name, as in Berthold original
    style = dict(font=font, fontSize=pt(24))
    bs = context.newString(font.info.familyName[:2].capitalize(), style=style)
    newTextBox(bs, parent=page, conditions=[Left2Left(), Top2SideTop()], 
        yAlign=BOTTOM)

    """
    border = dict(stroke=blackColor, strokeWidth=pt(0.5))
    r = newRect(parent=page, conditions=[Fit()], padding=0, fill=CC,
        yAlign=BOTTOM)
    
    fullName = '%s %s' % (font.info.familyName, font.info.styleName)
    style = dict(font=font, fontSize=pt(24), xTextAlign=CENTER)
    bs = context.newString(fullName.upper(), style=style)
    newTextBox(bs, parent=r, borderTop=border, borderBottom=border, margin=0, padding=0,
        h=34,
        conditions=[Left2Left(), Top2Top(), Fit2Width()])
    
    c1 = newRect(parent=r, w=CW, conditions=[Left2Left(), Float2Top(), Fit2Height()], fill=CC)
    c2 = newRect(parent=r, w=CW, conditions=[Left2Col(2), Float2Top(), Fit2Height()], fill=CC)
    c3 = newRect(parent=r, w=CW, conditions=[Left2Col(3), Float2Top(), Fit2Height()], fill=CC)
    
    """
    
def makePage2(page, font):
    border = dict(stroke=blackColor, strokeWidth=pt(0.5))
    r = newRect(parent=page, conditions=[Fit()])

    fullName = '%s %s' % (font.info.familyName, font.info.styleName)
    style = dict(font=font, fontSize=pt(24), xTextAlign=CENTER)
    bs = context.newString(fullName.upper(), style=style)
    newTextBox(bs, parent=r, borderTop=border, borderBottom=border, margin=0, padding=0,
        conditions=[Left2Left(), Top2Top(), Fit2Width()])
         
def makeDocument(font):
    u"""Create the main document in the defined size with a couple of automatic empty pages."""

    # Build 4 pages, two for the original scan, the two for the generated version.
    doc = Document(w=W, h=H, title='Variable Font Sample Page', 
        context=context, gridX=GRID_X, fontSize=24)
    
    # Get default view from the document and set the viewing parameters.
    view = doc.view
    view.padding = 0 # For showing cropmarks and such, make > mm(20) or inch(1).
    view.showCropMarks = True # Won't show if there is not padding in the view.
    view.showFrame = SHOW_FRAMES # No frame in case PAPER_COLOR exists to be shown.
    view.showPadding = SHOW_FRAMES # No frame in case PAPER_COLOR exists to be shown.
    view.showRegistrationMarks = True
    view.showOrigin = True # Show position of xAlign and yAlign
    view.showBaselines = set([BASE_LINE, BASE_INDEX_LEFT])
    view.showGrid = DEFAULT_GRID # Show GRID_X lines
    view.showInfo = True # Show file name and date of the document
    view.showTextOverflowMarker = False # Don't show marker in case Filibuster blurb is too long.
     
    page = doc[1]
    # During development, draw the template scan as background
    # Set z-azis != 0, to make floating elements not get stuck at the background
    page.padding = {True: PADDING_LEFT, False: PADDING_RIGHT}[page.isLeft]        
    page.bleed = pt(6)
    if SHOW_TEMPLATE:
        newImage(BERTHOLD_PATH, index=1, parent=page, conditions=[Fit2Sides()])
    else:
        newRect(parent=page, fill=PAPER_COLOR, yAlign=BOTTOM, conditions=[Fit2Bleed()])
    makePage1(page, sampleFont)
    
    print(doc.solve())
    
    return doc

doc = makeDocument(sampleFont)
doc.export(EXPORT_PATH_PDF) 
  
print('Done')
