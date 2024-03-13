#!/usr/bin/env python3
#Created by PepeBigotes

from random import shuffle
from time import sleep
from random import randint
import os

# DEFINE CARD VALUES HERE:
VALUES =  {
    +2: [ #++++++++++++++++++++
        
        ],
    +1.5: [
        
          ],
    +1: [
    " 2♠", " 2♥", " 2♦", " 2♣",
    " 3♠", " 3♥", " 3♦", " 3♣",
    " 4♠", " 4♥", " 4♦", " 4♣",
    " 5♠", " 5♥", " 5♦", " 5♣",
    " 6♠", " 6♥", " 6♦", " 6♣",
    " 7♠", " 7♥", " 7♦", " 7♣",
    " 8♠", " 8♥", " 8♦", " 8♣",
    " 9♠", " 9♥", " 9♦", " 9♣",

        ],
    +0.5: [
        
          ],
    0: [ #+++++++++++++++++++++
       ], #--------------------
    -0.5: [
        
          ],
    -1: [
        
        ],
    -1.5: [
        
          ],
    -2: [
    "10♠", "10♥", "10♦", "10♣",
    " J♠", " J♥", " J♦", " J♣",
    " Q♠", " Q♥", " Q♦", " Q♣",
    " K♠", " K♥", " K♦", " K♣",
    " A♠", " A♥", " A♦", " A♣",

        ], #-------------------
}

value = 0


def shuffled_deck():
   deck = []
   for i in VALUES: deck += VALUES[i]
   deck = deck * 6
   shuffle(deck)
   return deck

def get_card_value(card: str):
    for i in VALUES:
        if card in VALUES[i]: value = i
    return value

def deal_cards(cards: list):
    cards_num = len(cards)
    if not cards_num in (4, 6, 8, 10, 12, 14): raise Exception("Invalid number of cards to deal")

    global value
    for card in cards:
        value += get_card_value(card)

    print(f"DEALER: {cards[0]} {cards[1]}")
    hand = []
    for card in cards[2:]:
        hand.append(card)
        if len(hand) == 2:
            print(f"  HAND: {hand[0]} {hand[1]}")
            hand = []

def show_card(card: str):
    print(f"card: {card}")

def ask_card(card: str):
    global value

os.system('cls' if os.name=='nt' else 'clear')
print(f"""{str.center("Welcome to PepeBigotes' BlackJack Card Counting Game", 80)}
-------------------------------------------------------------------------------
All cards have another "hidden" value other than their original blackjack value
and your goal is to keep count of that hidden value and answer correctly when
you get asked about it.
You can stop the script whenever you want by pressing CTRL+C.

Here is the "hidden" cards value (you can change them inside the script btw):
""")

for i in VALUES:
    if len(VALUES[i]) > 0:
        print(f"Cards worth {i if i <= 0 else f'+{i}'}: ", end='')
        for card in VALUES[i]:
            print(card, end=' ')
        print()

deck = shuffled_deck()

try:
    hands_num = eval(input("\nHow many hands would you like to play at the same time? (1-6) "))
    if not hands_num in range(1,6): print("Invalid hands number, minimun 1, maximum 6"); exit(1)
    cards_per_deal = 2 + hands_num*2
    print(f"Okay, dealing {hands_num} hands ({cards_per_deal} cards) at the same time...")

    while True:
        print(f" Cards left: {len(deck)}")
        deal_cards(deck[:cards_per_deal])
        deck = deck[cards_per_deal:]
        input()
        if randint(0,2) == 0:
            ans = eval(input("What's the current value? "))
            if ans == value: input("Correct!")
            else: input(f"Nah, it's {value}")
            print("----------------------------")
        if len(deck) <= 30:
            print("The deck has been shuffled")
            deck = shuffled_deck
except SyntaxError: print('\nI did not understand that "number" of yours, bye'); exit(1)
except KeyboardInterrupt: print("\nKeyboardInterrupt"); exit()
