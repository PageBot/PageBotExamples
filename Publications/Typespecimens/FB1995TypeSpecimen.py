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
#     FB1995TypeSpecimen.py
#
#     This scripts generates a look-alike revival type specimen with an interpretation
#     of the “Font Bureau Type Specimen“ of 1995.
#
#     For educational purpose in using PageBot, almost every line of code has been commented.
#

import os # Import standard libary for accessing the file system.
from random import choice, shuffle, random # Used for random selection of sample words

from pagebot import getContext # Decide if running in DrawBot or Linux-Flat
context = getContext()

from pagebot.toolbox.units import inch, pt, em
from pagebot.toolbox.color import color

from pagebot.constants import LEFT, RIGHT, CENTER # Import some measure and alignments constants.
from pagebot.document import Document # Overall container class of any PageBot script
from pagebot.fonttoolbox.objects.family import getFamily # Access to installed fonts
from pagebot.elements import newRect, newTextBox, newImage, newLine # Used elements in this specimen
from pagebot.toolbox.transformer import path2FontName # Convenient CSS color to PageBot color conversion
from pagebot.toolbox.hyphenation import wordsByLength # Use English hyphenation dictionary as word selector
from pagebot.conditions import * # Import layout conditions for automatic layout.
from pagebot.contributions.filibuster.blurb import Blurb

# Debugging switches
SHOW_FRAMES = False # True shows page and padding frames.
SHOW_TEMPLATE = False # True shows the FB Specimen scan at the back of every page to show alignment.
SHOW_GRID = False # Show page grid and elements backgrounds in opaque colors.

if SHOW_GRID: # Some debugging colors, used when SHOW_GRID is on.
    DEBUG_COLOR0 = (0.7, 0.3, 0.7, 0.2)
    DEBUG_COLOR1 = (0.3, 0.3, 0.7, 0.2)
    DEBUG_COLOR2 = (0.7, 0.3, 0.3, 0.2)
    DEBUG_COLOR3 = (0.3, 0.7, 0.3, 0.2)    
else: # Otherwise ignore the background colors of the column elements.
    DEBUG_COLOR0 = DEBUG_COLOR1 = DEBUG_COLOR2 = DEBUG_COLOR3 = None
    
blurb = Blurb()
    
# Basic page metrics.
U = pt(8) # Page layout units, to unite baseline grid and gutter.
W = inch(6.34 * 2) # Draw as spread, as page view does not support them (yet)
H = inch(10) # Copy size from the original specimen.
# Hard coded padding sizes derived from the scan.
PT, PR, PB, PL = PADDING = pt(23, 34, 28, 28) # Page padding top, right, bottom, left
L = 2*U # Baseline leading
G = 2*U # Default gutter = space between the columns
GM = 7*U # Gutter in middle of the spread.

# Hard coded column sizes derived from the scan.
C = (W - PL - PR - GM - 4*G)/6
C3 = 3*C + 2*G
# Construct the grid pattern. 
# Last value None means that there is no gutter running inside the right padding.
GRID_X = ((C, G), (C, G), (C, GM), (C, G), (C, G), (C, None))
GRID_Y = ((H - PT - PB, None),)

# “Font Bureau Type Specimen“ of 1995.
# Path to the scan, used to show at first page of this document.
FB_PATH_L = 'images/FB1995TypeSpecimen-Proforma-L.jpg'
FB_PATH_R = 'images/FB1995TypeSpecimen-Proforma-R.jpg'

# Build the specimen pages for the font names that include these patterns.
FAMILIES = (
    getFamily('Upgrade'),
    #getFamily('Proforma'),
    #getFamily('Bitcount'),
    #getFamily('Bungee'), 
    #getFamily('Roboto'), 
    #getFamily('AmstelvarAlpha')
)
#print('Proforma', FAMILIES[1].getStyles().keys())

#labelFamily = getFamily('Roboto')
labelFamily = getFamily('Upgrade')
labelFont = labelFamily.findRegularFont() # Ask family to find the most regular font.
labelItalicFont = labelFamily.findRegularFont(italic=True) # Ask family to find the most regular font.

labelStyle = dict(font=labelFont.path, fontSize=7, leading=em(1), paragraphTopSpacing=4, paragraphBottomSpacing=4)
fontSetStyle = dict(font=labelItalicFont.path, fontSize=9, xTextAlign=CENTER, leading=em(1.25))
charSetStyle = dict(font=labelFont.path, fontSize=10, xTextAlign=CENTER, leading=em(1.25))
descriptionStyle = dict(font=labelFont.path, fontSize=12, xTextAlign=CENTER, leading=em(1.25))

# Sample glyphs set in bottom right frame. Automatic add a spacing between all characters.
GLYPH_SET = """ABCDEFGHIJKLMNOPQRSTUVWXYZ&$1234567890abcdefghijklmnopqrstuvwxyz.,-‘:;!?\nAÀÁÂÃÄÅĀĂĄǺBCÇĆĈĊČDĎEÈÉÊËĒĔĖĘĚFGĜĞĠĢǦHĤIÌÍÎÏĨĪĬĮİJĴKĶLĹĻĽMNÑŃŅŇOÒÓÔÕÖŌŎŐPQRŔŖŘSŚŜŞŠȘTŢŤȚUÙÚÛÜŨŪŬŮŰŲVWŴẀẂẄXYÝŶŸỲZŹŻŽÆǼÐØǾÞĐĦĿŁŊŒŦΔaàáâãäåāăąǻbcçćĉċčdďeèéêëēĕėęěfgĝğġģǧhĥiìíîïĩīĭįjĵkķlĺļľmnñńņňoòóôõöōŏőpqrŕŗřsśŝşšștţťțuùúûüũūŭůűųvwŵẁẃẅxyýÿŷỳzźżžªºßæǽðøǿþđħıŀłŋœŧƒȷəﬁﬂ0123456789¼½¾₀₁₂₃₄₅₆₇₈₉²³¹⁰⁴⁵⁶⁷⁸⁹_-–—―‒([{‚„)]}!"#%&'*,.//:;?@\¡·¿†‡•…‰′″£¤¥€¦§©®°¶℗℗™◊✓"""

# Export in _export folder that does not commit in Git. Force to export PDF.
DO_OPEN = False
if SHOW_GRID:
    EXPORT_PATH_PDF = '_export/FB1995TypeSpecimen-Grid.pdf' 
    EXPORT_PATH_PNG = '_export/FB1995TypeSpecimen-Grid.png' 
else:
    EXPORT_PATH_PDF = '_export/FB1995TypeSpecimen.pdf' 
    EXPORT_PATH_PNG = '_export/FB1995TypeSpecimen.png' 

# Some parameters from the original book
PAPER_COLOR = color(rgb=0xFEFEF7) # Approximation of paper color of original specimen.

# Get the dictionary of English ("en" is default language), other choice is Dutch ("nl").
# Danish could be made available for PageBot if requested.
# Other hyphenation tables are appreciated to be added to PageBot.
# WORDS key is the word length in character count and the values are lists words of
# equal length.
LANGUAGE = 'en' #'en'
WORDS = wordsByLength(LANGUAGE)
SHORT_WORDS = WORDS[3]+WORDS[4]+WORDS[3]+WORDS[4]+WORDS[3]+WORDS[4]+WORDS[5]+WORDS[6]
shuffle(SHORT_WORDS)

def getCapitalizedWord(l):
    u"""Select a random word from the hyphenation dictionary for this language."""
    if not l in WORDS:
        return None
    return choice(WORDS[l]).capitalize()

def getCapWord(l):
    word = getCapitalizedWord(l).upper()
    if word is not None:
        return word.upper()
    return None
    
def getShortWordText():
    u"""Answer all words of 3, 4, 5, 6 and shuffle them in a list."""
    shortWords = ' '.join(SHORT_WORDS[:40])
    shuffle(SHORT_WORDS)
    return shortWords.lower().capitalize()
 
def getWeightNames(family):
    # Collect all weight names in increasing order.
    weightClasses = family.getWeights()
    weightNames = ''
    index = 0
    for weightClass, fonts in sorted(weightClasses.items()):
        weightName = '[%d] ' % weightClass
        for font in fonts:
            if index > 24:
                return weightNames
            weightName += ' ' + path2FontName(font.path)
            index += 1
        weightNames += ' ' + weightName
    return weightNames
         
def buildSpecimenPages(page, family):
    page.padding = PADDING
    page.gridX = GRID_X
    pageTitle = family.name
    # Add filling rectangle for background color of the old paper book.
    # Set z-azis != 0, to make floating elements not get stuck at the background
    newRect(z=-10, w=W, h=H, parent=page, fill=PAPER_COLOR)
    # During development, draw the template scan as background
    # Set z-azis != 0, to make floating elements not get stuck at the background
    if SHOW_TEMPLATE:
        newImage(FB_PATH_L, x=0, y=0, z=-10, w=W/2, parent=page)
        newImage(FB_PATH_R, x=W/2, y=0, z=-10, w=W/2, parent=page)
    
    # Left and right family name the current font.
    titleBs = context.newString(pageTitle, 
                                style=dict(font=labelFont.path, fontSize=16, xTextAlign=LEFT, textFill=0))
    titleBox = newTextBox(titleBs, parent=page, h=3*U, w=C3, 
               conditions=[Top2Top(), Left2Left()],
               fill=DEBUG_COLOR0)

    titleBs = context.newString(pageTitle, 
                                style=dict(font=labelFont.path, fontSize=16, xTextAlign=RIGHT, textFill=0))
    titleBox = newTextBox(titleBs, parent=page, h=3*U, w=C3,
               conditions=[Top2Top(), Right2Right()],
               fill=DEBUG_COLOR0)

    lineL = newLine(parent=page, w=C3, h=1, mb=U, strokeWidth=1, stroke=0, conditions=(Float2Top(), Left2Left()))
    lineR = newLine(parent=page, w=C3, h=1, mb=U, strokeWidth=1, stroke=0, conditions=(Float2Top(), Right2Right()))
    
    descriptionFont = family.findRegularFont()
    description = ''
    if descriptionFont.info.description:
        description += descriptionFont.info.description + ' '
    if descriptionFont.info.trademark:
        description += descriptionFont.info.trademark
    if description:
        description = context.newString(description, style=descriptionStyle)
        _, descriptionH = context.textSize(description, w=C3)
    else:
        descriptionH = 0
        
    # Get the weightClass-->fonts dictionary, sorted by weight.
    weightClasses = family.getWeights()
    
    # Text samples on the right
    y = 300#lineR.bottom 
    for weightClass, fonts in sorted(weightClasses.items()):
        for font in fonts:
            if font.isItalic():
                continue
            sample = context.newString(blurb.getBlurb('article'), style=dict(font=font.path, fontSize=9, leading=em(1.1)))
            h = H/len(family)+L
            newTextBox(sample, parent=page, w=C3, h=h, conditions=(Right2Right(), Float2Top()),
                fill=DEBUG_COLOR1)
            y -= h
            if y <= PB + descriptionH:
                break

    if description:
        newTextBox(description, parent=page, w=C3, h=descriptionH, 
                   conditions=(Right2Right(), Bottom2Bottom()),
                   fill=DEBUG_COLOR1)
 
    weightNames = getWeightNames(family)            
 
    charSetString = context.newString(weightNames + '\n\n', style=fontSetStyle)
    charSetString += context.newString(GLYPH_SET, style=charSetStyle)
    _, charSetStringH = context.textSize(charSetString, w=C3)
            
    newTextBox(charSetString, parent=page, w=C3, h=charSetStringH, conditions=(Left2Left(), Bottom2Bottom()))


    page.solve() # So far with conditional placement. 
    
    # It's easier for this example to position the elements by y-coordinate now, because there
    # is mismatch between the position of the pixel image of the lines and the content of text
    # boxes. Although it is possible to build by floating elements or by on single text, which
    # will show in another proof-revival example.
    
    y = lineL.bottom-U # Position at where this went to by solving the layout conditions.
    # Stacked lines on the left, by separate elements, so we can squeeze them by pixel image size.
    for n in range(100): # That's enough
        headline = blurb.getBlurb('_headline', cnt=choice((2,3,4,4,4,4,4,5,6,7,8)))
        if random() <= 0.2:
            headline = headline.upper()
        stackLine = context.newString(headline,
            style=dict(font=choice(context.installedFonts()), leading=em(-0.2),
                       paragraphTopSpacing=0, paragraphBottomSpacing=0
            ), w=C3, pixelFit=False)
        _, by, bw, bh = stackLine.bounds()
        tw, th = context.textSize(charSetString)
        if y - bh < PB + th: # Reserve space for glyph set
            break # Filled the page.
        newTextBox(stackLine, parent=page, x=PL, y=y-bh-by-U, w=C3, h=th+2, fill=DEBUG_COLOR1)
        y -= bh + by + U
        page = page.nextc
    
def makeDocument(families):
    u"""Create the main document in the defined size with a couple of automatic empty pages."""
    # Calculate the amount of pages to create
    numPages = len(families)+1 # One family per spread.
        
    doc = Document(w=W, h=H, title='Variable Font Sample Page', originTop=False, startPage=0, 
        autoPages=numPages, context=context, gridX=GRID_X, gridY=GRID_Y)

    # Get default view from the document and set the viewing parameters.
    view = doc.view
    view.padding = inch(0.5) # For showing cropmarks and such, make >=20*MM or INCH.
    view.showPageCropMarks = True # Won't show if there is not padding in the view.
    view.showPageFrame = SHOW_FRAMES # No frame in case PAPER_COLOR exists to be shown.
    view.showPagePadding = SHOW_FRAMES # No frame in case PAPER_COLOR exists to be shown.
    view.showPageRegistrationMarks = True
    view.showGrid = SHOW_GRID # Show GRID_X lines
    view.showPageNameInfo = True # Show file name and date of the document
    view.showTextOverflowMarker = False # Don't show marker in case Filibuster blurb is too long.

    # Build the pages for all fonts that include one of these patterns.
    for family in families:
        page = doc[1]
        page.ch = pt(0) # No vertical grid
        page.padding = PADDING
        page.gridX = GRID_X
        newImage(FB_PATH_L, x=0, y=0, w=W/2, parent=page)
        newImage(FB_PATH_R, x=W/2, y=0, w=W/2, parent=page)
    
        buildSpecimenPages(page, family)

    doc.solve()
    
    return doc

doc = makeDocument(FAMILIES)
doc.export(EXPORT_PATH_PDF) 
doc.export(EXPORT_PATH_PNG) 
if DO_OPEN:
    os.system(u'open "%s"' % EXPORT_PATH)
  
print('Done')
