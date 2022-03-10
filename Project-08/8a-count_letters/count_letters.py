# Author: Timur Guner
# Date: 2021-02-24
# Description: Project 8a creates a function that takes in a string, counts each letter of the alphabet,
# and puts the count of each letter in a dictionary

def count_letters(input_string):
    """This function takes in a string, counts each letter of the alphabet, and puts the count of each letter
       in a dictionary"""

    # create an empty dictionary to create or alphabet dictionary later and set the input string to upper case
    count_dictionary = {}
    input_string = input_string.upper()

    # set each letter count to 0
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_e = 0
    count_f = 0
    count_g = 0
    count_h = 0
    count_i = 0
    count_j = 0
    count_k = 0
    count_l = 0
    count_m = 0
    count_n = 0
    count_o = 0
    count_p = 0
    count_q = 0
    count_r = 0
    count_s = 0
    count_t = 0
    count_u = 0
    count_v = 0
    count_w = 0
    count_x = 0
    count_y = 0
    count_z = 0

    # a for loop is used iterate through each element in the string
    for letter in input_string:

        # a nested if / elif statement is used to create or add to the total of each letter in the count_dictionary
        # if the input string does not contain the letter in the if / elif, then it will never be created in the dictionary
        if letter == "A":
            count_a += 1
            count_dictionary["A"] = count_a
        elif letter == "B":
            count_b += 1
            count_dictionary["B"] = count_b
        elif letter == "C":
            count_c += 1
            count_dictionary["C"] = count_c
        elif letter == "D":
            count_d += 1
            count_dictionary["D"] = count_d
        elif letter == "E":
            count_e += 1
            count_dictionary["E"] = count_e
        elif letter == "F":
            count_f += 1
            count_dictionary["F"] = count_f
        elif letter == "G":
            count_g += 1
            count_dictionary["G"] = count_g
        elif letter == "H":
            count_h += 1
            count_dictionary["H"] = count_h
        elif letter == "I":
            count_i += 1
            count_dictionary["I"] = count_i
        elif letter == "J":
            count_j += 1
            count_dictionary["J"] = count_j
        elif letter == "K":
            count_k += 1
            count_dictionary["K"] = count_k
        elif letter == "L":
            count_l += 1
            count_dictionary["L"] = count_l
        elif letter == "M":
            count_m += 1
            count_dictionary["M"] = count_m
        elif letter == "N":
            count_n += 1
            count_dictionary["N"] = count_n
        elif letter == "O":
            count_o += 1
            count_dictionary["O"] = count_o
        elif letter == "P":
            count_p += 1
            count_dictionary["P"] = count_p
        elif letter == "Q":
            count_q += 1
            count_dictionary["Q"] = count_q
        elif letter == "R":
            count_r += 1
            count_dictionary["R"] = count_r
        elif letter == "S":
            count_s += 1
            count_dictionary["S"] = count_s
        elif letter == "T":
            count_t += 1
            count_dictionary["T"] = count_t
        elif letter == "U":
            count_u += 1
            count_dictionary["U"] = count_u
        elif letter == "V":
            count_v += 1
            count_dictionary["V"] = count_v
        elif letter == "W":
            count_w += 1
            count_dictionary["W"] = count_w
        elif letter == "X":
            count_x += 1
            count_dictionary["X"] = count_x
        elif letter == "Y":
            count_y += 1
            count_dictionary["Y"] = count_y
        elif letter == "Z":
            count_z += 1
            count_dictionary["Z"] = count_z

    # return the dictionary
    return count_dictionary