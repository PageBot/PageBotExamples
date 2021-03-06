# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     ResponsivePage.py
#
#     https://www.tornadoweb.org
#     http://localhost:7778
#
import tornado.ioloop
import tornado.web

ioloop = None
counter = 0

MAX_QUERIES = 10

PORT = 7778
HTML = '<html><head><title>Responsive Page #%d</title></head><body>Hello World</body></html>'

class MainHandler(tornado.web.RequestHandler):
    """Run the web server, answer on url http://localhost:7778 
    for MAX_QUERIES, then the server stops.
    """
    def get(self):
        global ioloop, counter
        self.write(HTML % counter)
        if counter > MAX_QUERIES:
            ioloop.stop()
        counter += 1

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    global loop
    app = make_app()
    print('Starting ResponsivePage web application on port %s' % PORT)
    app.listen(PORT)
    ioloop = tornado.ioloop.IOLoop.current()
    ioloop.start()
    print('Done')

