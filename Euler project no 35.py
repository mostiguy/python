# -*- coding: utf-8 -*-
"""

The number, 197, is called a circular prime because all rotations of the digits: 
    197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 
    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

Analysis:
    Only number 1,3,7,9 can be used because even num, 0 or 5 will be divisible
"""
from itertools import permutations
import time
from  math_functions import is_prime, prime_sieve
from collections import deque

start_time = time.time()
def circular (n):
    circ = []
    n = str(n)
    for i in range(len(n)):
        circ.append(int(n[1:]+n[0]))
        n = n[1:]+n[0]
    return circ

def is_prime_list (List):
    for i in List:
        if not is_prime(i):
            return False
    return True


primes = prime_sieve(1000000)
circ = []
for i in primes:
    if (is_prime_list(circular(i))):
        circ.append(i)
    
print ("Answer to PE35 = ", circ, str(len(circ)))
  
elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))

