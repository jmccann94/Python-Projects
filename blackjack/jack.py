#!/usr/bin/python3

import os
import io
import random
import string

# Player
class Player:
    def __init__(self):
        self.hand = []
        self.score1 = 0
        self.score2 = 0

# Card
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

# List of suits and values and points 
colors = ['hearts', 'diamonds', 'spades', 'clubs']
values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', 'jack', 'queen', 'king']
points1 = {'ace' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8
    , '9' : 9, 'jack' : 10, 'queen' : 10, 'king' : 10}
points2 = {'ace' : 11, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8
    , '9' : 9, 'jack' : 10, 'queen' : 10, 'king' : 10}

# dealer and player deck and bust checks
player = Player()
dealer = Player()
playerBust = False
dealerBust = False
deck= []

def initialize():
    # initialize deck of cards
    global deck
    global player
    global dealer
    deck = []
    deck = [Card(value, color) for value in values for color in colors]

    # initialize players scores and hands to prevent score pour over
    player.score1 = 0
    player.score2 = 0
    dealer.score1 = 0
    dealer.score2 = 0
    player.hand = []
    dealer.hand = []

    # shuffle the deck and print to verify
    shufDeck = deck
    random.shuffle(deck )

    # Dealing cards to player and dealer
    dealer.hand.append(deck.pop())
    dealer.hand.append(deck.pop())
    player.hand.append(deck.pop())
    player.hand.append(deck.pop())

    # Print players hand and add up points
    print("Begin Game")
    print("Players Hand:")
    for c in player.hand:
        print(c.value + " of " + c.color)
        player.score1 = player.score1 + points1[c.value]
        player.score2 = player.score2 + points2[c.value]
    for c in dealer.hand:
        dealer.score1 = dealer.score1 + points1[c.value]
        dealer.score2 = dealer.score2 + points2[c.value]

    # Print players points
    print(str(player.score1) + " Ace as 1 point")
    print(str(player.score2) + " Ace as 11 points")

# Function for accepting y or n
def yesOrno(x):
    while True:
        if x not in ("n", "y", "N", "Y"):
            print("Try Again")
        elif x in ("n", "N"):
            return False
        elif x in ("y", "Y"):
            return True
        x = input("Enter y/n:")

# calculates players final score
def playerScoreEnd():
    global player
    if player.score1 > 21:
        return player.score1
    elif player.score1 > 21 and player.score2 > 21:
        return player.score1
    else:
        return player.score2

# Draws for player 
def playerDraw():
    global deck
    global player
    global playerBust

    # Draw
    player.hand.append(deck.pop())

    # Reset score
    player.score1 = 0
    player.score2 = 0

    # Print hand and add score
    print("Player Hand:")
    for c in player.hand:
        print(c.value + " of " + c.color)
        player.score1 = player.score1 + points1[c.value]
        player.score2 = player.score2 + points2[c.value]
    if player.score1 and player.score2 > 21:
        playerBust = True
        finishGame()
    
    #Dealer Draw
    dealerDraw()

    #Print player Score
    print(str(player.score1) + " Ace as 1 point")
    print(str(player.score2) + " Ace as 11 points")

# Draws for dealer
def dealerDraw():
    global deck
    global dealer
    global dealerBust

    # Checks for Bust
    if dealer.score1 > 21:
        dealerBust = True
        finishGame()
    
    # Draws if either score is below 17
    if dealer.score2 < 17 and dealer.score1 < 17:
        dealer.hand.append(deck.pop())

        # Resets and totals score
        dealer.score1 = 0
        dealer.score2 = 0
        for c in dealer.hand:
            dealer.score1 = dealer.score1 + points1[c.value]
            dealer.score2 = dealer.score2 + points2[c.value]
    
# Totals Dealer final score
def dealerScoreEnd():
    global dealerBust

    # Ensures dealer did not bust
    if not dealerBust:
        while dealer.score2 < 17 and dealer.score1 < 17:
            dealerDraw()

    # decides which total to return 
    if dealer.score1 > 21:
        dealerBust = True
    if dealer.score2 > 21:
        return dealer.score1
    elif dealer.score1 > 21 and dealer.score2 > 21:
        return dealer.score2
    else:
        return dealer.score1

# Calculates score and decides winner
def finishGame():
    global player
    global dealer
    playerScore = playerScoreEnd()
    dealerScore = dealerScoreEnd()

    # Prints player and dealer hands
    print("Players Hand:")
    for c in player.hand:
        print(c.value + " of " + c.color)
        player.score1 = player.score1 + points1[c.value]
        player.score2 = player.score2 + points2[c.value]
    print("Dealers Hand:")
    for c in dealer.hand:
        print(c.value + " of " + c.color)
        dealer.score1 = dealer.score1 + points1[c.value]
        dealer.score2 = dealer.score2 + points2[c.value]

    # Decides Winner
    if playerBust:
        print("You Busted, You Loose!\nPlayer Score: " + str(playerScore))
        print("Player Score: " + str(playerScore)+ "\nDealer Score: " + str(dealerScore))
    elif dealerBust:
        print("Dealer Busted, You Win")
        print("Player Score: " + str(playerScore)+ "\nDealer Score: " + str(dealerScore))
    elif playerScore < dealerScore:
        print("You Loose!")
        print("Player Score: " + str(playerScore)+ "\nDealer Score: " + str(dealerScore))
    elif playerScore > dealerScore:
        print("You Win!")
        print("Player Score: " + str(playerScore)+ "\nDealer Score: " + str(dealerScore))
    elif dealerScore == playerScore:
        print("Tie Game!")
        print("Player Score: " + str(playerScore)+ "\nDealer Score: " + str(dealerScore))
    
    # Prompts to play again
    x = input("Would You Like To Play Again? (y/n) ")
    if yesOrno(x):
        initialize()
    else:
        exit()

    


#game loop
initialize()
while True:
    
    x = input("Would you like to draw? (y/n) ")
    if yesOrno(x):
        playerDraw()
        if playerBust:
            finishGame()    
    else:
        finishGame()





# Rules
# Basic premise is to get as closer to 21 (without going over) than the dealer
# Ace can be 1 or 11
# 2 - 10 are as is
# Jack, Queen, and King are counted as 10
# Suit means nothing
# A tie means your bet stays in the circle
# if both you and the dealer bust than you get your bet back
# if the dealer bust you win, and if you bust you lose
# if you draw a face card and an ace you win with a blackjack
# dealer must draw until atleast 17
