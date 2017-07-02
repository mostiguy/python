# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:52:50 2016

@author: ostm
"""
import numpy
import math

my_array = [1,2,3]


my_array[1] = int(input("Enter the 1st number of the Ulam seq:"))
my_array[2] = int(input("Enter the 2nd number of the Ulam seq:"))
seq_len = int(input("Enter the sequence length:"))

print("Voici la sequence de ulam pour les ", seq_len)

for i in range(3,seq_len):
    if my_array[1]+my_array[2] == i:
        print(i)
        
        
