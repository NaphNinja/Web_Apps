#!/usr/bin/env python3

import os
import itertools

print("\n")

print (" - - - Welcome to the Range Inspector - - - ")

print("\n")

xnum1 = int(input("Enter the initial element of the origin range: "))
znum1 = int(input("Enter the end element of the origin range: "))
range_1 = list(range(xnum1, znum1))

xnum2 = int(input("Enter the initial element of the modifier range: "))
znum2 = int(input("Enter the end element of the modifier range: "))
range_2 = list(range(xnum2, znum2))

xnum3 = int(input("Enter the initial element of the deleter range: "))
znum3 = int(input("Enter the end element of the deleter range: "))
range_3 = list(range(xnum3, znum3))

add_range = list(set(range_1).union(range_2))

delete_list = [i for j, i in enumerate(add_range) if j not in range_3]

# Driver Code
print("\n")

print ("The origin range is:", range_1)

print("\n")

print ("The modifier range is:", range_2)

print("\n")

print ("The deleter range is:", range_3)

print("\n")

print ("The combined range after processing: " + str(add_range))

print("\n")

print ("The truncated range is:", delete_list)
