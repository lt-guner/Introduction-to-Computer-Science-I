# Author: Timur Guner
# Date: 2021-01-20
# Description: ask user for an integer and all divisble integers

# ask user for an integer
user_integer = int(input("Please enter a positive integer: "))
print("The factors of", user_integer, "are:")

# print all the divisors of the integer
for numbers in range(1, user_integer + 1):
    if user_integer % numbers == 0:
        print(numbers)