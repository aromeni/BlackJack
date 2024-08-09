import random
from blackjack_logo import blackjack_logo

def deal_card():
    '''Returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''Takes a list of cards and returns the score calculated from the cards'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # This represents a blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(u_score, comp_score):
    if u_score == comp_score:
        return "It's a draw!"
    elif comp_score == 0:
        return "You lose, the opponent has Blackjack!"
    elif u_score == 0:
        return "You win with a Blackjack!"
    elif u_score > 21:
        return "You went over 21. You lose!"
    elif comp_score > 21:
        return "Opponent went over 21. You win!"
    elif u_score > comp_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    print(blackjack_logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())  # Call the function with ()
        computer_cards.append(deal_card())  # Call the function with ()

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or user_score > 21 or computer_score == 0:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Implement computer's turn logic
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    # Call the compare function with the correct arguments
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Black Jack. Type 'y' or 'n': ") == "y":
    play_game()

