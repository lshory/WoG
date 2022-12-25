import os
import random
import time

import Utils


def generate_sequence(difficulty):
    rand_list = []
    n = int(difficulty)
    for i in range(n):
        rand_list.append(random.randint(1, 101))
    print(rand_list)
    time.sleep(0.7)
    Utils.screen_cleaner()

    return rand_list


def get_list_from_user(difficulty):
    usr_numbers_list = []
    n = int(difficulty)
    for i in range(0, n):
        numbers = int(input("Enter the numbers - hit Enter after each number: "))
        usr_numbers_list.append(numbers)

    print(usr_numbers_list)
    return usr_numbers_list


def is_list_equal(sequence, guess):
    for i in range(0, len(guess)):
        guess[i] = int(guess[i])
    return guess == sequence


def play(difficulty):
    sequence = generate_sequence(difficulty)
    guess = get_list_from_user(difficulty)

    if is_list_equal(sequence, guess):
        print("You won! :-)")
    else:
        print(f"You lost :-( the correct answer was {sequence}")
