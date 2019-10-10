H = 850
W = 652
x = 100
y = 100
w = 200
h = 300
box = (x, H - y - h, w, h)
fill(None)
stroke(1, 0, 0)
rect(*box)
stroke(None)
fill(0, 0, 0)
fontSize(14)
hyphenation(True)

# TODO: test with Bezier path.

tb = textBox("""The 25-storey Jumeirah Beach Hotel, with its distinctive design in the shape of a wave, has become one of the most successful hotels in the world.
Located on Jumeirah Beach, this well-known hotel offers a wonderful holiday experience and a variety of pleasurable activities. The many restaurants, bars and cafés, daily live entertainment and sports facilities will keep you entertained, whilst children will have a great time at the Sinbad’s Kids’ Club or Wild Wadi WaterparkTM which is freely accessible through a private gate.""", box)

# Overflow.
print(type(tb))
print(len(tb))
print(tb)
