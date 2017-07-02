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


p_list_tmp = []
p_list = []
prime = prime_sieve(1000)
s = 0
maxsum = 100

for j in rang (1,maxsum/2)
    p_list_tmp.clear
    for i in  prime:
        s += i
        if is_prime(s):
            p_list.append(i)
            s_last = s
            print("List",p_list," Sum: ",s_last)
        else :
            break
        
    p
    
print ("The sum of consecutive primes below 1000 is: ",s_last,"\nThe list is",p_list)


elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))

