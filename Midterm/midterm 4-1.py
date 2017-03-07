# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:20:44 2017

@author: Josh
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    if base>num:
        return (0)
    i=1
    while (base**i)<num:
        i += 1

    a = abs((base**(i-1))-num)
    b = abs((base**(i))-num)
    print(a,b)
    if a<b:
        return(i-1)
    else:
        return(i)
