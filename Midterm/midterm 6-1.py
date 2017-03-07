# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:49:35 2017

@author: Josh
"""
L = [[1, 2], [3, 4], [5, 6, 7]]
def deep_reverse(L):
    """ 
    Assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    for i in range(0, len(L)):
        L[i].reverse()
        print(L[i])
    L.reverse()
    print (L)