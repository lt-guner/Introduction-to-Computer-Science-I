# Author: Timur Guner
# Date: 2021-01-13
# Description: Ask the user for five input numbers to find the average

# ask user for five inputs
print("Please enter five numbers.")

# gather the five inputs in num1 through num5 and average_num = the average of the five
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())

average_num = ((num1 + num2 + num3 + num4 + num5) / 5.0)

# print the average of the five integers to the user
print("The average of those numbers is:")
print(average_num)