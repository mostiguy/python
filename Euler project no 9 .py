# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 15:58:59 2017

A Pythagorean triplet is a set of three natural numbers, a < b < c, 
for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

import time
import math

#sum = int(input("Enter the number of adjacent numbers: "))

sum = 1000
max = 500
start_time = time.time()

for a in range (3,max):
    for b in range (a+1,max):
        c_sqrt = a**2 + b**2
        c = math.sqrt(c_sqrt)
        if (c%1 == 0):
#            print ("Pythagorean triplet a,b,c:",a,b,int(c),"Triplet squared:",a**2,b**2,c_sqrt,"Sum:",int(a+b+c), "Product:",int(a*b*c))
            if (a+b+c == sum):
                print ("FOUND: Pythagorean triplet a,b,c:",a,b,int(c),"Triplet squared:",a**2,b**2,c_sqrt,"Sum:",int(a+b+c), "Product:",int(a*b*c))

        b+=1
        
    a+=1
           
            
            
            
elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))
