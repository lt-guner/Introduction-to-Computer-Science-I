# Author: Timur Guner
# Date: 2021-02-10
# Description: Project 6c creates a class called Person that stores name and variable. A function called std_dev
#              takes a list of objects that were created using Person and calculates the standard deviation of the ages

class Person:
    """The class Person has two private members to store the person's name and age. It also has a get_age method"""

    def __init__(self, person_name, person_age):
        """Creates an object with the person's name and age"""
        self._person_name = str(person_name)
        self._person_age = int(person_age)

    def get_age(self):
        """Method that returns the person's age"""
        return self._person_age

def std_dev(people_list):
    """std_dev produces the standard deviation from a list of people's ages"""

    # set variables to 0 for later use in the calculation
    # the comments in the other sections explain more about each variable
    total_age = 0
    age_variances = 0

    # sum up the ages in the list
    for age in people_list:
        total_age += age.get_age()

    # get average
    average_age = total_age / int(len(people_list))

    # calculate the total age variance
    for age2 in people_list:
        age_variances += (age2.get_age() - average_age) ** 2

    # divide total age variance by population to get the actual variance
    actual_variance = age_variances / int(len(people_list))

    # square the actual age variance to get the standard deviation
    standard_deviation = actual_variance ** .5

    # return the standard deviation
    return standard_deviation