# Author: Timur Guner
# Date: 2021-01-27
# Description: This file creates for the hailstone sequence

# This function is used to define the hailstone and return the number of steps it took to get to 1
# How the sequence works is shown in the docstring
# If input is 1 then return 0
# Else use a while loop to perform the calculations for even and odd integers until the number reaches 1 then
# return the count of the steps
def hailstone(hailstone_var):
    """This function computers the Hailstone sequence and returns the number of steps it took to get to one.

    A hailstone sequence starts with some positive integer. If that integer is even, then you divide it by two to get
    the next integer in the sequence, but if it is odd, then you multiply it by three and add one to get the next
    integer in the sequence. Then you use the value you just generated to find the next value."""
    hailstone_var = int(hailstone_var)
    hailstone_count = 0
    hailstone_while = 1
    if hailstone_var == 0:
        return hailstone_count
    else:
        while hailstone_while > 0:
            if hailstone_var == 1:
                hailstone_while = 0
            elif hailstone_var % 2 == 0:
                hailstone_var = hailstone_var / 2
                hailstone_count += 1
            else:
                hailstone_var = hailstone_var * 3 + 1
                hailstone_count += 1
        return hailstone_count