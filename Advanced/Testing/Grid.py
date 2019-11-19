from pagebot import getContext
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.toolbox.units import pt
from pagebot.toolbox.color import color, Color
from pagebot.fonttoolbox.objects.font import findFont

for contextName in ['DrawBot', 'Flat']:
    context = getContext(contextName)
    context.newDrawing()
    context.newPage(W, H)
    path = '_export/Grid-%s.pdf' % context.name
    context.saveImage(path)
