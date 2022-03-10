# Author: Timur Guner
# Date: 2021-02-10
# Description: Project 6a creates a function that returns the median from a list

def find_median (list_of_numbers):
    """This function takes a list of numbers and returns the median
       If the list contains an even amount of numbers, then the average of the two middle numbers are the median.
       If the list contains an odd amount of numbers, then there is only one middle number for the median"""

    # sort list"
    list_of_numbers.sort()
    print(list_of_numbers)

    # if else to return the median based on if the list has odd or even amount of numbers
    # if the list has an even amount of numbers then we take to two middle numbers and divide by two
    if int(len(list_of_numbers)) % 2 == 0:

        # create the first index and find the first value in the list
        index_1 = int(len(list_of_numbers) / 2 - 1)
        value_1 = list_of_numbers[(index_1)]

        # create the second index and find the second value in the list
        index_2 = int(len(list_of_numbers) / 2)
        value_2 = list_of_numbers[(index_2)]

        # return the average of the two values for the median
        return float((value_1 + value_2) / 2)

    # if the list has an odd amount of numbers then just return the middle number
    else:

        # create the index and pass find the value if the amount in list is odd
        index_odd = int(len(list_of_numbers) / 2)
        value_odd = list_of_numbers[(index_odd)]

        # return the median
        return float(value_odd)

