# PageBot Examples

The examples in this folder are very basic, explaining the usage principles of PageBot, ordered by increasing complexity.

There are roughly 3 levels of DrawBot/PageBot scripts. 

* Plain DrawBot
* PageBot Contexts
* PageBot Document, View and Element

## Plain DrawBot

Since initially PageBot was built on top of [DrawBot](http://drawbot.com), all examples are supported when running in the DrawBotApp. 

## Context 

To make the relation between PageBot and DrawBot more abstract, a “Context” layer was added. 
Context connect the abstract Document/Element with a specific output format.
Normally contexts are invisible, used by PageBot Document and Element instances, but for testing and demo, they can be addressed separately, in the same way as drawing in DrawBot happens.

# PageBot Document, View and Element

This is the main level of PageBot publications. Theoretically a document is unaware of which output format it is rendering.

# Running PageBot on Google Cloud, start here:

https://developers.google.com/sheets/api/quickstart/python