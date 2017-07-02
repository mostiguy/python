# -*- coding: utf-8 -*-
"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000



Analysis:

d1 = 1
d10 = 1
    
"""
import time


start_time = time.time()
d_list = ""
d_prod = 1
for i in range (1,1000000) :
    d_list += str(i)

print ("String length = ",len(d_list))

for i in range (1,8):
    d_prod *= int(d_list[(1*(10**(i-1))-1)])
    print ("d",(1*(10**(i-1)))," Value=",d_list[(1*(10**(i-1))-1)])

print ("list",d_list[0],d_list[9],d_list[99],d_list[999],d_list[9999],d_list[99999],d_list[999999]," Product = ",d_prod)
  
elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))

