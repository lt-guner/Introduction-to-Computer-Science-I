# Author: Timur Guner
# Date: 2021-01-13
# Description: gets an input of cents from a user and outputs to quarters, dimes, nickels, pennies

# Ask user for cents between 0-99 and store it in cents
print("Please enter an amount in cents less than a dollar.")
cents = int(input())

# start converting to quarters, dimes, nickels, and cents using % and //
# cents will keep changing by arithmetic when finding each denomination
quarters = cents // 25
cents = cents % 25
dimes = cents // 10
cents = cents % 10
nickels = cents // 5
cents = cents % 5
pennies = cents

# time to print the number of quarters, dimes, nickels, and cents
print("Your change will be:")
print("Q:", quarters)
print("D:", dimes)
print("N:", nickels)
print("P:", pennies)