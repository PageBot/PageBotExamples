# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T  E X A M P L E S
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
from pagebot import getContext
# Blob random text for content in case no name records are given
from pagebot.contributions.filibuster.blurb import Blurb
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
from pagebot.toolbox.color import blackColor, color, noColor
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

        bodyStyle = mood.getStyle('body')
        captionStyle = mood.getStyle('caption')
        logoStyle = mood.getStyle('logo')

        page = self.getDocument(name='BaseBusinessCard')[1]
        page.padding = self.padding = p(1)

        bs = context.newString(self.idData['logo'], style=logoStyle)
        bs += context.newString(' '+self.idData['name'], style=bodyStyle)
        tw, th = bs.size
        e = newText(bs, parent=page, w=tw, stroke=noColor, fill=0.7,
        	conditions=[Left2Left(), Top2Top()])
        print('===', e.x, tw, th, e.w, e.h)

        bs = context.newString(self.person['name'], style=bodyStyle)
        bs += context.newString('\n'+self.person['position'], style=captionStyle)
        bs += context.newString('\n\n'+self.person['addressStreet'], style=captionStyle)
        bs += context.newString('\n'+self.person['addressCity'], style=captionStyle)
        bs += context.newString('\n'+self.person['addressTelephone'], style=captionStyle)
        newText(bs, parent=page, fill=noColor, stroke=noColor,
        	conditions=[Left2Left(), Fit2Width(), Middle2Middle()])

        self.showFrame = True
        self.showPadding = True
        self.showCropMarks = True
        self.showRegistrationMarks = True
        self.viewCropMarkSize=pt(16)
        self.viewCropMarkDistance=pt(8)

        page.solve()
        print('+++', e.x)

class SheetOfCards(Publication):
    """Hold the Document instance that generates a sheet of BusinessCard
    instances."""
    # Standard "tetris" path of elements, to close up on top-left.
    CONDITIONS = [Right2Right(), Float2Top(), Float2Left()]

    def newCard(self, w, h, idData, person):
        page = self.document.getLastPage()
        page.padding = 0
        bc = LogoTopLeft_BusinessCard(parent=page,
                idData=idData, person=person,
            w=w, h=h, margin=(page.pw - w*3 - 1)/6,
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
    if 0:
        name = blurb.getBlurb('business_name')
        name = name[0].upper() + name[1:]
        logo = ''
        for part in name.split(' '):
            logo += part[0].upper()
    else:
        name = ''
        logo = 'LOGO'
    return logo, name

def personRecord():
    return dict(
        name=blurb.getBlurb('name'),
        position=blurb.getBlurb('position'),
        addressStreet=blurb.getBlurb('address_street_line'),
        addressCity=blurb.getBlurb('address_city_line'),
        addressTelephone=blurb.getBlurb('telephone'),
    )

def getPersonRecords(count):
    persons = []
    for n in range(count):
        persons.append(personRecord())
    return persons


PERSON_COUNT = 9
ID_COUNT = 1
ID_DATA = []

themeNames = list(ThemeClasses.keys())

for n in range(ID_COUNT):
    logo, name = companyName()
    theme = ThemeClasses[choice(themeNames)]()
    ID_DATA.append(dict(logo=logo, name=name, theme=theme))

for idData in ID_DATA:
    # For all the identities, create a sheets with filled business cards

    name = idData['name']
    theme = idData['theme']
    theme.selectMood('light')
    mood = theme.mood
    style = mood.getStyle('logo')
    style['font'] = 'Upgrade-Bold'
    style['fontSize'] = pt(32)
    style['leading'] = em(0.8)

    #style['fill'] = color(spot=300)
    style['textFill'] = mood.logo = color(spot=300)

    style = mood.getStyle('body')
    style['font'] = 'Upgrade-Medium'
    style['leading'] = em(1.2)
    style['xTextAlign'] = CENTER

    style = mood.getStyle('caption')
    style['font'] = 'Upgrade-Italic'
    style['leading'] = em(1.1)
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

