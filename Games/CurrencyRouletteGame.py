from random import randint
from currency_converter import CurrencyConverter


amount = randint(1, 100)
c = CurrencyConverter()


def get_money_interval(difficulty):
    current_currency = c.convert(amount, 'USD', 'ILS')
    interval = (current_currency - (5 - int(difficulty)), current_currency + (5 - int(difficulty)))
    return interval


def get_guess_from_user():
    guess = int(input(f"Enter a guess of the ILS value of {amount}: "))
    return guess


def play(difficulty):
    interval = get_money_interval(difficulty)
    guess = get_guess_from_user()

    if interval[0] <= guess <= interval[1]:
        print(f"You won! :-) {guess} is correct!")
        return True
    else:
        print(f"You lost :-( {guess} is not a correct guess")
        return False



