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
#     AdServer.py
#
#     Using https://www.tornadoweb.org
#
#     Using the PageBot Server to host a advertizement (Publication) generator.
#     URL parameters direct the type and content of the ad.
#
#     http://localhost:8888
#
from tornado.web import StaticFileHandler
from pagebot.server.tornadoserver.baseserver import BasicRequestHandler, RequestData, BaseServer 
#from pagebot.publications.websites.nanosite.nanosite import NanoSite

class RequestHandler(BasicRequestHandler):
    def get(self, *args):
        """Figure out how or handle the request and where to get content from.
        """
        requestData = RequestData(self.request.uri) # Split path parts and arguments
        self.write('<h1>path: %s</h1>' % requestData.path)
        self.write('<h2>uri: %s</h2>' % requestData.uri)
        self.write('<h2>filePath: %s</h2>' % requestData.filePath)
        self.write('<h2>args: %s</h2>' % requestData.args)
        self.write('<h3>requestHandler id: %s</h3>' % id(self))
        for imagePath in ('IMG_1734.jpg', 'IMG_1764.jpg', 'IMG_3740.jpg'):
            self.write('<h1><a href="/%s/par1-123/par2-xyz">' % imagePath.split('.')[0])
            self.write('<img src="/images/%s" width="500"></a>' % imagePath)

class AdServer(BaseServer):

    def getRequestHandlers(self):
        handlerData = {'path': './images'}
        return [
           ('/(.*.ico)', StaticFileHandler, handlerData),
           ('/images/(.*)', StaticFileHandler, handlerData),
           ('/(.*)', RequestHandler),
        ] # http://localhost:8889/<args>


server = AdServer(port=8993)
server.run()
