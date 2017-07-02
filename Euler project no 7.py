# -*- coding: utf-8 -*-
"""
Euler project #7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import time

# pos is the nth prime number
#pos = 6

pos = int(input("Enter the nth prime: "))

def eprimo(num):
    if num < 2:
        return False
    if num == 2:
        return True
    else:
        for div in range(2,num):
            if num % div == 0:
                return False
        return True

start_time = time.time()
i = 1
nth = 1

# loop until the nth prime is found
while nth <= pos:
    if eprimo(i) == True :
        if nth == pos :
            print ("Number: ",i," is the nth : ", nth)
        nth += 1
    
    i = i +1
      

elapsed_time = time.time() - start_time
print ("Elapse time:",elapsed_time, " sec")
