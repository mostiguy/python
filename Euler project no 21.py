# -*- coding: utf-8 -*-
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
 each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import time
import math 


def sumPropDiv(n):
    """returns sum of proper divisors of n"""
    dSum = 0
    for x in range(1, int(n/2 + 1)):
        if n % x == 0:
            dSum += x
    return dSum

def amicSum(number):
    """finds the sum of all amicable numbers less than number, with number greater than 4."""
    answer = 0
    for x in range(4, number):
        if (sumPropDiv(x) > 4):
            if (sumPropDiv(sumPropDiv(x)) == x and sumPropDiv(x) != x):
                answer += x
                print ("These 2 numbers are amicable number pair",x,sumPropDiv(x))
    return answer

start_time = time.time()
print (amicSum(10000))
elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))