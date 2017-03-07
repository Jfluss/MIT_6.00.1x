# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 22:46:50 2017

@author: Josh
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    ans=base
    if exp == 0 :
        ans=1
    while exp > 1 :
        ans = ans * base
        exp -= 1 
    return ans