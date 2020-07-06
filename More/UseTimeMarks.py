#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2017 Thom Janssen <https://github.com/thomgb>
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     UseTimeMarks.py
#
from pagebot.toolbox.timemark import TimeMark

def run():
        """TimeMarks are use to control the change of element values over time.
        This way movement can be defined in time based documents, such as
        animations, but also support for the generation of specific document
        content and appearance, based on a time or date, can be defined."""

	tms = [TimeMark(0, 'aaaa'), TimeMark(10000, 'vvv')]

	tms.append(TimeMark(4, 'TimeMark@4'))
	tms.append(TimeMark(100, 'TimeMark@100'))
	print('Unsorted after append', tms)
	tms.sort()
	print('Sorted TimeMark list', tms)
	print()

	def findTimeMarks(t, tms):
	    for index, tm in enumerate(tms):
	        if tm.t > t:
	            return tms[index-1], tm
	    return None

	# Search what is valid in t=5
	t = 5
	print(findTimeMarks(t, tms))


if __name__ == '__main__':
    run()
