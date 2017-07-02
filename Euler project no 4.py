# -*- coding: utf-8 -*-
"""
Euler project #4

 palindromic number reads the same both ways. 
 The largest palindrome made from the product of 
 two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
# 


def is_palindrome(p):
    my_str = str(p)
    my_str_reverse = my_str[::-1]
    if list(my_str) == list(my_str_reverse):
        return True
    else :
        return False
 
a1 = 999
a2 = a1
found = False
pal = 0
pal_list = []
i = 1
largest_pal = pal

while a1>1:
    while found == False:
        pal = a1 * a2
        if is_palindrome(pal) == True:
            pal_list.append(pal)
            if pal > largest_pal:
                largest_pal = pal
            i += 1
            break
        elif a2>99:
            a2 -=1
        else:
            break
    
    a1 -=1
    a2 = a1
    if a1 ==99:
        break
    
print (pal_list)
print (largest_pal, " is the largest palindrome with 3 digits")

#for j in range (j, len(pal_list)):
#   print (pal_list[j])
    


        

    
