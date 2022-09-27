# Importing modules
import random
playerIn = True
dealerIn = True

# Deck of cards / player and dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A",]
playerHand = []
dealerHand = []

# deealing the cards
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# determining the total value of the cards
def total(turn):
    total = 0
    ace_11s = 0
    for card in turn:
        if card in range(11):
            total += card
        elif card in ["J", "Q", "K"]:
            total + 10
        else:
            total += 11
            ace_11s += 1
    while ace_11s and total > 21:
        total -= 10
        ace_11s -= 1
    return total

# Check for winner
def revealDealerHand():
        if len(dealerHand) == 2:
            return dealerHand[0]
        elif len(dealerHand) > 2:
            return dealerHand[0], dealerHand[1]

# the game loop
for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

while playerIn or dealerIn:
    print(f"Dealer had an {revealDealerHand()} and X")
    print(f"You have {playerHand()} for a total of {total(playerHand)}.")
    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if total(dealerHand) > 16:
        dealerIn = False

