#!/usr/bin/env python3
"""
Created by: Hai Tran
Created on: May 2026
This is a blackjack game
"""

import random

# Setup constants for the game
SUITS = ["♥", "♦", "♣", "♠"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}


def create_deck():
    """Creates a shuffled 52-card deck."""
    deck = [{"rank": rank, "suit": suit} for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck


def calculate_score(hand):
    """Calculates the total value of a hand, adjusting Aces if necessary."""
    score = sum(VALUES[card["rank"]] for card in hand)

    # Adjust for Aces if the score is over 21
    aces = sum(1 for card in hand if card["rank"] == "A")
    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score


def format_hand(hand):
    """Returns a string representation of a hand."""
    return ", ".join(f"{card['rank']}{card['suit']}" for card in hand)


def play_blackjack():
    print("--- Welcome to Terminal Blackjack! ---")

    deck = create_deck()

    # Deal initial hands
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Player's Turn
    while True:
        player_score = calculate_score(player_hand)
        print(f"\nYour hand: {format_hand(player_hand)} (Score: {player_score})")
        print(f"Dealer's visible card: {dealer_hand[0]['rank']}{dealer_hand[0]['suit']}")

        if player_score == 21:
            print("Blackjack! You stand.")
            break
        elif player_score > 21:
            print("Bust! You went over 21.")
            return

        choice = input("Do you want to [H]it or [S]tand? ").strip().lower()
        if choice == "h":
            player_hand.append(deck.pop())
        elif choice == "s":
            break
        else:
            print("Invalid input. Please enter 'H' or 'S'.")

    # Dealer's Turn
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print(
        f"\nDealer's full hand: {format_hand(dealer_hand)} (Score: {dealer_score})"
    )

    # Dealer must hit until they reach at least 17
    while dealer_score < 17:
        print("Dealer hits...")
        dealer_hand.append(deck.pop())
        dealer_score = calculate_score(dealer_hand)
        print(
            f"Dealer's hand: {format_hand(dealer_hand)} (Score: {dealer_score})"
        )

    # Determine Winner
    print("\n--- Final Results ---")
    if dealer_score > 21:
        print("Dealer busted! You win! 🎉")
    elif player_score > dealer_score:
        print(f"You score {player_score} vs Dealer's {dealer_score}. You win! 🎉")
    elif player_score < dealer_score:
        print(f"You score {player_score} vs Dealer's {dealer_score}. Dealer wins. 😔")
    else:
        print(f"Both scored {player_score}. It's a tie (Push)! 🤝")


if __name__ == "__main__":
    while True:
        play_blackjack()
        again = (
            input("\nWould you like to play another round? (y/n): ")
            .strip()
            .lower()
        )
        if again != "y":
            print("Thanks for playing!")
            break