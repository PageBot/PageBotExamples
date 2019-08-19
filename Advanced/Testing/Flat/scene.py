#!/usr/bin/env python3
from flat import *

m = mesh.openstl('../../../docs/3d/puzzlecube.stl')
s = scene()

mat = diffuse((1, 1, 1), emittance=None)

s.add(m, mat)
raw = s.render(100, 100)
print(raw)

d = document(100, 100, 'mm')
p = d.addpage()
#p.place(i)

p.image(kind='rgb').png('_export/scene.png')
