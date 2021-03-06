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
#    E01_Dependencies.py
#

import sys, os

print('System: %s, %s' % (os.name, sys.platform))
print('Python version is:')
print(sys.version)
print('Python executable: %s' % sys.executable)

CLEAN = True

print('\nChecking installation paths... \n')

try:
    # Note: inside DrawBot site.pyc needs to be removed from root level.
    import site
    print('Found site at %s' % site.__file__)
    packages = site.getsitepackages()
    for p in packages:
        print(' - %s' % p)
except:
    print('x Could not read site packages :S')

# TODO: add svgwrite, flat, markdown etc?
# TODO automate, eval()?

required = ['flat', 'pagebot', 'booleanOperations', 'fontTools', 'markdown', 'sass', 'svgwrite', 'tornado']


if sys.platform == 'darwin':
    optional = ['pagebotosx', 'drawBot', 'objc']
else:
    optional = ['']

missing = []

for l in required:
    try:
        __import__(l)
        print('Required dependency %s installed at %s' % (l, __import__(l).__file__))
    except:
        print('Required dependency x %s not installed' % l)
        missing.append(l)
        CLEAN = False

for l in optional:
    try:
        __import__(l)
        print('Optional dependency %s installed at %s' % (l, __import__(l).__file__))
    except:
        print('Optional dependency x %s not installed' % l)
        missing.append(l)

if not CLEAN:
    print('Not all dependencies are installed, please install missing ones:')
    print(', '.join(missing))
else:
    print('Found all dependencies, running some test...')

    # Testing PageBot context.
    from pagebot import getContext
    context = getContext()
    print('The default PageBot context is %s' % context)
    print('The default builder module is %s' % context.b)
