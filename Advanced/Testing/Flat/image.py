#!/usr/bin/env python3

from pagebot.fonttoolbox.objects.font import findFont
from pagebot.constants import A5
from pagebot.toolbox.units import pt
from pagebot.contributions.filibuster.blurb import Blurb
from flat import * # rgb, font, shape, strike, document
import random

h, w = pt(A5)
w = int(w)
h = int(h)
documentName = 'image'

d = document(w, h, 'pt')
d.meta(documentName)
p = d.addpage()

src = '../../../docs/stylewars/dondi-white-children-of-the-grave-pt3-martha-cooper.png'
im = image.open(src)
#im.resize(300, 400)
#im.invert()
im.rescale(0.4)
imw = im.width
imh = im.height
x0 = (w - imw) / 2
y0 = (h - imh) / 2
p.place(im).frame(x0, y0, imw, imh)

# Export.
export = '_export'
p.image(kind='rgb').png('%s/%s.png' % (export, documentName))
p.svg('%s/%s.svg' % (export, documentName))
d.pdf('%s/%s.pdf' % (export, documentName))
