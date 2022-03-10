# Author: Timur Guner
# Date: 2021-01-27
# Description: This file creates a function to determine fibonacci sequence based on the integer
#              integer input from the user

# We first assign the the first 2 numbers in the fibonacci which are both 1 fib_spot_1 and fib_spot_2.
# If the user enters sequence spot 1 or spot 2 then it will return 1 in the if statement.
# If the user enters sequence spot 3 or higher then it will go through a while loop.
# The while loop is loops through as long as the sequence input is greater than 2.
# The reason the conditional is greater than 2 is because we already cover spot 1 and spot 2 from the first part of If.
# We assign variable of spot 2 to a placeholder, make spot 2 = spot 2 + spot 1, and assign the place hold to spot 1.

def fib(fib_sequence_var):
    """This returns returns the fibonacci number based on the sequence input from the user.
       Example fib(10) would return 55 or fib(3) would return 2."""
    fib_sequence_var = int(fib_sequence_var)
    fib_spot_1 = 1
    fib_spot_2 = 1
    fib_spot_holder = 0
    if fib_sequence_var == 1 or fib_sequence_var == 2:
        return 1
    else:
        while fib_sequence_var > 2:
            fib_spot_holder = fib_spot_2
            fib_spot_2 = fib_spot_2 + fib_spot_1
            fib_spot_1 = fib_spot_holder
            fib_sequence_var -= 1
        return fib_spot_2