from twisted.internet.defer import Deferred

def addBold(result):
  return "<b>%s</b>" % (result,)

def addItalic(result):
  return "<i>%s</i>" % (result,)

def printHTML(result):
  print result

d = Deferred()
d.addCallback(addBold)
d.addCallback(addItalic)
d.addCallback(printHTML)
d.callback("Hello world!")
e = Deferred()
e.addCallback(addBold).addCallback(addItalic).addCallback(printHTML)
e.callback("Goodbye world!")
