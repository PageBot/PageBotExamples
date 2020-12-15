#!/usr/bin/env python3
# Moving experimental context feature here.

def newText(textStyles, newLine=False):
    """Answers a BabelString as a combination of all text and styles in
    textStyles, which is should have format:

    [(baseString, style), (baseString, style), ...]

    Add return \n to the string is the newLine attribute is True or if a
    style has

    style.get('display') == DISPLAY_BLOCK

    """
    assert isinstance(textStyles, (tuple, list))
    s = None

    for t, style in textStyles:
        if newLine or (style and style.get('display') == DISPLAY_BLOCK):
            t += '\n'

        bs = self.newString(t, style=style)
        if s is None:
            s = bs
        else:
            s += bs
    return s


