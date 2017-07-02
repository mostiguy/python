# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 11:28:27 2016
@author: ostm
"""

import numpy as np
import matplotlib.pyplot as plt

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

print (fib(50))
