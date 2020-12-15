#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#


# -----------------------------------------------------------------------------
#
#     E20_TraceImageInDrawBot.py
#
#     Trace a halftone image to vectors.
#     This only works in DrawBotContext, because of the required filters.
#
from pagebot.contexts.basecontext.bezierpath import BezierPath
from pagebot.filepaths import getResourcesPath
from pagebot.toolbox.units import p
from pagebot.toolbox.color import color
from pagebot import getContext

# Get the context (e.g. DrawBot) to call for conversion method
# Currently only the DrawBotContext has the required filters.
for contextName in ['DrawBot', 'Flat']:
	context = getContext(contextName)

	# Get the path of the image from PageBot resources
	imagePath = getResourcesPath() + '/images/cookbot10.jpg'

	# Create a PageBotPath wrapper instance, that include a Context.BezierPath
	path = BezierPath(context=context)

	# Trace the image.
	# traceImage(path, threshold=0.2, blur=None, invert=False, turd=2, tolerance=0.2, offset=None)
	# Convert a given image to a vector outline.
	# Optionally some tracing options can be provide:
	#
	#   threshold (0.2): the threshold used to bitmap an image
	#   blur (None): the image can be blurred
	#   invert (False): invert to the image
	#   turd (2): the size of small turd that can be ignored
	#   tolerance (0.2): the precision tolerance of the vector outline
	#   offset (None): add the traced vector outline with an offset to the BezierPath

	path.traceImage(imagePath)

	# Create a new page
	context.newPage(1000, 1000)
	context.image(imagePath)
	# Set fill to red
	context.fill((1, 0, 0))
	# Draw the converted outlines as red path
	context.drawPath(path)
	# Shift the path by some points
	path.moveBy((12, 6))
	# Change the color to blue and transparancy
	c = color(0, 0.5, 0.7, 0.7)
	context.fill(c)
	# Draw the path again in different color
	context.drawPath(path)
	# Move the path again and make a darker color
	path.moveBy((0, -14))
	context.fill(c.darker().darker())
	# Draw the path again on new position and darker color
	context.drawPath(path)
	# Save the page as PDF
	context.saveImage('_export/20_TraceImageBy%s.pdf' % contextName)

