#Guessing Game..........
#Generates random number between 1 to 10
#import


import random
# Generates a random number

number = random.randint(1,10)
print("Welcome to the game!!!")
player_name = input("Hello,What's your name?").strip()
print("Hello {}!".format(player_name),"I am guessing a number between 1 and 10")
print("  Try to guess....   ")

#resticting number of guesses to 3


for i in range(0,3):
    num_guess = int(input())
    i+=1 
    if num_guess<number:
        print("Your guess is too low..........")
    elif num_guess>number:
        print("Your guess is too high..........")
    elif num_guess == number:
        break


if num_guess==number:
    print("Correct Guess,You guessed in {} number of tries.....".format(i))
else:
    print("You lose the game")
    print("Wrong guess,The correct number was {}".format(number))