#!/usr/bin/env python3

# This program is a range inspector that implements the 'GET' function to querey and fetch a user input range
# Enter the values for the origin range and modifier range to get a combined range
# Querey that combined range by entering values for the Querey rangeself.
# The results will be shown after each prompt

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

# Represents the origin range based on input
print ("The origin range is:", range_1)


print("\n")

# This defines the user input values for the modifier range
xnum2 = int(input("Enter the initial element of the second range: "))
znum2 = int(input("Enter the end element of the second range: "))

# Representation of range in list format based on the input values above
range_2 = list(range(xnum2, znum2))

print("\n")

# Represents the modifier range based on input
print ("The modifier range is:", range_2)


print("\n")

# Similar to the first method, this uses a set union function for a union of elements between range_1 and range_2
add_range = list(set().union(range_1, range_2))

# Represent the combined range formed by the union of the origin range and the modifier range
print ("The combined range after processing: " + str(add_range))

print("\n")

# This defines the user input values that will 'GET'the range that we want to find within the combined range
xnum3 = int(input("Enter the initial element of the range you wish to find: "))
znum3 = int(input("Enter the end element of the range you wish to find: "))

# Representation of the Querey range in list format
range_3 = list(range(xnum3, znum3))

print("\n")

# This uses the Python standar library set intersection function to determine the intersection between the combined add_range and Querey range_3
find_range = list(set(add_range).intersection(range_3))

# Represents the range that results from quereying the combined range with the user input range_3
print ("The ranges that intersect after processing: " + str(find_range))
