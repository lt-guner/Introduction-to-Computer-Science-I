# Author: Timur Guner
# Date: 2021-02-17
# Description: Project 7b creates a function called reverse_list that takes as a parameter a list and and reverses the
#              order of the elements in that list. It should not return anything - it should mutate the original list.

def reverse_list(list_of_objects):
    """ This function takes a list as a parameter and reverses the order of the elements"""

    # get the length of the list to use for iteration in the for loop
    iterable = int(len(list_of_objects))

    # copy the parameter list to another object to iterate through backwards in the for loop
    copied_list = list(list_of_objects)

    # the for loop reverses the order of the elements of the parameter list by setting the current indexed element in
    # the for loop to the reversed index element in the copied list
    for x in range(0, iterable):
       list_of_objects[x] = copied_list[(iterable - 1) - x]