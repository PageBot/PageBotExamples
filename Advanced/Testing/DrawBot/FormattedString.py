fontSize(20)
font('Helvetica')
print('global leading %s' % fontLeading())
print('global line height %s' % fontLineHeight())

'''
print(fontXHeight())
print(fontCapHeight())
print(fontAscender())
print(fontDescender())
print(fontFilePath())
'''

leading = 1
fontSize = 100
lineHeight = leading * fontSize
s = FormattedString('bla', font='Helvetica', fontSize=fontSize, lineHeight=lineHeight, fill=(0.4,0.5,0.2))


fontSize = 300
#lineHeight = fontSize * leading
s.fontSize(fontSize)
s.lineHeight(lineHeight) # Keeps value of first part.
s.font('Helvetica-Bold')
s.fill(0.3, 0.2, 0.9)
s += 'bla2'


text(s, (0,lineHeight))

print('formatted string leading %s' % s.fontLeading())
print('formatted string size %s' % s.size())
print('formatted string line height %s' % s. fontLineHeight())
'''
print(s.fontAscender())
print(s.fontDescender())
'''
w, h = s.size()
fill(None)
stroke(0)
rect(0, lineHeight, w, h)

from AppKit import NSFont
font = NSFont.fontWithName_size_("Helvetica", 12)
print(font.leading())
