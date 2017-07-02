# -*- coding: utf-8 -*-
"""

"""

import time

def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]


def f(L):
  if L < 8: return 3
  for d in prime_sieve(L)[::-1]:
    period = 1
    while pow(10, period, d) != 1: period += 1
    if d-1 == period: break
  return d
  
start_time = time.time()

L = int(input('The longest recurring cycle for 1/d where d <'))
print ("is", f(L))

elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))
