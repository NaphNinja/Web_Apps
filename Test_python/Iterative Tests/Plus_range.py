#!/usr/bin/env python3

import os
import itertools

print ("We're now combining the two ranges")

xnum1 = int(input("Enter the first element of range 1: "))
znum1 = int(input("Enter the last element of range 1: "))
range_1 = list(range(xnum1, znum1+1))

xnum2 = int(input("Enter the first element of range 2: "))
znum2 = int(input("Enter the last element of range 2: "))
range_2 = list(range(xnum2, znum2+1))

add_range = list(itertools.chain(range_1, range_2))

print ("The combine range after processing: " + str(add_range))
