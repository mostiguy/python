# -*- coding: utf-8 -*-
"""
A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are 
listed numerically or alphabetically, we call it lexicographic order. The lexicographic 
permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


"""
from itertools import permutations
import time
import math

start_time = time.time()

d = [0,1,2,3,4,5,6,7,8,9]
index = 1
for p in permutations(d):
    if index == 1000000 :
        print (index, p)
        s = map(str,p)
        print (''.join(s))
    index += 1
  
elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))


