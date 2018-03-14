# coding: utf-8
"""Guessing Game: Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(_Hint: remember to use the user input lessons from the very first exercise
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""

from random import randint

print "Welcome to the guessing game!"
rand_number = randint(1,9)
print rand_number

def guessingGame(random):
    option = ''
    guess = 0
    while (option != 'exit'):  
        user_input = input("Enter a number between 1 and 9:")
        if (user_input < 1 or user_input > 9):
            print "Invalid number. Please try again"
        else:
            if (user_input < random):
                print "Guessed number is too low"
                guess += 1
            elif (user_input > random):
                print "Guessed number is too high"
                guess += 1
            elif (user_input == random):
                print "Congratulations! You are right."
                guess += 1
                break
        option = raw_input("Do you want to try again? (yes/exit):")
    print "Total number of guesses are {0}".format(guess)
    print "End of Game!"
    
guessingGame(rand_number)  
