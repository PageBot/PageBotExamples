t = '''Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Typi non habent
claritatem insitam; est usus legentis in iis qui facit eorum claritatem. Investigationes demonstraverunt lectores legere me lius quod ii legunt saepius. Claritas est etiam processus dynamicus, qui sequitur mutationem consuetudium
lectorum. Mirum est notare quam littera gothica, quam nunc putamus parum claram, anteposuerit litterarum formas humanitatis per seacula quarta decima et quinta decima. Eodem modo typi, qui nunc nobis videntur parum clari, fiant sollemnes in futurum.'''

t2 = """The 25-storey Jumeirah Beach Hotel, with its distinctive design in the shape of a wave, has become one of the most successful hotels in the world.
Located on Jumeirah Beach, this well-known hotel offers a wonderful holiday experience and a variety of pleasurable activities. The many restaurants, bars and cafés, daily live entertainment and sports facilities will keep you entertained, whilst children will have a great time at the Sinbad’s Kids’ Club or Wild Wadi WaterparkTM which is freely accessible through a private gate."""

H = 850
W = 652
x = 100
y = 100
w = 200
h = 300
LINE = 14
fontSize(14)
l = fontLeading()
print(l)
lh = fontLineHeight()
print(lh)

box = (x, H - y - h, w, h)
fill(None)
stroke(1, 0, 0)
rect(*box)
line((x, H - y - LINE), (x+w, H - y - LINE))
line((x, H - y - LINE - lh), (x+w, H - y - LINE - lh))
line((x, H - y - LINE - 2*lh), (x+w, H - y - LINE - 2*lh))

stroke(None)
fill(0, 0, 0)

hyphenation(True)

# TODO: test with Bezier path.

tb = textBox(t2, box)

# Overflow.
print(type(tb))
print(len(tb))
print(tb)

x += w + 20
box = (x, H - y - h, w, h)
textBox(tb, box)

'''
s = 36
fontSize(s)
font('Verdana')
hyphenation(True)

p= 10
x = p
w = 600
h = 400
y0 = p
y1 = h + 2*p


overflow = textBox(t, (x, y0, w, h), align='right')
print('Overflow: %d' % len(overflow))

hyphenation(False)
baselineShift(s)
lh = 100
lineHeight(lh)
print('Line height: %d' % lh)
print('Leading: %s' % fontLeading())
print('Ascender %s' % fontAscender())
overflow = textBox(t, (x, y1, w, h), align='center')
print('Overflow: %d' % len(overflow))


fill(None)
stroke(0, 1, 0)
rect(x=x, y=y0, w=w, h=h)
rect(x=x, y=y1, w=w, h=h)
stroke(1, 0, 0)
line((x, y0+h-s), (w+x, y0+h-s))
line((x, y1 + h-s), (w+x, y1 + h-s))
'''
