from collections import Counter
from enum import Enum
from functools import cmp_to_key

class HAND(Enum):
    HIGH = 1
    PAIR = 2
    TWOPAIR = 3
    THREE = 4
    FULLHOUSE = 5
    FOUR = 6
    FIVE = 7
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value

def getHand(hand):
    counts = sorted(Counter(hand).values(),reverse=True)

    # Defaults
    if len(counts) == 0:
        counts = [0,0]
    elif len(counts) == 1:
        counts += [0]

    if   counts[0] == 5:
        return HAND.FIVE
    elif counts[0] == 4:
        return HAND.FOUR
    elif counts[0] == 3 and counts[1] == 2:
        return HAND.FULLHOUSE
    elif counts[0] == 3 and counts[1] != 2:
        return HAND.THREE
    elif counts[0] == 2 and counts[1] == 2:
        return HAND.TWOPAIR
    elif counts[0] == 2 and counts[1] != 2:
        return HAND.PAIR
    else:
        return HAND.HIGH
    
def getHandJoker(hand):
    jokers = hand.count('J')
    
    newHand = hand.replace('J','')
    handValue = getHand(newHand)

    if   jokers == 0: # Regular Hand
        return handValue
    elif jokers == 1: # Upgrading a 4-card hand
        if handValue == HAND.HIGH:    return HAND.PAIR
        if handValue == HAND.PAIR:    return HAND.THREE
        if handValue == HAND.TWOPAIR: return HAND.FULLHOUSE
        if handValue == HAND.THREE:   return HAND.FOUR
        if handValue == HAND.FOUR:    return HAND.FIVE
        return handValue
    elif jokers == 2: # Upgrading a 3-card hand
        if handValue == HAND.HIGH:    return HAND.THREE
        if handValue == HAND.PAIR:    return HAND.FOUR
        if handValue == HAND.THREE:   return HAND.FIVE
        return handValue
    elif jokers == 3: # Upgrading a 2-card hand
        if handValue == HAND.HIGH:    return HAND.FOUR
        if handValue == HAND.PAIR:    return HAND.FIVE
        return handValue
    else:
        return HAND.FIVE

def compareHands(hand1,hand2,joker=False):
    getHandCompare = getHandJoker if joker else getHand
    if   getHandCompare(hand1) < getHandCompare(hand2):
        return -1
    elif getHandCompare(hand1) > getHandCompare(hand2):
        return 1
    # Same hands, compare cards
    else:
        cardOrder = "J23456789TQKA" if joker else "23456789TJQKA"
        for card1,card2 in zip(hand1,hand2):
            if   cardOrder.index(card1) < cardOrder.index(card2):
                return -1
            elif cardOrder.index(card1) > cardOrder.index(card2):
                return 1
        return 0


def Part1(data):
    cardBids = [d.split() for d in data]
    # Add empty bid to shift ranks to start at 1
    sortedCards = [['23456','0']] + sorted(cardBids,key=cmp_to_key(lambda c1,c2: compareHands(c1[0],c2[0],False)))
    return sum( [i*int(bid[1]) for i,bid in enumerate(sortedCards)] )
     
def Part2(data):
    cardBids = [d.split() for d in data]
    # Add empty bid to shift ranks to start at 1
    sortedCards = [['23456','0']] + sorted(cardBids,key=cmp_to_key(lambda c1,c2: compareHands(c1[0],c2[0],True)))
    return sum( [i*int(bid[1]) for i,bid in enumerate(sortedCards)] )