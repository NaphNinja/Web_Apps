#!/usr/bin/env python3

# This program is a range inspector that implements the 'ADD' function to add a range from the user input
# Enter the values for the origin range
# Add a range in the modifier which will create a union between the origin and the modifier by including overlaps
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

# User input values for the modifier range that will function on the origin range
xnum2 = int(input("Enter the initial element of the modifier range: "))
znum2 = int(input("Enter the end element of the modifier range: "))

# Representation of range in list format based on the input values above
range_2 = list(range(xnum2, znum2))

# Python Standard Library function to implement Set union between the two user input ranges
add_range = list(set(range_1).union(range_2))


# -- RESULTS --

print("\n")

# Represents the origin range based on user inputs
print ("The origin range is:", range_1)

print("\n")

# Represents the modifier range based on user inputs
print ("The modifier range is:", range_2)

print("\n")

# Returns the combined range including overlaps between the old and new ranges
print ("The combined range after processing: " + str(add_range))
