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
#     UseProofing.py
#
from pagebot import getContext
from pagebot.toolbox.units import *
from pagebot.constants import A3
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.fonttoolbox.fontpaths import getFontPaths

font = findFont('PageBot-Regular') # PageBot demo version of TYPETR-Upgrade
H, W = A3 # Landscape, reverse W, H
PADDING = p(5)
S = 'abcdefghijklmnopqrstuvwxyz'
LEADING = 1

for contextName in ('DrawBot', 'Flat'):
	context = getContext(contextName)
	exportPath = '_export/50_UseProofing-%s.pdf' % contextName
	context.newPage(W, H)
	y = 0
	for ps in (10, 11, 12, 13, 14, 15, 16, 18, 20, 22, 24, 28, 32, 36, 40, 46, 54):
	    y += ps*LEADING/2
	    bs = context.newString(S, style=dict(font=font, fontSize=ps))
	    tw, th = bs.textSize
	    context.textBox(bs, (PADDING, H-PADDING-y, W-2*PADDING, th))

	context.saveImage(exportPath)