# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:30:07 2018

@author: mostiguy
"""

from  math_functions import gcd

# print(gcd(374,285))
d = 1
for i in range(1, 10):
    for j in range(1, i):
        q, r = divmod(9*j*i, 10*j-i)
        if not r and q <= 9:
            d*= i/float(j)

print ("Project Euler 33 Solution =", d)

