# -*- coding: utf-8 -*-
"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""



import time
import math 

start_time = time.time()

c = 2**1000
s = str(c)
#print ("Number :",c,s[3],len(s))

sum = 0
for i in range (0,len(s)):
    sum += int(s[i])
#    print (s[i])

print ("Number :",c,s[3],len(s),sum)

    
elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))