
from flat import rgb, font, shape, strike, document, paragraph, text
from pagebot.fonttoolbox.objects.font import findFont

# Get the PageFont instance
pbFont = findFont('PageBot-Regular')
fontSize = 200
red = rgb(255, 0, 100)
black = rgb(0, 0, 0)
flatFont = font.open(pbFont.path)

figure = shape().stroke(black).width(2.5)
strk = strike(flatFont).color(red).size(fontSize, tracking=0.1)

# Flat has origin in top-left
flatDoc = document(1000, 1300, 'pt')
flatPage = flatDoc.addpage()

x = 50
y = 100
flatPage.place(figure.rectangle(x, y, 20, 20))
placedText = flatPage.place(strk.text('textV.W.Hkpx'))
placedText.position(x, y) # Placing on top of text
# Placing as frame seems to give not control on vertical position.
placedText = flatPage.place(strk.text('Hkpx'))
placedText.frame(x+400, y, placedText.width, fontSize)

y = 600
flatPage.place(figure.rectangle(x, y-20, 20, 20))
placedText = flatPage.place(strk.text('Hkpx'))
ascender = fontSize*pbFont.info.typoAscender/pbFont.info.unitsPerEm
# Placing as frame seems to give not control on vertical position.
#placedText.position(x, 400-) # Placing on baseline
placedText.frame(x, y-ascender, placedText.width, fontSize)

# Mixing spans in a paragraph to make baselines the same.
y = 900
flatPage.place(figure.rectangle(x, y-20, 20, 20))
spans = []
for fontSize in range(50, 300, 50):
    strk = strike(flatFont).color(red).size(fontSize)
    spans.append(strk.span('Hn'))
par = [paragraph(spans)]
placedText = flatPage.place(text(par))
# Placing as frame seems to give not control on vertical position.
#placedText.position(x, 400-) # Placing on baseline
ascender = fontSize*pbFont.info.typoAscender/pbFont.info.unitsPerEm
placedText.frame(x, y-ascender, placedText.width, fontSize)
flatDoc.pdf('_export/E00_TextPosition.pdf')

print('Done')