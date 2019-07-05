# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
# -----------------------------------------------------------------------------
#
#     SheetsOfCards.py
#
#     This script generates a variation of corporare identities, only to
#     the level what is needed to create a set of similar but not identical
#     business cards, and put them together on a sheet of given size with
#     registration and cropmarks.
#
#     Main input parameters
#     • Typographic styles (including layout styles)
#     • Theme (including corporate identity color)
#     • Optional image(s) and/or logo for front and back
#     • List of name records (dictionaries), otherwise filled with random names.
#
#     Main output parameters
#     • Size of business card
#     • Size of output paper

from random import choice, random

# Getting the current context, which is DrawBotContext if running this script
# from within DrawBot. But it can also run inside a webserver, where it
# likely will be a FlatContext
from pagebot.contexts import getContext
# Blob random text for content in case no name records are given
from pagebot.contributions.filibuster.blurb import blurb
# Import the generic Publication class, that ours will inherit from.
from pagebot.publications.publication import Publication 
# Get all types of elements, constants and conditions.
from pagebot.constants import *
from pagebot.conditions import *
from pagebot.elements import * 
# Import base themes to use as template and alter where necessary.
from pagebot.themes import ThemeClasses
# Get needed DateTime generator
from pagebot.toolbox.dating import now
# Import the measure units that we need
from pagebot.toolbox.units import inch, pt, mm, em, p
# Import color stuff, for what is not supplied by the theme
from pagebot.toolbox.color import blackColor, color
# Font findings functions
from pagebot.fonttoolbox.objects.font import findFont

context = getContext()

# =============================================================================
#    BusinessCard and the Sheet are separate “Publications”.
# .............................................................................

class CorporateIdentity(Publication):
    """Holding abstract design and typographic parameters, that then generate
    different kinds of publications as export."""

class BaseBusinessCard(Publication):
    """Holding the Document instance that holds a single page with a
    business card. To be placed as a group of other cards by the SheetOfCards."""
    def __init__(self, idData=None, person=None, **kwargs):
        Publication.__init__(self, **kwargs)
        self.idData = idData or {}
        self.person = person or {}

class LogoTopLeft_BusinessCard(BaseBusinessCard):
    """
    """
    def __init__(self, **kwargs):
        BaseBusinessCard.__init__(self, **kwargs)
        context = self.doc.context
        mood = self.idData['theme'].mood
        style = mood.getStyle('logo')
        bs = context.newString(self.idData['name'], style=style)
        tw, th = bs.size
        newTextBox(bs, parent=self, w=tw, fill=mood.logo_fill,
        	conditions=[Right2Right(), Float2TopSide()])
        bodyStyle = mood.getStyle('body')
        captionStyle = mood.getStyle('caption')
        bs = context.newString(self.person['name'], style=bodyStyle)
        bs += context.newString('\n'+self.person['position'], style=captionStyle)
        bs += context.newString('\n\n' + self.person['addressStreet'], style=bodyStyle)
        bs += context.newString('\n' + self.person['addressCity'], style=bodyStyle)
        newTextBox(bs, parent=self, fill=mood.logo_fill,
        	conditions=[Fit2Width(), Middle2Middle()])

class SheetOfCards(Publication):
    """Hold the Document instance that generates a sheet of BusinessCard
    instances."""
    # Standard "tetris" path of elements, to close up on top-left.
    CONDITIONS = [Right2Right(), Float2Top(), Float2Left()]

    def newCard(self, w, h, idData, person):
        page = self.document.getLastPage()
        bc = LogoTopLeft_BusinessCard(parent=page, 
                idData=idData, person=person,
            w=w, h=h, margin=p(0.5), 
            conditions=self.CONDITIONS)
        bc.showCropmarks = True
        bc.showRegistrationMarks = True
        page.solve()
        # If we managed to fit it on the same page, then keep it.
        # Otherwise move it to a next page. 
        if bc.bottom < 0:
        	page = page.next
        	page.appendElement(bc)


    
# =============================================================================
#    Sampled identities
#
#     Create random input data for identities and name records
# .............................................................................

for themeName in ThemeClasses.keys():
    pass
    #print(themeName)

def companyName():
    name = blurb.getBlurb('business_name')
    return name[0].upper() + name[1:]

def personRecord():
    return dict(
        name=blurb.getBlurb('name'), 
        position=blurb.getBlurb('position'),
        addressStreet=blurb.getBlurb('address_street_line'),
        addressCity=blurb.getBlurb('address_city_line'),
    )

def getPersonRecords(count):
    persons = []
    for n in range(count):
        persons.append(personRecord())
    return persons


PERSON_COUNT = 27
ID_COUNT = 5
ID_DATA = []

themeNames = list(ThemeClasses.keys())

for n in range(ID_COUNT):
    ID_DATA.append(dict(name=companyName(), theme=ThemeClasses[choice(themeNames)]()))

for idData in ID_DATA:
    # For all the identities, create a sheets with filled business cards

    name = idData['name']
    theme = idData['theme']
    theme.selectMood('light')
    mood = theme.mood
    style = mood.getStyle('logo')
    style['font'] = 'Upgrade-Medium'
    style['fontSize'] = style['leading'] = pt(18)
    #style['fill'] = color(spot=300)
    style['textFill'] = mood.getStyle('h1')['textFill']

    style = mood.getStyle('body')
    style['font'] = 'Upgrade-Regular'
    style['leading'] = em(1.1)
    style['xTextAlign'] = CENTER

    style = mood.getStyle('caption')
    style['font'] = 'Upgrade-Italic'
    style['leading'] = em(1)
    style['xTextAlign'] = CENTER

    ci = CorporateIdentity(name=name, theme=theme)

    w, h = BusinessCard
    sheetH, sheetW = A4

    sheet = SheetOfCards(w=sheetW, h=sheetH, name=name, theme=theme)
    sheetDoc = sheet.newDocument(w=sheetW, h=sheetH, padding=p(4, 3, 5, 3))
    persons = getPersonRecords(PERSON_COUNT)

    for person in persons:
        sheet.newCard(w=w, h=h, idData=idData, person=person)

    sheetDoc.export('_export/BusinessCards-%s.pdf' % name.replace(' ','-'))

# =============================================================================
#    Create a series of identities, as input data forExport to PDF or other file formats
# .............................................................................

#doc.export('_export/TheVariableGlobe.pdf')

