# https://projecteuler.net/problem=54
# In the card game poker, a hand consists of five cards and are ranked, from 
# lowest to highest, in the following way:

    # High Card: Highest value card.
    # One Pair: Two cards of the same value.
    # Two Pairs: Two different pairs.
    # Three of a Kind: Three cards of the same value.
    # Straight: All cards are consecutive values.
    # Flush: All cards of the same suit.
    # Full House: Three of a kind and a pair.
    # Four of a Kind: Four cards of the same value.
    # Straight Flush: All cards are consecutive values of same suit.
    # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest 
# value wins; for example, a pair of eights beats a pair of fives (see example 1 
# below). But if two ranks tie, for example, both players have a pair of queens, 
# then highest cards in each hand are compared (see example 4 below); if the 
# highest cards tie then the next highest cards are compared, and so on.



# The file, poker.txt, contains one-thousand random hands dealt to two players. 
# Each line of the file contains ten cards (separated by a single space): the 
# first five are Player 1's cards and the last five are Player 2's cards. 
# You can assume that all hands are valid (no invalid characters or repeated cards), 
# each player's hand is in no specific order, and in each hand there is a clear winner.

# How many hands does Player 1 win?
from time import time

def countValue(hand, value):
    total = 0

    for card in hand:
        if cardValue(card) == value:
            total += 1

    return total



def onePair(hand):
    modifier = 15 * 1
    
    result = -1

    for card in hand:
        if countValue(hand, cardValue(card)) == 2:
            result = max(result, cardValue(card))

    if result == -1:
        return -1

    return modifier + result
    
    
def twoPair(hand):
    modifier = 15 * 2
    
    for i in range(4):
        for j in range(i+1, 5):
            v1 = cardValue(hand[i])
            v2 = cardValue(hand[j])

            if v1 == v2:
                for k in range(4):
                    for l in range(k+1, 5):
                        v3 = cardValue(hand[k])
                        v4 = cardValue(hand[l])

                        if v3 == v4 and v3 != v1:
                            return modifier + max(v1, v3)

    return -1



    
def threeOfAKind(hand):
    modifier = 15 * 3
    
    result = -1

    for card in hand:
        if countValue(hand, cardValue(card)) == 3:
            result = max(result, cardValue(card))

    if result == -1:
        return -1

    return modifier + result

    
def straight(hand):
    modifier = 15 * 4

    hand = sorted(hand, key=cardValue)

    for i in range(1, 5):
        if cardValue(hand[i]) != cardValue(hand[i-1]) + 1:
            return -1

    return modifier + cardValue(hand[4])
    
    
def flush(hand):
    modifier = 15 * 5

    hand = sorted(hand, key=cardValue)
    color = hand[0][1]

    for i in range(1, 5):
        if hand[i][1] != color:
            return -1

    return modifier + cardValue(hand[4])
    
    
def fullHouse(hand):
    modifier = 15 * (6-3)

    tak = threeOfAKind(hand)
    op = onePair(hand)
    if tak != -1 and op != -1 and (tak-15 * 3) != (op - 15 * 1):
        # print(tak)
        return modifier + tak

    return -1
    
    
def fourOfAKind(hand):
    modifier = 15 * 7

    result = -1

    for card in hand:
        if countValue(hand, cardValue(card)) == 4:
            result = max(result, cardValue(card))

    if result == -1:
        return -1

    return modifier + result
    
    
def straightFlush(hand):
    modifier = 15*(8 - 4)

    s = straight(hand)
    f = flush(hand)
    if s != -1 and f != -1:
        return modifier + s

    return -1
    
    
def royalFlush(hand):
    # modifier = 15 * 9

    sf = straightFlush(hand)
    if sf == 134:
        return sf + 15

    return -1
    
    
def separateHands(line):
    line = line.split(' ')
    
    return [line[:5], line[5:]]

def highestCard(hand, i):
    hand = sorted(hand, key=cardValue, reverse=True)

    return hand[i]
    
    
def winner(turn):
    tests = [onePair, twoPair, threeOfAKind, straight, flush, fullHouse]
    tests += [fourOfAKind, straightFlush, royalFlush]
    
    score0 = 0
    score1 = 0

    for test in tests:
        score0 = max(score0, test(turn[0]))
        score1 = max(score1, test(turn[1]))

    # print(score0, score1)
    if score0 < score1:
        return 1
    elif score0 > score1:
        return 0

    for i in range(5):
        score0 = cardValue(highestCard(turn[0], i))
        score1 = cardValue(highestCard(turn[1], i))
        # print(score0, score1)

        if score0 < score1:
            return 1
        elif score0 > score1:
            return 0

    # .............
    return -1

    

def cardValue(card):
    return {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}[card[0]]
    
# ******************************************************************************
def tests():
    # 15
    print("One Pair")
    print("20 = %d" % onePair(['5H', '5C', '6S', '7S', 'KD']))
    print("25 = %d" % onePair(['TC', '3S', '8S', '8D', 'TD'])) # ~
    print("-1 = %d" % onePair(['2C', '3S', '5S', '8D', 'TD']))
    print("-1 = %d" % onePair(['2D', '9C', 'AS', 'AH', 'AC']))

    # 30
    print("Two pair")
    print("33 = %d" % twoPair(['2C', '3S', '3S', '2D', 'TD']))
    print("-1 = %d" % twoPair(['2C', '3S', '8S', '2D', 'TD']))

    # 45
    print("Three of a kind")
    print("53 = %d" % threeOfAKind(['2C', '3S', '8S', '8D', '8D']))
    print("-1 = %d" % threeOfAKind(['2C', '3S', '2S', '8D', '8D']))

    # 60
    print("Straight")
    print("66 = %d" % straight(['2C', '3S', '4S', '5D', '6D']))
    print("66 = %d" % straight(['6C', '2S', '4S', '5D', '3D']))
    print("-1 = %d" % straight(['2C', '3S', '4S', '5D', '8D']))

    # 75
    print("Flush")
    print("81 = %d" % flush(['2C', '3C', '4C', '5C', '6C']))
    print("89 = %d" % flush(['AC', '3C', '4C', '5C', '2C']))
    print("-1 = %d" % flush(['2C', '3S', '4S', '5D', '8D']))

    # 90
    print("Full House")
    print("93 = %d" % fullHouse(['2C', '2C', '3C', '3C', '3C']))
    print("92 = %d" % fullHouse(['AC', '2C', 'AC', '2C', '2C']))
    print("-1 = %d" % fullHouse(['2C', '3S', '4S', '5D', '8D']))
    print("-1 = %d" % fullHouse(['2D', '9C', 'AS', 'AH', 'AC']))

    # 105
    print("Four of a kind")
    print("108 = %d" % fourOfAKind(['3C', 'AC', '3C', '3C', '3C']))
    print("119 = %d" % fourOfAKind(['AC', 'AC', 'AC', '2C', 'AC']))
    print("-1 = %d" % fourOfAKind(['2C', '3S', '4S', '5D', '8D']))

    # 120
    print("Straight flush")
    print("126 = %d" % straightFlush(['2C', '3C', '4C', '5C', '6C']))
    print("134 = %d" % straightFlush(['TD', 'JD', 'QD', 'KD', 'AD']))
    print("-1 = %d" % straightFlush(['2C', '3S', '4C', '5C', '6C']))

    # 135
    print("Royal flush")
    print("-1 = %d" % royalFlush(['2C', '3C', '4C', '5C', '6C']))
    print("149 = %d" % royalFlush(['TD', 'JD', 'QD', 'KD', 'AD']))
    print("-1 = %d" % royalFlush(['2C', '3S', '4C', '5C', '6C']))


    # Examples:
    print("1 = %d" % winner([['5H', '5C', '6S', '7S', 'KD'], ['2C', '3S', '8S', '8D', 'TD']]))
    print("0 = %d" % winner([['5D', '8C', '9S', 'JS', 'AC'], ['2C', '5C', '7D', '8S', 'QH']]))
    print("1 = %d" % winner([['2D', '9C', 'AS', 'AH', 'AC'], ['3D', '6D', '7D', 'TD', 'QD']]))
    # print(threeOfAKind(['2D', '9C', 'AS', 'AH', 'AC']))
    # print(flush(['3D', '6D', '7D', 'TD', 'QD']))
    print("0 = %d" % winner([['4D', '6S', '9H', 'QH', 'QC'], ['3D', '6D', '7H', 'QD', 'QS']]))
    print("0 = %d" % winner([['2H', '2D', '4C', '4D', '4S'], ['3C', '3D', '3S', '9S', '9D']]))

# ******************************************************************************
tests()

startTime = time()

file = open("poker.txt", 'r')

poker = file.read().split('\n')
poker = map(separateHands, poker)
scores = [0, 0]
for item in poker:
    scores[winner(item)] += 1

print(scores[0])
print(time() - startTime)