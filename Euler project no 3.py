# -*- coding: utf-8 -*-
"""
Euler project #4

 palindromic number reads the same both ways. 
 The largest palindrome made from the product of 
 two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
# 


def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac



    
print ("Prime n:", primes(6008514751435443378633313))
print ("End")