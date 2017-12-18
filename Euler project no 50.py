# -*- coding: utf-8 -*-
"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive 
primes?
  
"""
import time
from math_functions import prime_sieve
from math_functions import is_prime

start_time = time.time()

target = 1000000
prime = prime_sieve(int(target/2))
l_prime = len(prime)
max_psum = 0
max_consecutive = 0
max_prime = 0
p_list = []

start = 0
# Build a list of prime sums and the number of consecutive prime
for start in range(0,int(l_prime/2)):
    p_sum = 0
    p_list.clear()
    for a in range(start,int(l_prime)):
        p_sum += prime[a]
        p_list.append(p_sum)
        c = a+1-start
        p_list.append(c)
        if (is_prime(p_sum) and (p_sum < target)):
            if (c > max_consecutive):
                    max_consecutive = c
                    max_psum = p_sum

        if p_sum > target:
            break
    
#print("Prime sum list and consecutive prime",p_list) 
print("Prime sum and consecutive prime",max_psum,max_consecutive)


elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))

