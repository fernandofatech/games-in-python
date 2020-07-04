#https://github.com/fernandofatech

import random

def game():

    print("*********************************")
    print("**Welcome to the Guessing game!**")
    print("*********************************")

    number_secret = random.randrange(1,101)
    total_attempts = 0
    points = 1000

    print("What is level of difficulty?")
    print("(1) Easy (2) Medium (3) Hard")

    level = int(input("Set the level: "))

    if(level == 1):
        total_attempts = 20
    elif(level == 2):
        total_attempts = 10
    else:
        total_attempts = 5

    for round in range(1, total_attempts + 1):
        print("Attempt {} of {}".format(round, total_attempts))

        shot_str = input("Enter a number between 1 and 100: ")
        print("You typed " , shot_str)
        shot = int(shot_str)

        if(shot < 1 or shot > 100):
            print("You should enter a number between 1 and 100!")
            continue

        hit = shot == number_secret
        bigger   = shot > number_secret
        smaller   = shot < number_secret

        if(hit):
            print("You got it right and you did it {} points!".format(points))
            break
        else:
            if(bigger):
                print("You failed! Your guess was bigger than the secret number.")
            elif(smaller):
                print("You failed! Your guess was less than the secret number.")
            lost_points = abs(number_secret - shot)
            points = points - lost_points

    print("End of the game")

if(__name__ == "__main__"):
    game()
