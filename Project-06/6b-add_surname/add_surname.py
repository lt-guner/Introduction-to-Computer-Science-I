# Author: Timur Guner
# Date: 2021-02-10
# Description: Project 6B creates a function to take a list of first names and add the surname Kardashian using
#              list comprehension

def add_surname(first_names):
    """Takes a list of first names and adds the surname Kardashian if the first name starts with K"""
    return [fn + " Kardashian" for fn in first_names if fn[0] == "K"]