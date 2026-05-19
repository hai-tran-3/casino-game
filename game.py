import random

# --- GAME SETUP ---
def create_deck():
    """Creates a standard 52-card deck with ranks and suits."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = []
    for suit in suits:
        color = 'Red' if suit in ['Hearts', 'Diamonds'] else 'Black'
        for rank in ranks:
            deck.append({'rank': rank, 'suit': suit, 'color': color})
    random.shuffle(deck)
    return deck

def is_instant_win(hand):
    """Checks if a hand has exactly two Aces of different colors."""
    if len(hand) != 2:
        return False
    if hand[0]['rank'] == 'Ace' and hand[1]['rank'] == 'Ace':
        return hand[0]['color'] != hand[1]['color']
    return False

def calculate_best_score(hand):
    """Calculates the score closest to 0, handling flexible Ace values."""
    base_score = 0
    ace_count = 0
    
    # Calculate non-Ace cards and count Aces
    for card in hand:
        sign = 1 if card['color'] == 'Red' else -1
        if card['rank'] in ['Jack', 'Queen', 'King', '10']:
            base_score += 10 * sign
        elif card['rank'] != 'Ace':
            base_score += int(card['rank']) * sign
        else:
            ace_count += 1

    if ace_count == 0:
        return base_score

    # Evaluate all possible combinations for Aces (each can be 1, 10, or 11)
    possible_values = [1, 10, 11]
    best_score = None
    best_distance = float('inf')

    # Recursive helper to try every combination of the Aces in the hand
    def evaluate_aces(current_score, aces_left):
        nonlocal best_score, best_distance
        if aces_left == 0:
            distance = abs(current_score)
            # We prefer non-busting scores. If both bust, prefer the lower distance.
            if distance <= 18 and distance < best_distance:
                best_distance = distance
                best_score = current_score
            elif best_score is None or (best_distance > 18 and distance < best_distance):
                best_distance = distance
                best_score = current_score
            return

        # Current Ace's sign depends on its color
        current_ace_card = hand[-aces_left]
        sign = 1 if current_ace_card['color'] == 'Red' else -1
        for val in possible_values:
            evaluate_aces(current_score + (val * sign), aces_left - 1)

    evaluate_aces(base_score, ace_count)
    return best_score

def display_hand(name, hand):
    """Formats and prints a player's hand and current best score."""
    cards_str = ", ".join([f"{c['rank']} of {c['suit']} ({c['color']})" for c in hand])
    score = calculate_best_score(hand)
    print(f"{name}'s Hand: {cards_str}")
    print(f"Current Score: {abs(score)}\n")

# --- GAMEPLAY LOOP ---
def play_game():
    deck = create_deck()
    
    # Deal initial 2 cards
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("--- INITIAL DEAL ---")
    display_hand("Player", player_hand)

    # Check Instant Win condition immediately
    player_instant = is_instant_win(player_hand)
    dealer_instant = is_instant_win(dealer_hand)

    if player_instant or dealer_instant:
        print("--- INSTANT WIN CHECK ---")
        display_hand("Dealer", dealer_hand)
        if player_instant and dealer_instant:
            print("Incredible! Both got 2 colored Aces. It's a DRAW!")
        elif player_instant:
            print("PLAYER INSTANT WIN! (Double Payout!)")
        else:
            print("DEALER INSTANT WIN!")
        return

    # --- PLAYER'S TURN ---
    print("--- PLAYER'S TURN ---")
    cards_drawn = 0
    while cards_drawn < 3:
        choice = input(f"Draw another card? ({3 - cards_drawn} left) [y/n]: ").strip().lower()
        if choice == 'y':
            new_card = deck.pop()
            player_hand.append(new_card)
            print(f"\nDrew: {new_card['rank']} of {new_card['suit']} ({new_card['color']})")
            display_hand("Player", player_hand)
            cards_drawn += 1
        else:
            break

    player_score = calculate_best_score(player_hand)
    player_bust = abs(player_score) > 18

    # --- DEALER'S TURN ---
    print("\n--- DEALER'S TURN ---")
    display_hand("Dealer", dealer_hand)
    
    dealer_drawn = 0
    while dealer_drawn < 3:
        dealer_score = calculate_best_score(dealer_hand)
        # Dealer must stand if distance is 12 or closer to 0 (since min 12 points required to check)
        if abs(dealer_score) <= 12:
            print("Dealer satisfies the minimum threshold to stay.")
            break
            
        # Otherwise, dealer takes a card to try and get closer to 0
        new_card = deck.pop()
        dealer_hand.append(new_card)
        print(f"Dealer draws: {new_card['rank']} of {new_card['suit']} ({new_card['color']})")
        display_hand("Dealer", dealer_hand)
        dealer_drawn += 1

    dealer_score = calculate_best_score(dealer_hand)
    dealer_bust = abs(dealer_score) > 18

    # --- FINAL RESOLUTION ---
    print("--- FINAL RESULT ---")
    p_dist = abs(player_score)
    d_dist = abs(dealer_score)
    
    print(f"Player Final Score: {p_dist} {'(BUSTED)' if player_bust else ''}")
    print(f"Dealer Final Score: {d_dist} {'(BUSTED)' if dealer_bust else ''}\n")

    if player_bust and dealer_bust:
        print("Both players busted! It's a DRAW.")
    elif player_bust:
        print("Player busted! DEALER WINS.")
    elif dealer_bust:
        print("Dealer busted! PLAYER WINS.")
    elif p_dist == d_dist:
        print("Equal Score It's a DRAW.")
    elif p_dist < d_dist:
        print("PLAYER WINS (Closer to 0)!")
    else:
        print("DEALER WINS (Closer to 0)!")

if __name__ == "__main__":
    play_game()