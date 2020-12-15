#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     www.pagebot.io
#     Licensed under MIT conditions
#
# -----------------------------------------------------------------------------
#
#    E02_Sass.py
#
#    Test working on exteral scss/sass application to compile into css.
#
import shutil
from pagebot.filepaths import getResourcesPath

def testSass():
    import sass

    # Testing Sass.
    css = sass.compile(string='a { b { color: blue; } }')
    print(css)
    path = getResourcesPath() + '/templates/test.scss'
    import os.path
    print('Path %s exists:' % path, os.path.exists(path))
    css = sass.compile(filename=path)
    print(css)

    #test_scss = open('test.scss', 'w')
    import os, os.path

    for f in ('_export/css', '_export/sass'):
        if not os.path.exists(f):
            os.makedirs(f)
    shutil.copy(path, '_export/sass')
    sass.compile(dirname=('_export/sass', '_export/css'), output_style='compressed')
    with open('_export/css/test.css') as example_css:
        print(example_css)

    # Export with HtmlBuilder.
    from pagebot.contexts.markup.htmlbuilder import HtmlBuilder
    hb = HtmlBuilder()
    print(hb)
    hb.compileScss(path, cssPath = '_export/css/testHtmlBuilder.css')

testSass()
