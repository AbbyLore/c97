print("Let's play a game!  I'm thinking of a number between 1-9.  You have 5 chances to guess!")
import random
number = random.randint(1,9)
chances = 0
while chances < 5:
    guess = int(input("Guess: "))
    if guess == number:
        print("Congrats!  You win!  Have an uwu")
        break
    elif guess < number:
        print("Guess a number higher than", guess)
    else:
        print("Guess a number lower than", guess)


if not chances < 5:
    print("You loose!  The number was", number)