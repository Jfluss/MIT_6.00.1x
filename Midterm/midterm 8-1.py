# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:28:08 2017

@author: Josh
"""
def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    temp_list=[]
    for i in L:
        if g(f(i)) == True:
            temp_list.append(i)
    print(temp_list)        
    L = temp_list  
    if L == []:
        return -1
    else:
        return max(L)
    