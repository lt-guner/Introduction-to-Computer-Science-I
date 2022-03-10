# Author: Timur Guner
# Date: 2021-01-27
# Description: This program gets an input for number of seconds and uses a function to display
#              how far the object has fallen

# function to calculate the distance an object has fallen
def fall_distance(time_var):
    """This function returns the distance an object has fallen in meters based on the time (seconds) from the input"""
    time_var = float(time_var)
    time_var = (1/2) * 9.8 * time_var ** 2
    return time_var