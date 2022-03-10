# Author: Timur Guner
# Date: 2021-03-10
# Description: Project 10 creates a class called FourLetterBoard(). There are two players x and y. Each player can place
#              a letter (A-D) in blank spot as long as the other player hasn't played that letter the same row, column,
#              or quadrant. A player can place the same letter in a row, column, or quadrant, as long as they previously
#              placed that letter. If the player places the final letter, to complete the combo of A-D, in a row,
#              column, or quadrant then the game is over and that player won. If all spaces are full and no one has won,
#              then the game ends in a draw


class FourLetterBoard():
    """This class creates a 4x4 board for players x and y. Each player can place letters A - D on a blank space, as long
       as the letter was not previously played by the other player in the same row, column, or quadrant. A player can
       place the same letter in a row, column, or quadrant as long as they were the player that previously played it. If
       a player completes A-D in a row, column, or quadrant, then that player has won the game. If all 16 spaces are
       filled with no winner, then the game ends in a draw."""

    def __init__(self):
        """init establishes a blank list of lists to represent the board and sets current state to UNFINISHED"""
        self._board = [['', '', '', ''],['', '', '', ''],['', '', '', ''],['', '', '', '']]
        self._current_state = "UNFINISHED"

    def get_current_state(self):
        """get_current_state returns the current state of the game"""
        return self._current_state

    def make_move(self, row, column, letter, player):
        """make_move keeps track of all the moves that were made. During each move, it checks if the space is blank,
        the game is UNFINISHED, and if the letter was not played by other player in the same row, column, or quadrant,
        otherwise it returns false. It does allow the player to place the same letter in a row, column, or quadrant, if
        that player already made the move"""

        # variables used later on in code for varies checking
        quadrant = 0
        a_letter = ''
        b_letter = ''
        c_letter = ''
        d_letter = ''
        space_counter = 0

        # set the quadrant of the move
        # [0][0]-[1][1] quadrant 1, [0][2]-[1][3] quadrant 2, [2][0]-[3][1] quadrant 3, [2][2]-[3][3] quadrant 4
        if row < 2 and column < 2:
            quadrant = 1
        elif row < 2 and column > 1:
            quadrant = 2
        elif row > 1 and column < 2:
            quadrant = 3
        else:
            quadrant = 4

        # check to see if game is still valid
        if self._current_state == "UNFINISHED":

            # check to see if the space i blank
            if self._board[row][column] == '':

                # if player o, then go through the following steps
                if player.lower() == "o":

                    # check to make sure the letter was not played by x in the chosen column and if so return false
                    if self._board[row][0] == letter + ',x' or self._board[row][1] == letter + ',x' or \
                            self._board[row][2] == letter + ',x' or self._board[row][3] == letter + ',x' + player:
                        return False

                    # check to make sure the letter was not played by x in the chosen column and if so return false
                    elif self._board[0][column] == letter + ',x' or self._board[1][column] == letter + ',x' or \
                            self._board[2][column] == letter + ',x' or self._board[3][column] == letter + ',x':
                        return False

                    # check if the move was played in quadrant 1
                    # if so, check to see x played the letter and return False if it was
                    elif quadrant == 1:
                        if self._board[0][0] == letter + ',x' or self._board[0][1] == letter + ',x' or \
                                self._board[1][0] == letter + ',x' or self._board[1][1] == letter + ',x':
                            return False

                    # check if the move was played in quadrant 2
                    # if so, check to see x played the letter and return False if it was
                    elif quadrant == 2:
                        if self._board[0][2] == letter + ',x' or self._board[0][3] == letter + ',x' or \
                                self._board[1][2] == letter + ',x' or self._board[1][3] == letter + ',x':
                            return False

                    # check if the move was played in quadrant 3
                    # if so, check to see x played the letter and return False if it was
                    elif quadrant == 3:
                        if self._board[2][0] == letter + ',x' or self._board[2][1] == letter + ',x' or \
                                self._board[3][0] == letter + ',x' or self._board[3][1] == letter + ',x':
                            return False

                    # check if the move was played in quadrant 4
                    # if so, check to see x played the letter and return False if it was
                    elif quadrant == 4:
                        if self._board[2][2] == letter + ',x' or self._board[2][3] == letter + ',x' or \
                                self._board[3][2] == letter + ',x' or self._board[3][3] == letter + ',x':
                            return False

                    # make move if all the above checks pass
                    self._board[row][column] = letter + ',' + player

                    # use a for loop to check if all 4 letter were played in the row
                    for i in range(0,4):
                        if 'A' in self._board[row][i]:
                            a_letter = 'A'
                        elif 'B' in self._board[row][i]:
                            b_letter = 'B'
                        elif 'C' in self._board[row][i]:
                            c_letter = 'C'
                        elif 'D' in self._board[row][i]:
                            d_letter = 'D'

                    # if all four letters in the row are played then that means this turn was won by O / return True
                    # if not set reset letter tracking variables to ''
                    if a_letter == 'A' and b_letter == 'B' and c_letter == 'C' and d_letter == 'D':
                        self._current_state = "O_WON"
                        return True
                    else:
                        a_letter = ''
                        b_letter = ''
                        c_letter = ''
                        d_letter = ''

                    # use a for loop to check if all 4 letter were played in the column
                    for i in range(0,4):
                        if 'A' in self._board[i][column]:
                            a_letter = 'A'
                        elif 'B' in self._board[i][column]:
                            b_letter = 'B'
                        elif 'C' in self._board[i][column]:
                            c_letter = 'C'
                        elif 'D' in self._board[i][column]:
                            d_letter = 'D'

                    # if all four letters in the column are played then that means this turn was won by O / return True
                    # if not set reset letter tracking variables to ''
                    if a_letter == 'A' and b_letter == 'B' and c_letter == 'C' and d_letter == 'D':
                        self._current_state = "O_WON"
                        return True
                    else:
                        a_letter = ''
                        b_letter = ''
                        c_letter = ''
                        d_letter = ''

                    # begin checking if quadrant one was won with an if statement
                    if quadrant == 1:

                        # use a nested for loop determine if all four letters were played in quadrant 1
                        for i in range(0,2):
                            for x in range(0,2):
                                if 'A' in self._board[i][x]:
                                    a_letter = 'A'
                                elif 'B' in self._board[i][x]:
                                    b_letter = 'B'
                                elif 'C' in self._board[i][x]:
                                    c_letter = 'C'
                                elif 'D' in self._board[i][x]:
                                    d_letter = 'D'

                        # if all four letters were played, then this was won by player O and return True
                        # if not then, reset the letter tracking variables to ''
                        if a_letter == 'A' and b_letter == 'B' and c_letter == 'C' and d_letter == 'D':
                            self._current_state = "O_WON"
                            return True
                        else:
                            a_letter = ''
                            b_letter = ''
                            c_letter = ''
                            d_letter = ''

                    # begin checking if quadrant two was won with an if statement
                    if quadrant == 2:

                        # use a nested for loop determine if all four letters were played in quadrant 2
                        for i in range(0, 2):
                            for x in range(2, 4):
                                if 'A' in self._board[i][x]:
                                    a_letter = 'A'
                                elif 'B' in self._board[i][x]:
                                    b_letter = 'B'
                                elif 'C' in self._board[i][x]:
                                    c_letter = 'C'
                                elif 'D' in self._board[i][x]:
                                    d_letter = 'D'

                        # if all four letters were played, then this was won by player O and return True
                        # if not then, reset the letter tracking variables to ''
                        if a_letter == 'A' and b_letter == 'B' and c_letter == 'C' and d_letter == 'D':
                            self._current_state = "O_WON"
                            return True
                        else:
                            a_letter = ''
                            b_letter = ''
                            c_letter = ''
                            d_letter = ''

                    # begin checking if quadrant three was won with an if statement
                    if quadrant == 3:

                        # use a nested for loop determine if all four letters were played in quadrant 3
                        for i in range(2, 4):
                            for x in range(0, 2):
                                if 'A' in self._board[i][x]:
                                    a_letter = 'A'
                                elif 'B' in self._board[i][x]:
                                    b_letter = 'B'
                                elif 'C' in self._board[i][x]:
                                    c_letter = 'C'
                                elif 'D' in self._board[i][x]:
                                    d_letter = 'D'

                        # if all four letters were played, then this was won by player O and return True
                        # if not then, reset the letter tracking variables to ''
                        if a_letter == 'A' and b_letter == 'B' and c_letter == 'C' and d_letter == 'D':
                            self._current_state = "O_WON"
                            return True
                        else:
                            a_letter = ''
                            b_letter = ''
                            c_letter = ''
                            d_letter = ''

                    # begin checking if quadrant four was won with an if statement
                    if quadrant == 4:

                        # use a nested for loop determine if all four letters were played in quadrant 4
                        for i in range(2, 4):
                            for x in range(2, 4):
                                if 'A' in self._board[i][x]:
                                    a_letter = 'A'
                                elif 'B' in self._board[i][x]:
                                    b_letter = 'B'
                                elif 'C' in self._board[i][x]:
                                    c_letter = 'C'
                                elif 'D' in self._board[i][x]:
                                    d_letter = 'D'

                        # if all four letters were played, then this was won by player O and return True
                        # if not then, reset the letter tracking variables to ''
                        if a_letter == 'A' and b_letter == 'B' and c_letter == 'C' and d_letter == 'D':
                            self._current_state = "O_WON"
                            return True
                        else:
                            a_letter = ''
                            b_letter = ''
                            c_letter = ''
                            d_letter = ''

                # if player o, then go through the following steps
                if player.lower() == "x":

                    # check to make sure the letter was not played by x in the chosen column and if so return false
                    if self._board[row][0] == letter + ',o' or self._board[row][1] == letter + ',o' or \
                            self._board[row][2] == letter + ',o' or self._board[row][3] == letter + ',o' + player:
                        return False

                    # check to make sure the letter was not played by x in the chosen column and if so return false
                    elif self._board[0][column] == letter + ',o' or self._board[1][column] == letter + ',o' or \
                            self._board[2][column] == letter + ',o' or self._board[3][column] == letter + ',o':
                        return False

                    # check if the move was played in quadrant 1
                    # if so, check to see x played the letter and return False if it was
                    elif quadrant == 1:
                        if self._board[0][0] == letter + ',o' or self._board[0][1] == letter + ',o' or \
                                self._board[1][0] == letter + ',o' or self._board[1][1] == letter + ',o':
                            return False

                    # check if the move was played in quadrant 2
                    # if so, check to see x played the letter and return False if it was
                    elif quadrant == 2:
                        if self._board[0][2] == letter + ',o' or self._board[0][3] == letter + ',o' or \
                                self._board[1][2] == letter + ',o' or self._board[1][3] == letter + ',o':
                            return False

                    # check if the move was played in quadrant 3
                    # if so, check to see x played the letter and return False if it was
                    elif quadrant == 3:
                        if self._board[2][0] == letter + ',o' or self._board[2][1] == letter + ',o' or \
                                self._board[3][0] == letter + ',o' or self._board[3][1] == letter + ',o':
                            return False

                    # check if the move was played in quadrant 4
                    # if so, check to see x played the letter and return False if it was
                    elif quadrant == 4:
                        if self._board[2][2] == letter + ',o' or self._board[2][3] == letter + ',o' or \
                                self._board[3][2] == letter + ',o' or self._board[3][3] == letter + ',o':
                            return False

                    # make move if all the above checks pass
                    self._board[row][column] = letter + ',' + player

                    # use a for loop to check if all 4 letter were played in the row
                    for i in range(0, 4):
                        if 'A' in self._board[row][i]:
                            a_letter = 'A'
                        elif 'B' in self._board[row][i]:
                            b_letter = 'B'
                        elif 'C' in self._board[row][i]:
                            c_letter = 'C'
                        elif 'D' in self._board[row][i]:
                            d_letter = 'D'

                    # if all four letters in the row are played then that means this turn was won by O / return True
                    # if not set reset letter tracking variables to ''
                    if a_letter == 'A' and b_letter == 'B' and c_letter == 'C' and d_letter == 'D':
                        self._current_state = "X_WON"
                        return True
                    else:
                        a_letter = ''
                        b_letter = ''
                        c_letter = ''
                        d_letter = ''

                    # use a for loop to check if all 4 letter were played in the column
                    for i in range(0, 4):
                        if 'A' in self._board[i][column]:
                            a_letter = 'A'
                        elif 'B' in self._board[i][column]:
                            b_letter = 'B'
                        elif 'C' in self._board[i][column]:
                            c_letter = 'C'
                        elif 'D' in self._board[i][column]:
                            d_letter = 'D'

                    # if all four letters in the column are played then that means this turn was won by O / return True
                    # if not set reset letter tracking variables to ''
                    if a_letter == 'A' and b_letter == 'B' and c_letter == 'C' and d_letter == 'D':
                        self._current_state = "X_WON"
                        return True
                    else:
                        a_letter = ''
                        b_letter = ''
                        c_letter = ''
                        d_letter = ''

                    # begin checking if quadrant one was won with an if statement
                    if quadrant == 1:

                        # use a nested for loop determine if all four letters were played in quadrant 1
                        for i in range(0, 2):
                            for x in range(0, 2):
                                if 'A' in self._board[i][x]:
                                    a_letter = 'A'
                                elif 'B' in self._board[i][x]:
                                    b_letter = 'B'
                                elif 'C' in self._board[i][x]:
                                    c_letter = 'C'
                                elif 'D' in self._board[i][x]:
                                    d_letter = 'D'

                        # if all four letters were played, then this was won by player O and return True
                        # if not then, reset the letter tracking variables to ''
                        if a_letter == 'A' and b_letter == 'B' and c_letter == 'C' and d_letter == 'D':
                            self._current_state = "X_WON"
                            return True
                        else:
                            a_letter = ''
                            b_letter = ''
                            c_letter = ''
                            d_letter = ''

                    # begin checking if quadrant two was won with an if statement
                    if quadrant == 2:

                        # use a nested for loop determine if all four letters were played in quadrant 2
                        for i in range(0, 2):
                            for x in range(2, 4):
                                if 'A' in self._board[i][x]:
                                    a_letter = 'A'
                                elif 'B' in self._board[i][x]:
                                    b_letter = 'B'
                                elif 'C' in self._board[i][x]:
                                    c_letter = 'C'
                                elif 'D' in self._board[i][x]:
                                    d_letter = 'D'

                        # if all four letters were played, then this was won by player O and return True
                        # if not then, reset the letter tracking variables to ''
                        if a_letter == 'A' and b_letter == 'B' and c_letter == 'C' and d_letter == 'D':
                            self._current_state = "X_WON"
                            return True
                        else:
                            a_letter = ''
                            b_letter = ''
                            c_letter = ''
                            d_letter = ''

                    # begin checking if quadrant three was won with an if statement
                    if quadrant == 3:

                        # use a nested for loop determine if all four letters were played in quadrant 3
                        for i in range(2, 4):
                            for x in range(0, 2):
                                if 'A' in self._board[i][x]:
                                    a_letter = 'A'
                                elif 'B' in self._board[i][x]:
                                    b_letter = 'B'
                                elif 'C' in self._board[i][x]:
                                    c_letter = 'C'
                                elif 'D' in self._board[i][x]:
                                    d_letter = 'D'

                        # if all four letters were played, then this was won by player O and return True
                        # if not then, reset the letter tracking variables to ''
                        if a_letter == 'A' and b_letter == 'B' and c_letter == 'C' and d_letter == 'D':
                            self._current_state = "X_WON"
                            return True
                        else:
                            a_letter = ''
                            b_letter = ''
                            c_letter = ''
                            d_letter = ''

                    # begin checking if quadrant four was won with an if statement
                    if quadrant == 4:

                        # use a nested for loop determine if all four letters were played in quadrant 4
                        for i in range(2, 4):
                            for x in range(2, 4):
                                if 'A' in self._board[i][x]:
                                    a_letter = 'A'
                                elif 'B' in self._board[i][x]:
                                    b_letter = 'B'
                                elif 'C' in self._board[i][x]:
                                    c_letter = 'C'
                                elif 'D' in self._board[i][x]:
                                    d_letter = 'D'

                        # if all four letters were played, then this was won by player O and return True
                        # if not then, reset the letter tracking variables to ''
                        if a_letter == 'A' and b_letter == 'B' and c_letter == 'C' and d_letter == 'D':
                            self._current_state = "X_WON"
                            return True
                        else:
                            a_letter = ''
                            b_letter = ''
                            c_letter = ''
                            d_letter = ''

                # use a double for loop to check if all spaces are filled
                for i in range(0, 4):
                    for x in range(0, 4):
                        if self._board[i][x] != '':
                            space_counter += 1

                # set current state to draw if all 16 spaces are filled and return true
                if space_counter == 16:
                    self._current_state = "DRAW"
                    return True

                # return ture if moves were placed and status check and or update, else return false
                return True

            else:
                return False

        # return false if game is finished
        else:
            return False
