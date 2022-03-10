# Author: Timur Guner
# Date: 2021-02-03
# Description: Function named multiply that takes two positive integers as parameters and returns the product
#              of those two numbers (the result from multiplying them together)

def multiply(num_1, num_2):
    """This function multiplies two numbers together using addition by recursion.
       First integer that is entered is added together as many times by recursion based on the second integer input."""

    # set num_1 and num_2 to integers
    num_1 = int(num_1)
    num_2 = int(num_2)

    # if num_2 is finally down to 1, we end the process
    if num_2 == 1:
        return num_1

    # add num_1 to the previous recursive call using num_2 - 1 and passing num_1 as is
    return num_1 + multiply(num_1, (num_2 - 1))