# -*- coding: utf-8 -*-
"""

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""


import time
import math

# Fibonacci function.
# n is the number of iteration

def g(n):
    s = (n-1) // 2
    return (16*s*s*s + 30*s*s + 26*s + 3) // 3
 

# main program

n = int(input('Enter an odd side length ≥ 3?'))

start_time = time.time()

print ("Sum of both diagonals for a square spiral with length", n) 
print ("=", g(n))

  
elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))


