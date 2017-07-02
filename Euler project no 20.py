# -*- coding: utf-8 -*-
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""



import time
import math

start_time = time.time()

c = math.factorial(100)
s = str(c)
#print ("Number :",c,s[3],len(s))

sum = 0
for i in range (0,len(s)):
    sum += int(s[i])

print ("Number :",c,len(s),sum)

    
elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))