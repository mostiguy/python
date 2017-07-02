# -*- coding: utf-8 -*-
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

  
"""
import time

from math_functions import sof_digits

start_time = time.time()

s = sum(n for n in range(10, 1500000) if n == sof_digits(n))
print ("Project Euler 34 Solution =", s)
 
elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))

