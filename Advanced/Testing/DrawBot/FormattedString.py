fontSize(20)
font('Helvetica')
print(fontLeading())
print(fontLineHeight())
print(fontXHeight())
print(fontCapHeight())
print(fontAscender())
print(fontDescender())
print(fontFilePath())

s = FormattedString('bla', font='Helvetica', fontSize=100, fill=(0.4,0.5,0.2))

print(s.fontLeading())
print(s.fontLineHeight())
print(s.fontAscender())
print(s.fontDescender())

s.fontSize(300)
s.font('Helvetica-Bold')
s.fill(0.3, 0.2, 0.9)
s += 'bla2'

text(s, (0,0))

print(s.fontLeading())
print(s.fontLineHeight())
print(s.fontAscender())
print(s.fontDescender())


