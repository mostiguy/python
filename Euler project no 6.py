# -*- coding: utf-8 -*-
"""
Problem 6
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
 numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
"""

def sum_squares (n):
    i = 0
    sum = 0
    for i in range (1,n+1):
        sum = sum + i**2
        i += 1
#        print (i,sum, "sum in for")
        
    return sum
    
def square_sum (m):
    j = 0
    ssum = 0
    for j in range (1,m+1):
        ssum = ssum + j
        j += 1
#        print (j,ssum, "square sum")

    return (ssum**2)
        
        
s_square = 100
a = sum_squares(s_square)
b = square_sum(s_square)
print ("sum of squares of ",s_square," is ", a)
print ("the square of the sum of ", s_square, " is ", b)
print ("the difference is ", b - a )


