# -*- coding: utf-8 -*-
"""
Starting in the top left corner of a 2×2 grid, and only being able to move 
to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

My note: this is known as the central binomial coefficient with the form of

(2n!)/(n!)^2

http://www.robertdickau.com/lattices.html
http://stackoverflow.com/questions/24093387/pascals-triangle-for-python  

"""



import time
import math 

def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

start_time = time.time()

grid = 20

print (" Number of routes = ", int(factorial(2*grid))/(factorial(grid)**2))


elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))