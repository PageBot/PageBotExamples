# Reconstruction of BabelString

The examples are currently reconstructed, to support the new BabelString. 

All strings inside the PageBot handling of text are BabelString instances. As much as possible they can handle text manipulation themselves, except for methods that need the actual size of text.
In that case the context is called.

All examples in this directory are being revied and tested, unless they start with an ordering number. Those are supposed to work. 

A BabelString “contextx flavor” is defined as follows:

~~~
bs = context.newString(txt, style)
~~~
creates a BabelString that has
~~~
bs.context 
~~~
defined as internal weakref property to the context.

~~~
e = newText(txt, style, parent=page)
~~~
creates a txt element, where the context is derived from either

~~~
e.context
e.page.context
e.doc.context
~~~
