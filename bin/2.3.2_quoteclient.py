import twisted
from twisted.internet import reactor, protocol
from twisted.internet.protocol import Protocol

class QuoteProtocol(protocol.Protocol):
  def __init__(self, factory):
    self.factory = factory

  def connectionMade(self):
    self.sendQuote()

  def sendQuote(self):
    self.transport.write(self.factory.quote)

  def dataReceived(self, data):
    print("Received quote:", data)
    self.transport.loseConnection()

#class QuoteClientFactory(twisted.internet.protocol.ClientFactory):
class QuoteClientFactory(protocol.ClientFactory):
  def __init__(self, quote):
    self.quote = quote

  def buildProtocol(self, addr):
    return QuoteProtocol(self)

  def clientConnectionFailed(self, connector, reason):
    print('connection failed:', reason.getErrorMessage())
    maybeStopReactor()

  def clientConnectionLost(self, connector, reason):
    print('connection lost:', reason.getErrorMessage())
    maybeStopReactor()
<<<<<<< HEAD

def maybeStopReactor():
  print("TryingToStopReactor")
=======
def maybeStopReactor():
>>>>>>> 34143f723acea18ffe80027bf7bffb4686549223
  global quote_counter
  quote_counter -= 1
  if not quote_counter:
    reactor.stop()
<<<<<<< HEAD

=======
>>>>>>> 34143f723acea18ffe80027bf7bffb4686549223
quotes = [
  "You snooze you lose",
  "The early bird gets the worm",
  "Carpe diem"
#  "Mahna mahna",
#  "Doot doo d'doo doo",
#  "Mahna mahna",
#  "Doot doo d'doo",
#  "Mahna mahna",
#  "Doot doo d'doo d'doo d'doo doo doo"
]
quote_counter = len(quotes)

for quote in quotes:
  reactor.connectTCP('localhost', 8000, QuoteClientFactory(quote))
reactor.run()
