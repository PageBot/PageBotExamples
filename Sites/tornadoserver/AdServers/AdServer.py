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
#     http://localhost:8889
#     http://localhost:8889/blog
#     http://localhost:8889/query?n=100
#     http://localhost:8889/query/aaa?n=100
#     http://localhost:8889/resource/1234
#     http://localhost:8889/resource/abcd-200/xyz-100
#
from pagebot.server.baseserver import 