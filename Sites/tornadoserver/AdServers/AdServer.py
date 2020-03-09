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
from pagebot.publications.websites.nanosite.nanosite import NanoSite

class RequestHandler(BasicRequestHandler):
    def initialize(self, path, publication):
        self.path = path
        self.publication = publication

    def get(self, path):
        """Figure out how or handle the request and where to get content from.
        """
        requestData = RequestData(self.request.uri) # Split path parts and arguments
        self.write('<html><head>\n')
        self.write('<link media="all" rel="stylesheet" href="/css/nanostyle_py.css"/>\n')
        self.write('</head><body>\n')
        self.write('<h1>path: %s</h1>\n' % requestData.path)
        self.write('<h2>uri: %s</h2>\n' % requestData.uri)
        self.write('<h2>filePath: %s</h2>\n' % requestData.filePath)
        self.write('<h2>args: %s</h2>\n' % requestData.args)
        self.write('<h3>requestHandler id: %s</h3>\n' % id(self))
        self.write('<h3>publication: %s %d</h3>\n' % (self.publication.__class__.__name__, id(self.publication)))
        for imagePath in ('IMG_1734.jpg', 'IMG_1764.jpg', 'IMG_3740.jpg'):
            self.write('<h1><a href="/%s/par1-123/par2-xyz">\n' % imagePath.split('.')[0])
            self.write('<img src="/images/%s" width="500"></a>\n' % imagePath)
        self.write('</body></html>\n')

class AdServer(BaseServer):

    def getRequestHandlers(self):
        imagesHandlerData = {'path': './images'}
        cssHandlerData = {'path': './css'}
        site = NanoSite()
        return [
           ('/css/(.*.css)', StaticFileHandler, cssHandlerData),
           ('/(.*.ico)', StaticFileHandler, imagesHandlerData),
           ('/images/(.*)', StaticFileHandler, imagesHandlerData),
           ('/(.*)', RequestHandler, dict(path='./', publication=site)),
        ] # http://localhost:8889/<args>


server = AdServer(port=8996)
server.run()
