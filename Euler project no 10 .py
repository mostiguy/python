# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 10:31:33 2017

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time
import math

def eprime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    else:
        max = int(math.sqrt(num))
        for div in range(2,max+1):
            if num % div == 0:
                return False
        return True
p_max = int(input("Enter the number prime numbers to calculate the sum ?"))

sum = 0
start_time = time.time()

for i in range (1,p_max):
    if (eprime(i)):
        sum += i
#        print (i,sum)
    i += 2
        
print ("The sum is:",sum)        
            
elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))
