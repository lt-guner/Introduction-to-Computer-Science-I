# Author: Timur Guner
# Date: 2021-02-24
# Description: Project 8b creates a function called words_in_both that takes two strings. The strings are then compared
#              and a set of common words produced.

def words_in_both(input_string_1, input_string_2):
    """Function words_in_both takes two strings and creates sets from both strings.
        The intersect of both sets is then returned."""

    # set both strings to lower case for comparison later
    input_string_1 = input_string_1.lower()
    input_string_2 = input_string_2.lower()

    # the words from both strings are split and saved to two sets
    set_a = set(input_string_1.split())
    set_b = set(input_string_2.split())

    # return the intersect of set_a and set_b
    return set_a & set_b