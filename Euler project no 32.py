# -*- coding: utf-8 -*-
"""
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.


Analysis:
This is a perfect application for a simple brute force program that iterates through the possibilities and produces a solution.

The only thought of optimization was to generate as many 4 digit products as necessary in order to keep the concatenation of the factors and product at the required 9 digits.

The only possible combinations that accomplish this are a 1 digit number times a 4 digit number (like 1 x 2345 = 2345 and concatenates to 123452345; a nine digit number), or a 2 digit number times a 3 digit number (like 12 x 345 = 4140 and concatenates to 123454140; a nine digit number).

You must keep the factors form exceeding 4 digit products such as 56 x 789 = 44184 and that’s where the 10000//i comes in. The double slash (//) specifies integer (or floor) division.

A set is used to ignore duplicate products.
    
"""
import time
from  math_functions import is_pandigital

start_time = time.time()
p = set()
for i in range(2,  60):
    start = 1234 if i < 10 else 123 
    for j in range(start, 10000//i):
        if is_pandigital(str(i) + str(j) + str(i*j)): 
            p.add(i*j)
            print(i," x",j," = ",i*j)

print ("Sum of products =", sum(p))
  
elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))

