# Author: Timur Guner
# Date: 2021-02-17
# Description: Project 7a creates function named square_list that takes as a parameter a list of numbers
#              and replaces each value with the square of that value. It mutates the original list.

def square_list(list_of_numbers):
    """This function takes as a parameter a list of numbers and replaces each value with
       the square of that value. It mutates the original list."""

    # we need to set the length of the list to use in the for loop
    list_length = len(list_of_numbers)

    # the for loop iterates through each value in the list and squares it
    for x in range(0, list_length):
       list_of_numbers[x] = list_of_numbers[x] ** 2