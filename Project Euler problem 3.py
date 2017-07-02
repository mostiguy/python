# -*- coding: utf-8 -*-
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""



# main program

# Find the largest factor
            
#init_number = 600851475143
init_number = 50
number = 0

if init_number % 2 == 0:
    number = init_number / 2
else:
    number = (init_number - 1)/2
    
number = int(number)
factorh = number

print (number,factorh," Number and FactorH start")
# verify range from 0 to inital number / 2
for i in range (0,number) :
    factorh = factorh-1   # from the largest factor, verify if it's a factor
    print(factorh, "1")    
    for j in range(3,number) :
        if (j*factorh) == init_number:
            print ("Factor found: ", (j*factorh))
            break   # exist the for loop
        elif (j*factorh)> init_number:
            break
        else:
            print (j, factorh, " j * factorhis not a factor")
            
    




