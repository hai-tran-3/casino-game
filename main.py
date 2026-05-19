#!/usr/bin/env python3
"""
Created by: Hai Tran
Created on: May 2026
This is a casino game
"""

import random

player_hand = []
dealer_hand = []

deck_of_card = ["ace of hearts", "two of hearts", " three of hearts", "four of hearts", 
                "five of hearts", "six of hearts", " seven of hearts", "eight of hearts", 
                "nine of hearts", "ten of hearts", " jack of hearts", "queen of hearts", "king of hearts",

                "ace of diamonds", "two of diamonds", " three of diamonds", "four of diamonds", 
                "five of diamonds", "six of diamonds", " seven of diamonds", "eight of diamonds", 
                "nine of diamonds", "ten of diamonds", " jack of diamonds", "queen of diamonds", "king of diamonds",

                "ace of clubs", "two of clubs", " three of clubs", "four of clubs", 
                "five of clubs", "six of clubs", " seven of clubs", "eight of clubs", 
                "nine of clubs", "ten of clubs", " jack of clubs", "queen of clubs", "king of clubs",

                "ace of spades", "two of spades", " three of spades", "four of spades", 
                "five of spades", "six of spades", " seven of spades", "eight of spades", 
                "nine of spades", "ten of spades", " jack of spades", "queen of spades", "king of spades",
            ]

card_values = {"ace of hearts": 0, "two of hearts": 2, " three of hearts": 3, "four of hearts": 4, 
                "five of hearts": 5, "six of hearts": 6, " seven of hearts": 7, "eight of hearts": 8, 
                "nine of hearts": 9, "ten of hearts": 10, " jack of hearts": 10, "queen of hearts": 10, "king of hearts": 10,

                "ace of diamonds": 0, "two of diamonds": 2, " three of diamonds": 3, "four of diamonds": 4, 
                "five of diamonds": 5, "six of diamonds": 6, " seven of diamonds": 7, "eight of diamonds": 8, 
                "nine of diamonds": 9, "ten of diamonds": 10, " jack of diamonds": 10, "queen of diamonds": 10, "king of diamonds": 10,

                "ace of clubs": 0, "two of clubs": -2, " three of clubs": -3, "four of clubs": -4, 
                "five of clubs": -5, "six of clubs": -6, " seven of clubs": -7, "eight of clubs": -8, 
                "nine of clubs": -9, "ten of clubs": -10, " jack of clubs": -10, "queen of clubs": -10, "king of clubs": -10,

                "ace of spades": 0, "two of spades": -2, " three of spades": -3, "four of spades": -4, 
                "five of spades": -5, "six of spades": -6, " seven of spades": -7, "eight of spades": -8, 
                "nine of spades": -9, "ten of spades": -10, " jack of spades": -10, "queen of spades": -10, "king of spades": -10,
            }

def main() -> None:
    """The main() function do the input and the output, returns None."""
    playing_deck = deck_of_card
    
    initial_card = random.sample(playing_deck, 2)
    player_hand.extend(initial_card)
    for cards in initial_card:
        playing_deck.remove(cards)
    print(player_hand)
    initial_card = random.sample(playing_deck, 2)

    dealer_hand.extend(initial_card)
    for cards in initial_card:
        playing_deck.remove(cards)
    print(dealer_hand)


if __name__ == "__main__":
    main()