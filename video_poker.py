#video_poker.py
#Kyle Pietz

from random import shuffle
from collections import Counter

numberArray = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suitArray = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
handStrings = ['Royal Flush!', 'Straight Flush!', 'Four of a Kind!', 'Full House!', 'Flush!', \
                      'Straight!', 'Three of a Kind!', 'Two Pair!', 'Jacks or Better!']
multipliers = [250, 50, 25, 9, 6, 4, 3, 2, 1]
displayWelcome = True
total = 100

class Deck:
    
    def __init__(self):
        cards = []
        for number in numberArray:
            for suit in suitArray:
                C = Card(number, suit)
                cards += [C]
        shuffle(cards)
        self.cards = cards
        
    def to_string(self):
        for Card in self.cards:
            print(str(Card.number) + " of " + str(Card.suit))
    
    def draw(self):
        self.cards = self.cards[1:]
        return self.cards[0]
    
class Card:
    
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        
    def to_string(self):
        print(str(card.number) + " of " + str(card.suit))
        
class Hand:
    
    def __init__(self, cards):
        self.cards = cards
        
    def to_string(self):
        i = 1
        for Card in self.cards:
            print(str(i) + ') ' + str(Card.number) + " of " + str(Card.suit))
            i += 1
            
    def checkHand(self):
        handSuits = []
        handNumbers = []
        modifiedNumberArray = ['Ace'] + numberArray
        royalFlush, straightFlush, fourOfAKind, fullHouse, flush, straight, \
                    threeOfAKind, twoPair, jacksOrBetter = False, False, False, False, \
                    False, False, False, False, False

        #Making hand easier to check
        for Card in self.cards:
            handNumbers += [Card.number]
            handSuits += [Card.suit]

        handSuitsSet = set(handSuits)
        distinctSuits = list(handSuitsSet)
        if len(handSuitsSet) == 1:
            flush = True
                
        handNumbersSet = set(handNumbers)
        for i in range(10):
            if set(modifiedNumberArray[i:i+5]) == handNumbersSet:
                stright = True
        
        if flush == True and straight == True:
            straightFlush = True
        
        if flush == True and straight == True and handNumbers == numberArray[-5:]:
            royalFlush = True
        
        c = Counter(handNumbers)
        tuples = c.items()
        
        twoCount = 0
        threeCount = 0
        for i in tuples:
            if i[1] == 2:
                twoCount += 1
                if i[0] in numberArray[-4:]:
                    jacksOrBetter = True
            if i[1] == 3:
                threeCount += 1
                threeOfAKind = True
            if i[1] == 4:
                fourOfAKind = True
        
        if twoCount == 2:
            twoPair = True
        if twoCount == 1 and threeCount == 1:
            fullHouse = True
            
        handBools = [royalFlush, straightFlush, fourOfAKind, fullHouse, flush, straight, \
                    threeOfAKind, twoPair, jacksOrBetter]
        
        outcome = ('Better luck next time...', 0)
        for i in range(len(handBools)):
            if handBools[i] == True:
                outcome = (handStrings[i], multipliers[i])
                break
                
        return outcome
                
def swap(Deck, Hand, heldCards):
    #heldCards will be an array of ints 1-5 from anywhere of len 0 to 5
    throwaways = [n for n in range(1,6) if n not in heldCards]
    for n in throwaways:
        Hand.cards[n-1] = Deck.draw()
           
def main():
    global total, numberArray, suitArray, handStrings, multipliers, displayWelcome
    if displayWelcome == True:
        bet = 0
        while int(bet) > total or int(bet) < 1:
            bet = input("Welcome to Video Poker! You start out with " + str(total) +\
                        " credits. How much do you want to bet?\n")
    
    elif displayWelcome == False:
        bet = 0
        while int(bet) > total or int(bet) < 1:
            bet = input("You currently have " + str(total) +\
                        " credits. How much do you want to bet?\n")
    bet = int(bet)
    total -= bet
    
    ans = input("Type and enter 'draw' to draw 5 cards.\n")
    
    if ans == 'draw':
        D = Deck()
        newHand = []
        for i in range(5):
            newHand += [D.draw()]
            
        H = Hand(newHand)
        H.to_string()
        heldCards = []
        
        print("\nHere are your cards. To hold a card, type its number and hit enter. " +\
                    "When you're ready, type and enter 'draw'.")
        ans = ' '
        while ans != 'draw' and ans in ['1','2','3','4','5',' ']:
            if ans != ' ':
                heldCards += [int(ans)]
            ans = input("")
        
        swap(D, H, heldCards)
        H.to_string()
        tup = H.checkHand()
        total += tup[1]*bet
        print('\n' + tup[0] + '\n')
        
        if total > 0:
            print("You now have " + str(total) + " credits.\n")
        elif total == 0:
            print("Looks like you're all out of money. Thanks for playing!")
            exit()
        
        ans = input("Would you like to play again? Type 'y' for yes or type 'n' for no.\n")
        
        if ans == 'y':
            displayWelcome = False
            main()
        elif ans == 'n':
            print("You've cashed out with " + str(total) + " chips.")
            exit()

main()
        
