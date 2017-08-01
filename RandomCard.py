import random
import webapp2


class Card(object):
	deck = []
	Face = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK" ,"QUEEN" ,"KING", "ACE "]
	Suit = ["HEART", "DIAMOND", "CLUB", "SPADE"]

	def __init__(self,suit,face):
		self.suit = suit
		self.face = face

	def getSuit(self):
		return self.suit

	def getFace(self):
		return self.face

	# Create static method to generate card objects
	@staticmethod
	def getDeck():
		for i in (Card.Suit):
			for j in (Card.Face):
				Card.deck.append(Card(i,j))
		return Card.deck

	def getString(self):
		return "SUIT:" + self.suit + " " +"FACE:"+ self.face

class Deck(webapp2.RequestHandler):
	def __init__(self, mylist):
		self.cardList = mylist
		# intializing the super constructor
		
		super(Deck, self).__init__()

	def shuffleCard(self):
		number = random.randint(0,51)
		return self.cardList[number]
		
	
class TestClass(webapp2.RequestHandler):

	def get(self):
		Card.deck = Card.getDeck()
		mydeck = Deck(Card.deck)
		self.response.write(mydeck.shuffleCard().getString())


app = webapp2.WSGIApplication([(r'/',TestClass)])

def main():
	from paste import httpserver
	httpserver.serve(app,host='127.0.0.1',port='8080')

if __name__ == "__main__":
	main()
			