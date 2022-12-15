import MemoryGame
import GuessGame
import CurrencyRouletteGame


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play.")


def load_game():
    print('''Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS''')

    game_num = int(input("Game number:"))
    try:
        if int(game_num) == 0 or int(game_num) > 3:
            print("Sorry, game number doesn't exist")
        elif 0 < int(game_num) <= 3:
            difficulty = int(input("Please choose game difficulty from 1 to 5:"))
            if 0 < int(difficulty) <= 5:
                print("Greate! Let's Play!")
            else:
                print("Sorry, I don't understand your game difficulty")
    except ValueError:
        print("Sorry, I don't understand your game difficulty")

    if game_num == 1:
        MemoryGame.play(difficulty)
    elif game_num == 2:
        GuessGame.play(difficulty)
    elif game_num == 3:
        CurrencyRouletteGame.play(difficulty)

    return difficulty


