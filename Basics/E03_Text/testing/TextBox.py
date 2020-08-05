# To run– in DrawBot.

from pagebot.fonttoolbox.objects.font import findFont
f = findFont('Roboto-Regular')
font(f.path)

X = 10
Y = -50
W = 600
H = 400
newPage(W, H)
fontSize(200) 
print(fontAscender() - fontDescender())
txt = 'Hpxk'
box = (X, Y, W, H)
w, h = textSize(txt)
print('width: %s, height: %s' % (w, h))
textBox(txt, box)

stroke(1, 0, 0)

for x, y in textBoxBaselines(txt, box):
        line((x, y), (x + w, y))

line((0, H), (X, H+Y))

fill(None)
rect(X, H + Y - h, w, h)
