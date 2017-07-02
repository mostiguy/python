# -*- coding: utf-8 -*-
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases 
by 3330, is unusual in two ways: (i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
Analysis:



    
"""
import time
from itertools import permutations
from math_functions import is_prime, is_perm

start_time = time.time()

n, f = 1487, 1 	# start search with prime from description
while True:
    n += 3-f    # generates prime candidates faster than checking odd numbers
    f = -f
    b, c = n+3330, n+6660
    if is_prime(n) and is_prime(b) and is_prime(c) \
        and is_perm(n,b) and is_perm(b,c): break

print ("Project Euler 49 Solution =", str(n)+str(b)+str(c), n, b, c)
            
 
elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))

