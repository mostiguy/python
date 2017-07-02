# -*- coding: utf-8 -*-
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits
 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

Analysis

What is the value of n in n-digit? We know it’s between 4 and 9 but that leaves
 a huge set of prime number candidates to search through. So let’s eliminate some
 values of n by using the divisibility rule that any integer is divisible by 3 whose
 sum of digits is divisible by 3; therefore composite and not prime.

9+8+7+6+5+4+3+2+1 = 45,
8+7+6+5+4+3+2+1 = 36,
6+5+4+3+2+1 = 21, and
5+4+3+2+1 = 15,
all of which are divisible by 3 and therefore could not yield a 1 to {5, 6, 8, 9}
 pandigital prime. So that leaves 4 and 7 digit prime numbers less than 4321 and 7654321
 respectively. Since we want the largest pandigital prime we’ll check the 7 digit group first.

This method is much faster and easier to code than generating all the combinations
 of pandigital numbers into a set and then just checking with the is_prime function. 
 We are, in essence, doing that implicitly by checking each candidate first, 
 but we are clearly considering some irrelevant candidates by checking only odd numbers. 
 I guess you could start with a 7 digit prime and count down using the 6k±1 to save a few iterations, 
 but it only takes 954 iterations to find the result.

"""
import time
from  math_functions import is_prime, is_pandigital

start_time = time.time()
n = 7654321
while not(is_pandigital(n, 7) and is_prime(n)):
    n -= 2

print ("The largest existing n-digit pandigital prime is", n)
  
elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))

"""
Good example of permutation

# Pandigital primes
from sympy.ntheory import isprime
from itertools import permutations


def getPermutations(num):
    snum = str(num)
    return [int(''.join(n)) for n in permutations(list(snum))]


perms = getPermutations(1234567)
perms.sort(reverse=True)

for elem in perms:
    if isprime(elem):
        print('the answer is', elem)
        break
"""