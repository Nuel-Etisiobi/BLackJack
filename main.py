import random
from art import logo
from os import system, name
from time import sleep


def clear():
    if name == 'nt':
        _ = system('cls')


##################### Hints #####################

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.#

def deal_card():
    """This function returns a random card"""
    cards = random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
    return cards


# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins.
#If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above,
# then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw."
    if computer_score == 0:
        return "You lose! The dealer has a Blackjack"
    if user_score == 0:
        return "You win with a Blackjack!"
    if user_score > 21:
        return "You lose! You went over 21"
    if computer_score > 21:
        return "You win. The dealer went over 21"
    elif user_score > computer_score:
        return "you win with the highest score"
    else:
        return "You lost to the dealer having the highest score"


# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.
def calculate_score(cards):
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def play_game():
    print(logo)
    # Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    end_of_game = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    # Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

    while not end_of_game:  # Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
        user_score = sum(user_cards)
        computer_score = sum(computer_cards)
        print(f"You cards are {user_cards}, total score {user_score}")
        print(f"Computer first card {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            end_of_game = True

        # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card()
        # function to add another card to the user_cards List. If no, then the game has ended.
        else:
            draw_another_card = input("Do you want to draw another card? 'y' for yes or 'n' for no ")
            if draw_another_card == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                end_of_game = True

    # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())

    print(f"Your final card: {user_cards}, final score {user_score}")
    print(f"Computer final card: {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game
# of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? 'y' for yes or 'n' for no ") == "y":
    clear()
    play_game()
