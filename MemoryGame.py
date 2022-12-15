import random
import sys
import time


global rand_list
global usr_numbers_list


def generate_sequence(difficulty):
    global rand_list
    rand_list = []
    n = difficulty
    for i in range(n):
        rand_list.append(random.randint(1, 101))
    print(rand_list)
    time.sleep(0.7)
    print("\n" * 100)


def get_list_from_user(difficulty):
    global usr_numbers_list
    usr_numbers_list = []
    n = difficulty
    for i in range(0, n):
        numbers = int(input("Enter the numbers - hit Enter after each number: "))
        usr_numbers_list.append(numbers)

    print(usr_numbers_list)


def is_list_equal():
    if rand_list == usr_numbers_list:
        return True
    else:
        return False


def play(difficulty):
    generate_sequence(difficulty)
    get_list_from_user(difficulty)
    compared_result = is_list_equal()
    if compared_result is True:
        print("You won! :-)")
    else:
        print(f"You lost :-( the generated numbers list was {rand_list}")

