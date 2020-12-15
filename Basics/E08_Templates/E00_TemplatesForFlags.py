# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#

#     www.pagebot.io
#     Licensed under MIT conditions
#


# -----------------------------------------------------------------------------
#
#     E00_TemplatesForFlags.py
#
#     Shows the usage of templates, both as default in the document as well
#     as applying on an existing page.
#     The elements are copied from the template page, so not reference to the
#     original elenents remains in the page after thhe apply.
#     Note that also the apply will remove all previous element from the page,
#     so the order is important: first apply a new template, then add elements
#     to a specific page.
#

from pagebot import getContext
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.document import Document
from pagebot.toolbox.color import color, whiteColor

# Document is the main instance holding all information about the document togethers (pages, styles, etc.)

context = getContext('DrawBot')

PageSize = 500, 400

# Export in _export folder that does not commit in Git. Force to export PDF.
EXPORT_PATH = '_export/E00_CodedTemplates.pdf'

def makeTemplate(w, h, doFrench):
    """Make template for the main page (flag), for the given (w, h) size.
    The optional **french** flag creates a French flag, otherwise Italian."""

    # Creat enew Template instance for the given size.
    template = Template(w=w, h=h) # Create template.
    # Add named text box to template for main specimen text.
    if doFrench:
        rightColor = 0, 0, 0.5 # r, g, b Make French flag
    else:
        rightColor = 0, 0.5, 0 # r, g, b Make Italian flag.
    # Make 2 formatted strings with white text,
    fsLeft = context.newString('Template box left', style=dict(textFill=whiteColor))
    fsRight = context.newString('Template box right', style=dict(textFill=whiteColor))

    # Two columns on 1/3 of document width, fitting on padding height by layout conditions.
    newText(fsLeft, w=w/3, fill=color(1, 0, 0), padding=10,
        parent=template, conditions=[Left2Left(), Top2Top(), Fit2Height()])

    newText(fsRight, w=w/3, fill=rightColor, padding=10,
        parent=template, conditions=[Right2Right(), Top2Top(), Fit2Height()])
    
    # Answer the generated template page.
    return template

def makeDocument():
    """Make a new document, using the rs as root style."""

    #W = H = 120 # Get the standard a4 width and height in points.
    W, H = PageSize

    # Create a document, as a start with just a single page as default.
    doc = Document(title='Color Squares', w=W, h=H, context=context)

    view = doc.getView()
    view.padding = 0 # Don't show cropmarks in this example.

    return doc

def processPages(doc):
    # Make templates
    frenchTemplate = makeTemplate(doc.w, doc.h, doFrench=True)
    italianTemplate = makeTemplate(doc.w, doc.h, doFrench=False)

    # Get page by pageNumber, first in row (there is only one now in this row).
    page = doc[1] # Get the single page from the document with default template.

    # Do things with the first page.
    page.applyTemplate(frenchTemplate)

    # Get the next page. Create one if it does not exist, with the default
    # template in the document.
    page = page.next

    # Overwrite the default template by another template (in this case with different color).
    # Note that this way it is possible to mix different page sizes in one document.
    # The elements are copied from the template page, so no reference to the
    # original elements remains in the page after the apply.
    # Note that also the apply will remove all previous element from the page,
    # so the order is important: first apply a new template, then add elements
    # to a specific page.
    page.applyTemplate(italianTemplate)

    # Recursively solve the conditions in all pages.
    # If there are failing conditions, then the status is returned in the Score instance.
    score = doc.solve()
    if score.fails: # If some conditions where impossible, that answer the result.
        print(score.fails)

    return doc # Answer the doc for further doing.

d = makeDocument()
processPages(d)
d.export(EXPORT_PATH)

