# To run in DrawBot.

from pagebot.fonttoolbox.objects.font import findFont
f = findFont('Roboto-Regular')
font(f.path)
newPage(600, 600)
fontSize(200) 

print(fontAscender() - fontDescender())
txt = 'Hpxk sfsdf'
box = (0, 0, 600, 400)
w, h = textSize(txt)
print(w, h)
textBox(txt, box)

stroke(1, 0, 0)
for x, y in textBoxBaselines(txt, box):
        line((x, y), (x + w, y))
fill(None)
rect(0, 400-h, w, h)
