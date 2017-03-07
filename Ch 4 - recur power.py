# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 22:46:50 2017

@author: Josh
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0 :
        ans=1
    else:
        ans = base*recurPower(base, exp-1)
    return ans