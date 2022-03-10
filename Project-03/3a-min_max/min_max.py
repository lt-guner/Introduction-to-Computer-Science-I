# Author: Timur Guner
# Date: 2020-01-20
# Description: Ask user for how many numbers they want to enter
#              User enters the amount numbers they wanted to enter
#              Display the min and the max of the entered numbers

# Saving how many numbers the user wants to enter and set min and max
print("How many integers would you like to enter?")
total_number = int(input())


# get first umber from user to set it as both min and max
print("Please enter", total_number, "integers.")
intermediate_number = int(input())
max_number = intermediate_number
min_number = intermediate_number
total_number -= 1

# use a while to change the min and max numbers if needed
while total_number > 0:
    entered_number = int(input())
    if entered_number >= max_number:
        max_number = entered_number
    elif entered_number <= min_number:
        min_number = entered_number
    total_number -= 1

#print min and max
print("min:", min_number)
print("max:", max_number)