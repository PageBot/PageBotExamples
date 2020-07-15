#!/usr/bin/env python3
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
#     E01_FindFont.py
#
#     Some examples how to find Font instances, for the given installed fonts.
#     PageBot scans through places where it can find font files.
#
from pagebot.constants import A4, EXPORT
from pagebot.document import Document
from pagebot.elements import *
from pagebot import getContext
from pagebot.toolbox.units import pt
from pagebot.fonttoolbox.objects.family import findFamily, getFamily
from pagebot.fonttoolbox.objects.font import getFont, findFont, findFonts
from pagebot.toolbox.transformer import path2FileName

FILENAME = path2FileName(__file__)

def makeFonts(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    context = getContext(contextName)
    #
    #    Installed fonts created a list of font names that are already installed.
    #    This will miss out the fonts supported inside the PageBot library.
    #    So for now, we'll just check on Verdana and Georgia,
    #    which is supposed to exist in all contexts.

    allFontNames = context.installedFonts()
    # Shows something like: Total installed fonts: 1993
    print('Total installed fonts: %d' % len(allFontNames))

    fontNames = context.installedFonts('Verda') # Context knows to find what is installed.
    # ['Verdana', 'Verdana-Bold', 'Verdana-BoldItalic', 'Verdana-Italic']
    print('Found font names:', fontNames) # Filtering on (partical) family name

    fontNames = context.installedFonts('Verdana-BoldItalic')
    # ['Verdana-BoldItalic']
    print('Found font names:', fontNames) # Filtering on full family-style name.

    fontNames = context.installedFonts(['Verdana', 'Georgia'])
    # ['Georgia', 'Georgia-Bold', 'Georgia-BoldItalic', 'Georgia-Italic', 'Verdana', 'Verdana-Bold', 'Verdana-BoldItalic', 'Verdana-Italic']
    print('Fount font names:', fontNames) # Filtering on multiple patterns as "or"

    # The PageBot method to look for fonts is find a fanily with an exact name match
    family = getFamily('Bungee') # Creates a Family instance with Font instances as style.
    # <PageBot Family Bungee (5 fonts)>
    print('Family:', family)
    print('Family style:', len(family.fonts.keys())) # Dictionary of filePath:Font

    font = getFont('Verdana-BoldItalic') # Not specific enough, needs path
    print('Font:', font)

    font = findFont('Roboto') # Not specific enounh, needs full style name.
    # None
    print('Font:', font)

    fonts = findFonts('Roboto') # Used as pattern
    # 40 Now it can find a number of fonts, fitting the pattern
    print('Fonts:', len(fonts))

    robotoRegular = findFont('Roboto-Regular') # Specific name, file name without extension.
    # <Font Roboto-Regular>
    print('Find the font:', robotoRegular)

    font = findFont('Roboto-cannot-be-found', default='Roboto-Regular')
    # <Font Roboto-Regular>
    print('Find the default by name:', font)

    font = findFont('Roboto-cannot-be-found', default=robotoRegular)
    # <Font Roboto-Regular>
    print('Answer the default font:', font)

    # Let's make a page to show all font names.

    style = dict(font='PageBot-Bold', fontSize=pt(12), textFill=0)
    bs = context.newString('Installed fonts for %s\n' % contextName, style)
    bs += context.newString('\n'.join(allFontNames))

    doc = Document(size=A4, context=context)
    page = doc[1]
    page.padding = pt(30)
    newText(bs, x=page.pl, y=page.pb, w=page.pw, h=page.ph, parent=page, stroke=(1, 0, 0))
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    makeFonts(contextName)
