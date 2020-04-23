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
#     Only10PagesQuit.py
#
#     https://www.tornadoweb.org
#     
#     Running this example script, creates a local tornado web server.
#     This example "Hello world" is not using PageBot, for simplicity of the code.
#     Open with a browser on http://localhost:8880
#     Each request shows the "counter" variable, as the number of page hits.
#     Stop the server with cntr-C, before running the script again.
#     After 10 requests, the server stops.

import tornado.ioloop
import tornado.web

ioloop = None
counter = 0

PORT = 8880
MAX_QUERIES = 10

class MainHandler(tornado.web.RequestHandler):
    """For the sake of example testing, run the web server, 
    answer on url http://localhost:7777 for MAX_PAGES, 
    then the server stops.
    """
    def get(self):
        global counter, ioloop
        self.write("Hello, %d worlds" % counter)
        counter += 1
        if counter > MAX_QUERIES:
            ioloop.stop()

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    global loop
    app = make_app()
    app.listen(PORT)
    ioloop = tornado.ioloop.IOLoop.current()
    ioloop.start()
    print('Done')

