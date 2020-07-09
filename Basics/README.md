# PageBot Examples

The examples in this folder are very basic, explaining the usage principles of PageBot, ordered by increasing complexity.

There are roughly 3 levels of DrawBot / PageBot scripts. 

* Plain DrawBot
* PageBot Contexts
* PageBot Document, View and Element


## Contexts
 
Contexts connect our Document / Element structure with a specific output format. Because PageBot was initially built upon [DrawBot](http://drawbot.com), all examples should run in the DrawBotApp. 

Normally contexts are invisible, used by PageBot Document and Element instances, but for testing and demo, they can be addressed separately, in the same way as drawing in DrawBot happens.

# PageBot Document, View and Element

This is the main level of PageBot publications. Theoretically a document is unaware of which output 
format it is rendering.

## Update: Reconstruction of BabelString

Most the examples have currently being adapted to support the new BabelString. 

All strings inside the PageBot handling of text are BabelString instances. They will handle text manipulation themselves, except for methods that need the size of text. In that case context specific functions are called.

All examples in this directory are being revived and tested.

A BabelString “context flavor” is defined as follows:

~~~
bs = context.newString(txt, style)
~~~
creates a BabelString that has
~~~
bs.context 
~~~
defined as internal weakref property.

~~~
e = newText(txt, style, parent=page)
~~~
creates a txt element, where the context is derived from either

~~~
e.context
e.page.context
e.doc.context
~~~