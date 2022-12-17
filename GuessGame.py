from random import *


def generate_number(difficulty):
    secret_number = randint(1, int(difficulty))
    return secret_number


def get_guess_from_user(difficulty):
    user_input = input(f"Enter your guess between 1 to {difficulty}:")
    guess = int(user_input)
    print(guess)
    return guess


def compare_results(secret_number, guess):
    if secret_number == guess:
        return True
    else:
        return False


def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)

    if compare_results(secret_number, guess):
        print("You won! :-)")
    else:
        print(f"You lost :-( the correct answer was {secret_number}")
