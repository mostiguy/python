# -*- coding: utf-8 -*-
"""
Euler project #1

If we list all the natural numbers below 10 that are multiples 
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
# 
belownumber = 1000
summation = 0  # Init the summation to 0

for i in range(2, belownumber):
    if (i % 3) == 0:
        summation = summation + i
        print(summation,"3")
    if (i % 5) == 0:
        summation = summation + i
        print(summation, "5")
        
#need to remove when multiple of 3&5
    if ((i % 3) == 0) and ((i % 5) == 0):
       summation = summation - i
       print(summation, "3&5")


print(i,"times", summation, "summation")
  