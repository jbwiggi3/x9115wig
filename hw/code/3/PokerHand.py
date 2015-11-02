"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *


class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

        
    def has_pair(self):
    	card_dict = dict()
    	for i in range(1,14):
    		card_dict[str(i)] = 0;
    	
    	for i in range(len(self.cards)):
    		card_dict[str(self.cards[i].rank)] += 1
    		
    	for i in range(1,14):
    		if card_dict[str(i)] == 2:
    			return True
    		
    	return False
    	
    def has_twopair(self):
    	card_dict = dict()
    	for i in range(1,14):
    		card_dict[str(i)] = 0;
    	
    	for i in range(len(self.cards)):
    		card_dict[str(self.cards[i].rank)] += 1
    	
    	flag = False
    	for i in range(1,14):
    		if card_dict[str(i)] == 2:
    			if flag:
    				return True
    			else:
    				flag = True
    		
    	return False
    	
    def has_threeofakind(self):
    	card_dict = dict()
    	for i in range(1,14):
    		card_dict[str(i)] = 0;
    	
    	for i in range(len(self.cards)):
    		card_dict[str(self.cards[i].rank)] += 1
    		
    	for i in range(1,14):
    		if card_dict[str(i)] == 3:
    			return True
    		
    	return False
    	
    def has_straight(self):
    	card_dict = dict()
    	for i in range(1,14):
    		card_dict[str(i)] = 0;
    	
    	for i in range(len(self.cards)):
    		card_dict[str(self.cards[i].rank)] += 1
    		
    	for i in range(9):
    		had_straight = True
    		for j in range(1,6):
    			if card_dict[str(i+j)] == 0:
    				had_straight = False
    		if had_straight:
    			return True
    		
    	return False
    	
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    	
    def has_fullhouse(self):
    	card_dict = dict()
    	for i in range(1,14):
    		card_dict[str(i)] = 0;
    	
    	for i in range(len(self.cards)):
    		card_dict[str(self.cards[i].rank)] += 1
    	
    	flag = False
    	rankWithThree = -1
    	for i in range(1,14):
    		if card_dict[str(i)] == 3:
    			flag = True
    			rankWithThree = i
    	if not flag:
    		return False
    	
    	for i in range(1,14):
    		if i != rankWithThree:
    			if card_dict[str(i)] == 2:
    				return True
    		
    	return False
    
    def has_fourofakind(self):
    	card_dict = dict()
    	for i in range(1,14):
    		card_dict[str(i)] = 0;
    	
    	for i in range(len(self.cards)):
    		card_dict[str(self.cards[i].rank)] += 1
    		
    	for i in range(1,14):
    		if card_dict[str(i)] == 4:
    			return True
    		
    	return False
    	
    def has_straightflush(self):
    	
    	return self.has_straight() and self.has_flush()
    
    def classify(self):
    	if self.has_straightflush():
    		return "straight flush"
    	elif self.has_fourofakind():
    		return "four of a kind"
    	elif self.has_fullhouse():
    		return "full house"
    	elif self.has_flush():
    		return "flush"
    	elif self.has_straight():
    		return "straight"
    	elif self.has_threeofakind():
    		return "three of a kind"
    	elif self.has_twopair():
    		return "two pair"
    	elif self.has_pair():
    		return "pair"
    	else:
    		return "nothing"

"""if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        print hand.has_flush()
        print ''"""

numberofhands = 100000
amounts = [0,0,0,0,0,0,0,0]
for i in range(numberofhands):
	deck = Deck()
	deck.shuffle()
	hand = PokerHand()
	deck.move_cards(hand, 5)
	result = hand.classify()
	if result == "straight flush":
		amounts[7] += 1 
	elif result == "four of a kind":
		amounts[6] += 1 
	elif result == "full house":
		amounts[5] += 1 
	elif result == "flush":
		amounts[4] += 1 
	elif result == "straight":
		amounts[3] += 1 
	elif result == "three of a kind":
		amounts[2] += 1 
	elif result == "two pair":
		amounts[1] += 1 
	elif result == "pair":
		amounts[0] += 1 

#print out the table
print "Pair:            " + str(amounts[0]/(numberofhands/1.0))
print "Two Pair:        " + str(amounts[1]/(numberofhands/1.0))
print "Three of a Kind: " + str(amounts[2]/(numberofhands/1.0))
print "Straight:        " + str(amounts[3]/(numberofhands/1.0))
print "Flush:           " + str(amounts[4]/(numberofhands/1.0))
print "Full House:      " + str(amounts[5]/(numberofhands/1.0))
print "Four of a Kind:  " + str(amounts[6]/(numberofhands/1.0))
print "Straight Flush:  " + str(amounts[7]/(numberofhands/1.0))