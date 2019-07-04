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

from random import choice

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
from pagebot.toolbox.units import inch, pt, mm, em
# Import color stuff, for what is not supplied by the theme
from pagebot.toolbox.color import blackColor
# Font findings functions
from pagebot.fonttoolbox.objects.font import findFont

context = getContext()

# =============================================================================
#    BusinessCard and the Sheet are separate “Publications”.
# .............................................................................

class CorporateIdentity(Publication):
	"""Holding abstract design and typographic parameters, that then generate
	different kinds of publications as export."""

class BusinessCard(Publication):
    """Holding the Document instance that holds a single page with a
    business card. To be placed as a group of other cards by the SheetOfCards."""
    
class SheetOfCards(Publication):
    """Hold the Document instance that generates a sheet of BusinessCard
    instances."""

# =============================================================================
#    Sampled identities
# .............................................................................
for themeName in ThemeClasses.keys():
	pass
	#print(themeName)

def companyName():
	name = blurb.getBlurb('business_name')
	return name[0].upper() + name[1:]

COUNT = 2
ID_DATA = []
themeNames = list(ThemeClasses.keys())
for n in range(COUNT):
		ID_DATA.append(dict(name=companyName(), theme=ThemeClasses[choice(themeNames)]()))

for idData in ID_DATA:
	name = idData['name']
	theme = idData['theme']
	ci = CorporateIdentity(name=name, theme=theme)
	try:
		print('%s' % ci.name)
	except UnicodeEncodeError:
		for cc in ci.name:
			try:
				print('+'+cc)
			except UnicodeEncodeError:
				print('----')

# =============================================================================
#    Create a series of identities, as input data forExport to PDF or other file formats
# .............................................................................

#doc.export('_export/TheVariableGlobe.pdf')

