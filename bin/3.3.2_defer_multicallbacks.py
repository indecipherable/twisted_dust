from twisted.internet.defer import Deferred

def addBold(result):
  return "<b>%s</b>" % (result,)

def addItalic(result):
  return "<i>%s</i>" % (result,)

def printHTML(result):
  print result

def myCallback(result):
  print(result)

def myErrback(failure):
  print(failure)

d = Deferred()
e = Deferred()
e.addCallbacks(myCallback, myErrback)

d.addCallback(addBold)
d.addCallback(addItalic)
d.addCallback(printHTML)
#d.addErrback(addBold)
#d.addErrback(addItalic)
#d.addErrback(printHTML)

e.callback("Hello world!")
#e.errback(Exception("Goodbye world!"))
