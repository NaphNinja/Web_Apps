#!/usr/bin/env python3

# This program is a range inspector that implements the 'DELETE' function to delete user input range
# Enter the values for the origin range
# Delete a portion (or all) of that origin range by entering values in the deleter range
# The results will be shown after all the inputs have been entered

# This was created as part of a challenge question for Kepler Communications
# Author: Naphish Lashba Raj
# Github handle: https://github.com/NaphNinja

import os
import itertools # Iteration tools library to implement functionality such as FilterFalse and Chain()

print("\n") # Used line spaces for aesthetic reasons througout the program

print (" - - - Welcome to the Range Inspector - - - ")

print("\n")

# This defines the user input values in the form of integers for the start and end elements of the origin range
xnum1 = int(input("Enter the initial element of the origin range: "))
znum1 = int(input("Enter the end element of the origin range: "))

# Representation of range in list format based on the input values above
range_1 = list(range(xnum1, znum1))

print("\n")

# Represents the user input values of the deleter range to remove elements from the origin range
xnum3 = int(input("Enter the initial element of the deleter range: "))
znum3 = int(input("Enter the end element of the deleter range: "))

# Representation of the deleter range in list format
range_3 = list(range(xnum3, znum3))

# List comprehension function + Enumerate function to create a new list by removing the elements from range_3 present in range_1
# The above method was used instead of a 'for' loop due to it being computationaly more efficient and to reduce complexity.
delete_range = [i for j, i in enumerate(range_1) if j not in range_3]


# -- RESULTS --

print("\n")

# Represents the origin range based on user input
print ("The origin range is:", range_1)

print("\n")

# Represents the deleter range based on user input
print ("The deleter range is:", range_3)

print("\n")

# Prints the a new list by removing the elements common to both range_1 and range_3
print ("The truncated range is:", delete_range)
