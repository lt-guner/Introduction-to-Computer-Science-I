# Author: Timur Guner
# Date: 2021-02-03
# Description: Project 5B creates a taxicab class to store x and y coordinates, update the location of x and y,
#              and keep track of the odometer.

class Taxicab:
    """ A class to store the taxicab x and y coordinates, update the location, and track the odometer"""

    def __init__(self, xcoord, ycoord):
        """ Creates a taxi cab object with x and y coordinates and set odometer to 0"""
        self._xcoord = int(xcoord)
        self._ycoord = int(ycoord)
        self._odom = 0

    def get_x_coord(self):
        """returns the x coordinate of cab"""
        return self._xcoord

    def get_y_coord(self):
        """returns the y coordinate of cab"""
        return self._ycoord

    def get_odometer(self):
        """returns the current odometer reading"""
        return self._odom

    def move_x(self, xcoord_change):
        """updates the current x coordinate and adds distance to the odometer"""
        self._xcoord += int(xcoord_change)
        self._odom += abs(int(xcoord_change))

    def move_y(self, ycoord_change):
        """updates the current y coordinate and adds distance to the odometer"""
        self._ycoord += int(ycoord_change)
        self._odom += abs(int(ycoord_change))
