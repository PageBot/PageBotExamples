# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Free to use. Licensed under MIT conditions
#     Made for usage in DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     SLides.py
#
# 
import os

from pagebot.contexts import getContext
context = getContext()

from pagebot.fonttoolbox.objects.font import findFont
from pagebot.style import RIGHT
from pagebot.document import Document
from pagebot.typesetter import Typesetter
from pagebot.composer import Composer
from pagebot.elements import *
from pagebot.conditions import *

W, H = 1920, 1080

MD_PATH = u"WhatIsPageBot.md"
PADDING = 50
M = 310
T = 64
G = P = 24
FONT_NAME = 'MomentumSans-VF'
font = findFont(FONT_NAME)
fontPath = 'MomentumSans-TextMedium'

LOGO = 'TYPE NETWORK'
TITLE = 'What is PageBot? | April 2nd, 2018'

BG1 = 0.1
BG2 = BG3 = (1,1,1,0.15)

CONTENT = [
    dict(head="""What is PageBot?""", image=((W-M, None) ,'images/PageBotPage.png')),
    dict(head="""What is PageBot?""", content="PageBot is a Python libary to script the creation of any type of publication in any design from any type of source, and save it to any format.\n\nMIT Open Source since July 2017."),
    dict(head="""PageBot solves:""", content=u"""• Integration between style guide and design\n• Merge of design and production phases\n• Disconnect context from implementation\n• Rule based design\n• Scriptable templates\n• Single source publishing\n• Full control of (variable) font parameters."""),
    dict(head=u"""PageBot creates:""",
        content=u"""• Websites\n• Banners\n• Ads\n• Specimens\n• Newspapers\n• Brochures\n• Magazines\n• Books\n• Cards\n• Posters""",
        content2=u"""• Primitive element classes\n• Textbox\n• Filtered images\n• Path & polygons\n• Variable Font axis space\n• Tables\n• Various types of graphs\n• Animated infographics"""),
    dict(head="""Schema""",
        image=((W-M-4*P, None), 'images/PageBotSchema.pdf')),
    dict(head=u"""PageBot features:""", content=u"""• Programmatic design\n• Intelligent typography\n• Access to Variable Fonts\n• Conditional page-layout\n• MarkDown input\n• 3D data model\n• Context based export to platforms and formats"""),
    dict(head="""Prototype to publish""", content="Default build-in knowledge for rapid prototyping.\n\nShort design cycle includes full production sequence.\n\nTesting design model and parameters in early stages of the design."),
    dict(head="""Prototype to publish""", 
        image=((W-M-4*P, None), 'images/PageBotMagazineClassCode.png')),
    dict(head2="""Typographic rules""",
        image=((W-M-4*P, None), 'images/TypographicParameters.png')),
    dict(head="""Design target: Ads""",
        image=((W-M-P, None), 'images/Bier.png')),
    dict(head="""Design target: Ads""",
        image=((None, H-T-200), 'images/Travel.png')),
    dict(head="""Design target: Covers""",
        image=((None, H-T-200), 'images/BookCovers.png')),
    dict(head="""Design target: Specimens""",
        image=((None, H-T-200), 'images/Specimens.png')),
    dict(head="""Design target: Testing""",
        image=((None, H-T-200), 'images/Masters.png')),
    dict(head="""Design target: Visualizing""",
        background=((0.9,0.9,0.9), M, 0, W-M, H-T-200, ),
        image=((None, H-T), 'images/findVariableFontDeltas.pdf'),
        image2=((None, H-T-200), 'images/SkiaQ.png')),
    dict(head="""Design target: Infographics""",
        image=((None, H-T-200), 'images/fitVariableHeadline.gif')),
    dict(head="""Design target: Websites""",
        image=((W-M, None), 'images/DDSWebsite.png')),
    dict(head="""Implement style guide\nSketch, run, review\nAdjust rules, run, review\n..."""),
    dict(head="""Sketch, run, review, ...""",
        image=((None, H-240), 'images/SketchDesignSpace.png')),
    dict(head="""Sketch, run, review, ...""",
        image=((None, H-240), 'images/DecovarSpecimen.png')),
    dict(head="""Coding of typographic rules""", content=u"""• Float2Top( )\n• Left2Left( )\n• Fit2Right( )\n• FitHead2Width( )\n• page.solve( )"""),
    dict(head="""Implementing all material.io rules""", content=u"""• Sketching\n• Generating\n• Testing\n• Rule based templates\n• Export various formats""",
        image2=((None, H-T-200), 'images/Material.png')),
    dict(head2="""Unique variable solution to typographic issues""",
        background=((0.9,0.9,0.9), M, 0, W-M, H-T-320, ),
        image=((W-M+2*P, None), "images/Bitcount_a_specimen.pdf")),
    dict(head2="""Unique variable solution to typographic issues""",
        image=((None, H-T-270), "images/RobotoDelta-wght-wdth.pdf"),
        image2=((None, H-T-270), "images/Rubik.png")),
    dict(head="""Prototyping to product in one framework""",
        image=((None, H-T-200), 'images/PageBotSchema.pdf')),
]
headStyle = dict(textFill=1, font=fontPath, fontSize=90, rLeading=1.2)
contentStyle = dict(textFill=1, font=fontPath, fontSize=60, rLeading=1.5)
logoStyle = dict(textFill=1, font=fontPath, fontSize=32, rTracking=0.11)
titleStyle = dict(textFill=1, font=fontPath, fontSize=32, rTracking=0.04)
slideNumberStyle = dict(textFill=1, font=fontPath, fontSize=32, rTracking=0.04, xTextAlign=RIGHT)

doc = Document(w=W, h=H, autoPages=len(CONTENT), originTop=False, context=context)
for pn, slide in enumerate(CONTENT):
    doc.frameDuration = 2
    page = doc[pn+1]
    page.padding = PADDING
    newRect(fill=BG1, w=W, h=H, parent=page)
    newRect(fill=BG2, w=M, h=H, parent=page)
    newRect(fill=BG3, y=H-T, w=W, h=T, parent=page)
    
    background = slide.get('background')
    if background is not None:
        color, bx, by, bw, bh = background
        newRect(fill=color, x=bx, y=by, w=bw, h=bh, parent=page)
 
    head = slide.get('head')
    if head is not None:
        bs = context.newString(head,style=headStyle)
        content = slide.get('content')
        if content is not None:
            bs += context.newString('\n\n'+content, style=contentStyle)
        newTextBox(bs, name='content', x=M+1.5*P, y=P, w=W-M-4*P, h=H-2*P-T, parent=page)
       
    content2 = slide.get('content2')
    if content2 is not None:
        bs = context.newString(content2, style=contentStyle)
        newTextBox(bs, name='content2', x=3*M, y=-7.3*P, w=W-M-4*P, h=H-2*P-T, parent=page)
        
    imageInfo = slide.get('image')
    if imageInfo is not None:
        (w, h), imagePath = imageInfo
        newImage(imagePath, x=M, y=0, w=w, h=h, parent=page)

    imageInfo = slide.get('image2')
    if imageInfo is not None:
        (w, h), imagePath = imageInfo
        newImage(imagePath, x=M+(W-M)/2, y=0, w=w, h=h, parent=page)

    head2 = slide.get('head2')
    if head2 is not None:
        bs = context.newString(head2,style=headStyle)
        newTextBox(bs, name='content', x=M+1.5*P, y=P, w=W-M-4*P, h=H-2*P-T, parent=page)

    logo = context.newString(LOGO, style=logoStyle)
    newTextBox(logo, y=H-T, w=M+P, h=T, pt=12, pl=P/2, parent=page)
    
    title = context.newString(TITLE, style=titleStyle)
    newTextBox(title, y=H-T, w=W-M-2*P, x=M+P, h=T, pt=12, pl=P/2, parent=page)
    
    slideNumber = context.newString('%d/%d' % (pn+1, len(CONTENT)), style=slideNumberStyle)
    newTextBox(slideNumber, y=H-T, w=150, x=W-P-150, h=T, pt=12, parent=page)
    

"""
t = Typesetter(doc, tryExcept=False, verbose=False, writeTags=False)
t.typesetFile(MD_PATH)
"""
#doc.export('_export/WhatIsPageBot.gif')
#doc.export('_export/WhatIsPageBot.svg')
doc.export('_export/WhatIsPageBot.pdf')

print 'Done' 

