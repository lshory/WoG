import MemoryGame
import GuessGame
import CurrencyRouletteGame
import Utils
from Score import add_score


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play.")


def load_game():
    print('''Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS''')

    game_num = input("Game number:")
    if game_num.isnumeric() is False:
        print("Please enter a number")
        load_game()
    elif 4 > int(game_num) > 0:
        return game_num
    else:
        print("Sorry, game number:", game_num, "doesn't exist, please choose from the existing options")


def game_difficulty():
    difficulty = input("Please choose game difficulty from 1 to 5:")
    if difficulty.isnumeric() is False:
        print("Please enter a number")
    elif 6 > int(difficulty) > 0:
        print("Difficulty level: ", difficulty, "Greate! Let's Play!")
        return difficulty
    else:
        print("Sorry, I don't understand your game difficulty", difficulty, "please choose from the existing options")


def play(game_num, difficulty):
    if game_num == '1':
        MemoryGame.play(difficulty)
        if bool(MemoryGame) is True:
            add_score(difficulty)
    elif game_num == '2':
        GuessGame.play(difficulty)
        if bool(GuessGame) is True:
            add_score(difficulty)
    elif game_num == '3':
        CurrencyRouletteGame.play(difficulty)
        if bool(CurrencyRouletteGame) is True:
            add_score(difficulty)

    return int(difficulty)


def play_again():
    check_play_again = input("Do you want to play again? (Y/N)")
    if check_play_again.lower() == "y":
        play(load_game(), game_difficulty())
        Utils.screen_cleaner()
    else:
        print("Ok, see you later")
