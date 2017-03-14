# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 09:55:22 2017

@author: Josh
"""

def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def new_input(x):
        ans = 0
        exp = len(L)-1
        for i in L:
            ans+=(i*(x**exp))
            exp-=1
        return ans
    return new_input