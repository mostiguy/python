# -*- coding: utf-8 -*-
"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
  
"""
import time
max = 1000
sum = 0

start_time = time.time()

d = 10**10

for n in range(1, max+1):
    sum += (n**n) 

print ("Project Euler 48 Solution = ", (sum % d))

#for a in range(1, max):
#    sum += math.pow(a,a)
  
#print ("The sum of the series is", sum)

elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))

