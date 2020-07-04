#https://github.com/fernandofatech

import hangman
import guessing

def select_game():
    print("*********************************")
    print("*******Select your game!*********")
    print("*********************************")

    print("(1) Hangman (2) Guessing")

    game = int(input("Which game? "))

    if(game == 1):
        print("Playing Hangman")
        hangman.game()
    elif(game == 2):
        print("Playing Guessing")
        guessing.game()

if(__name__ == "__main__"):
    select_game()
