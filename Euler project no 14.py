# -*- coding: utf-8 -*-
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""



import time
import math 

start_time = time.time()

#Calculate the triangle number
def collatz(n):
    iteration = 1
#    l = []
#    l.clear
 #   l.append(int(n))
    while (n > 1):
        if (n % 2 == 0) :
            n=n/2
        else:
            n = 3*n + 1
        iteration += 1
 #       l.append(int(n))
    return iteration

h_chain = 0
max = 1000000
k = 1
h_k = 1
while (k < max):
    chain = collatz(k)
#    print (k,chain)
    if chain > h_chain:
        h_chain = chain
        h_k = k
    k += 1

print("The number of term below {:d} is {:d} for number {:d}".format(max,h_chain,h_k))

elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))