# Author: Timur Guner
# Date: 2021-03-03
# Description: Project 9 creates a class called AddThreeGames(). The class creates a game where two players choose
#              between 1 and 9. Each player picks one at a time until all 9 numbers are taken and its a draw or until
#              someone wins. A player wins by having 3 integers that add up to 15. The class has the init method along
#              with the get_current_state method to return whether the game is unfinished, first won, second won, or
#              draw. The second method, make_move, accepts two arguments, the player_turn and the number chose. It will
#              then update the list of chosen number for that player and removes that number as selection for the next
#              turn. If it is not that player's turn, or if the integer is not in the correct range, or if that integer
#              has already been chosen, or if the game has already been won or drawn, make_move should return False

class AddThreeGame():
    """AddThreeGame() is a class that creates a game for two players to choose numbers between 1 and 9. Each number can
       only be chosen once. Each player has a turn right after the turn of the previous player. If a player has 3
       integers that total 15, then that player has won. If all 9 numbers are picked and no one has won, then it is a
       draw."""

    def __init__(self):
        """init method sets the player turn to first, game status as unfinished, empty lists for chosen numbers for
           players one and two, and list of available numbers to chose from."""

        self._player_turn = "first"
        self._curent_state = "UNFINISHED"
        self._number_tracker_p1 = []
        self._number_tracker_p2 = []
        self._available_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def get_current_state(self):
        """Returns the status of the game; UNFISNISHED, DRAW, FIRST WON, SECOND WON"""
        return self._curent_state

    def make_move(self, player_turn, choice):
        """This method takes two arguments, the player and the number choice. If the game is unfinished, numbers can
           still be chosen, it is the correct players turn, and the chosen number is still available, then it will
           continue to move forward and record the move, otherwise it will returns False. If all four thresholds pass
           then it goes through the next steps for both player 1 and 2. The number chosen is added to the player's list
           and removed from the available numbers list. If the list of numbers chosen for that player has 3 values or
           more, then the method determines whether there are 3 integers that total 15. If so then then the game status
           it updated to WON for that player, otherwise it will be next players turn when the method is called. If all 9
           integers are chosen then the method updates the status to DRAW."""

        # check whether the game is unfinished
        if (self._curent_state == "UNFINISHED") and (self._available_numbers != []) and \
                (player_turn.lower()) == self._player_turn and (choice in self._available_numbers):

            if player_turn.lower() == "first":

                # append the value to player one's list, remove it from the available list, and set
                # the next turn to second
                self._number_tracker_p1.append(choice)
                self._available_numbers.remove(choice)
                self._player_turn = "second"

                # if player one's list is 3 or more, then the following code looks for 3 integers that
                # total 15
                if len(self._number_tracker_p1) >= 3:

                    # set the iteration slots for player one list to 0
                    x = 0
                    y = 0
                    z = 0

                    # loop to iterate through slot x in player one list
                    while x < len(self._number_tracker_p1):

                        # loop to iterate through slot y in player one list
                        while y < len(self._number_tracker_p1):

                            # loop to iterate through slot z in player one list
                            while z < len(self._number_tracker_p1):

                                # check to make sure x, y, and z are on not on the same iterate slot in the
                                # player's list
                                if (self._number_tracker_p1[x] != self._number_tracker_p1[y]) and \
                                        (self._number_tracker_p1[y] != self._number_tracker_p1[z]) and \
                                        (self._number_tracker_p1[x] != self._number_tracker_p1[z]):

                                    # if slots x, y, z in player list total 15, then set current state to
                                    # FIRST WON and return TRUE to exit the method
                                    if self._number_tracker_p1[x] + self._number_tracker_p1[y] + \
                                            self._number_tracker_p1[z] == 15:

                                        self._curent_state = "FIRST WON"
                                        return True

                                # increase iteration through z
                                z += 1

                            # increase iteration through y and reset z
                            y += 1
                            z = 0

                        # increase iteration through x and rest y and z
                        x += 1
                        y = 0
                        z = 0

                # check to see if all numbers have been chosen and set to draw if no one won
                if self._available_numbers == []:
                    self._curent_state = "DRAW"

                # once player one's turn is done computing, return true to exit method
                return True

            # if its player two's turn, then we step in, record the move, and check if the player won
            elif player_turn.lower() == "second":

                # append the value to player two's list, remove it from the available list, and set
                # the next turn to first
                self._number_tracker_p2.append(choice)
                self._available_numbers.remove(choice)
                self._player_turn = "first"

                # if player two's list is 3 or more, then the following code looks for 3 integers that
                # total 15
                if len(self._number_tracker_p2) >= 3:

                    # set the iteration slots for player two list to 0
                    x = 0
                    y = 0
                    z = 0

                    # loop to iterate through slot x in player two list
                    while x < len(self._number_tracker_p2):

                        # loop to iterate through slot y in player two list
                        while y < len(self._number_tracker_p2):

                            # loop to iterate through slot z in player two list
                            while z < len(self._number_tracker_p2):

                                # check to make sure x, y, and z are on not on the same iterate slot in the
                                # player's list
                                if (self._number_tracker_p2[x] != self._number_tracker_p2[y]) and \
                                        (self._number_tracker_p2[y] != self._number_tracker_p2[z]) and \
                                        (self._number_tracker_p2[x] != self._number_tracker_p2[z]):

                                    # if slots x, y, z in player list total 15, then set current state to
                                    # SECOND WON and return TRUE to exit the method
                                    if self._number_tracker_p2[x] + self._number_tracker_p2[y] + \
                                            self._number_tracker_p2[z] == 15:

                                        self._curent_state = "SECOND WON"
                                        return True

                                # increase iteration through z
                                z += 1

                            # increase iteration through y and reset z
                            y += 1
                            z = 0

                        # increase iteration through x and rest y and z
                        x += 1
                        y = 0
                        z = 0

                # check to see if all numbers have been chosen and set to draw if no one won
                if self._available_numbers == []:
                    self._curent_state = "DRAW"

                # once player two's turn is done computing, return true to exit method
                return True

        # return false if the game is not UNFINISHED, all numbers are chosen, if the its not the correct player, or the
        # number chosen was taken or not 1 - 9
        else:
            return False