# -*- coding: utf-8 -*-
"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime 
factors each. What is the first of these numbers?
"""

import time
import math
from collections import Counter
import sympy

     
def get_factors(n):
    """Factor number n"""
    f = sympy.factorint(n)
    return f
         
def main():
    """Main Program"""
    start_time = time.time()
    counter = 0
    for n in range(1000, 1000000):
        if counter == 4:
            print ("Answer=", n - 4)
            break
        else:
            x = get_factors(n)
            if len(x) == 4:
                counter += 1
            else:
                counter = 0
    
    elapsed_time = time.time() - start_time
    print ("Elapse time: {:.2f} sec".format(elapsed_time))

if __name__ == '__main__':
    main()
