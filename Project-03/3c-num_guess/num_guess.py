# Author: Timur Guner
# Date: 2021-01-20
# Description: Ask user for input and then guess the input while telling the user
#              if the number is higher or lower and printing the number of tries

# ask user for input integer and set guess count
print("Enter the integer for the player to guess.")
user_number_input = int(input())
guess_count = 1

# have the user try the first guess
print("Enter your guess.")
guess_number_input = int(input())

# if the first guess if correct tell the user or go into an else
# use a loop to tell the user if they guessed too high or too low have have them guess again
if guess_number_input == user_number_input:
    print("You guessed it in 1 try.")
else:
    while guess_number_input != user_number_input:
        guess_count += 1
        if guess_number_input > user_number_input:
            print("Too high - try again:")
            guess_number_input = int(input())
        else:
            print("Too low - try again:")
            guess_number_input = int(input())
    print("You guessed it in", guess_count, "tries.")