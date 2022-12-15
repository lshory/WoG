from random import randint
from currency_converter import CurrencyConverter


global guess
amount = randint(1, 100)
c = CurrencyConverter()


def get_money_interval(difficulty):
    current_currency = c.convert(amount, 'USD', 'ILS')
    interval = (current_currency - (5 - difficulty), current_currency + (5 - difficulty))
    return interval


def get_guess_from_user():
    global guess
    guess = int(input(f"Enter a guess of the ILS value of {amount}: "))


def play(difficulty):
    get_money_interval(difficulty)
    get_guess_from_user()
    global guess
    if get_money_interval(difficulty)[0] <= guess <= get_money_interval(difficulty)[1]:
        print(f"You won! :-) {guess} is correct!")
        return True
    else:
        print(f"You lost :-( {guess} is not a correct guess")
        return False


