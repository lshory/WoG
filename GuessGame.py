from random import *

global secret_number
global guess


def generate_number(difficulty):
    global secret_number
    secret_number = randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    global guess
    user_input = input(f"Enter your guess between 1 to {difficulty}:")
    guess = int(user_input)
    print(guess)
    return guess


def compare_results():
    if secret_number == guess:
        return True
    else:
        return False


def play(difficulty):
    generate_number(difficulty)
    get_guess_from_user(difficulty)
    compared_result = compare_results()
    if compared_result is True:
        print("You won! :-)")
    else:
        print(f"You lost :-( the generated number was {secret_number}")


