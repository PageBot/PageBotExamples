#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     BaseServer.py
#
#     https://www.tornadoweb.org
#
#     Running this example script, creates a local tornado web server.
#     This example "Hello world" is not using PageBot, for simplicity of the code.
#     Open with a browser on http://localhost:7777
#     Each request shows the "counter" variable, as the number of page hits.
#     Stop the server with cntr-C, before running the script again.
#
import tornado.ioloop
import tornado.web

counter = 0 # Counting the number of pages hits.

PORT = 7777 # The port that the server is listening to.

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        global counter
        self.write("Hello, %d world" % counter) # Answering the string (not even HTML)
        counter += 1

    def data_received(self):
        pass

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler), # Just listing to the main single http://localhost:7777 page.
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)
    print('Starting Tornado web application on port %s' % PORT)
    tornado.ioloop.IOLoop.current().start()
