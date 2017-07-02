# -*- coding: utf-8 -*-
"""


The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""


import time
import math

# Fibonacci function.
# n is the number of iteration

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a


def int_size(n):
    if n <= 0: return 0
    return int(math.log(n, 10) + 1)

# main program
start_time = time.time()

i = 3
found = False
while found == False : 
    a = fib(i)
    if order_size(a) == 1000 :
        found = True
    else :
        i += 1

print ("Fib index is",i,a,order_size(a))

  
elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))


