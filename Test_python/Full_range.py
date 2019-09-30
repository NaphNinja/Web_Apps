#!/usr/bin/env python3

# This program is a combined range inspector which includes all three methods included.
# Enter the elements for the origin and modifier range based on prompts to form the combined range
# Enter the elements for the deleter range and querey range to delete and find particular ranges from the combined range above
# This program will print all the results according once all inputs are defined.

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

# Defines the user input values for the modifier range
xnum2 = int(input("Enter the initial element of the modifier range: "))
znum2 = int(input("Enter the end element of the modifier range: "))

# Representation of range in list format based on the input values above
range_2 = list(range(xnum2, znum2))

# Defines the user input values for the range that will be deleted from the combined range
xnum3 = int(input("Enter the initial element of the range you wish to delete: "))
znum3 = int(input("Enter the end element of the range you wish to delete: "))

# Representation of range in list format based on the input values above
range_3 = list(range(xnum3, znum3))

# Defines the user input values for the range that will be quereyed from the combined range
xnum4 = int(input("Enter the initial element of the range you wish to find: "))
znum4 = int(input("Enter the end element of the range you wish to find: "))

# Representation of range in list format based on the input values above
range_4 = list(range(xnum4, znum4))

# Similar to the first method, this uses a set union function for a union of elements between range_1 and range_2
add_range = list(set(range_1).union(range_2))

# List comprehension function + Enumerate function to create a new list by removing the elements from range_3 present in range_1
# The above method was used instead of a 'for' loop due to it being computationaly more efficient and to reduce complexity.
delete_list = [i for j, i in enumerate(add_range) if j not in range_3]

# This uses the Python standar library set intersection function to determine the intersection between the combined add_range and Querey range_4
find_range = list(set(add_range).intersection(range_4))

# -- RESULTS --

print("\n")

# Represents the origin range based on user input
print ("The origin range is:", range_1)

print("\n")

# Represents the modifier range based on user input
print ("The modifier range is:", range_2)

print("\n")

# Represent the combined range formed by the union of the origin range and the modifier range
print ("The combined range after processing: " + str(add_range))

print("\n")

# Represents the range that will be deleted from the combined range
print ("The deleter range is:", range_3)

print("\n")

# Prints the a new list by removing the elements common to both add_range andn range_3
print ("The truncated range is:", delete_list)

print("\n")

# Represents the range that results from quereying the combined range with the user input range_4
print ("The ranges that intersect after processing: " + str(find_range))
