# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:04:45 2017

@author: Josh
"""

def intersect(d1, d2):
    '''
    d1, d2 are dictionaries.
    for keys in d1 and d2, create new dictionary dA which has keys of the union of those dictionaries and has f(a,b) as values. 
    f() is defined externally, either as a+b or a>b.
    '''
    dA = {}
    copy1 = d1.copy()
    copy2 = d2.copy()
    for key in d1:
        if key in d2:
            dA[key] = f(copy1[key], copy2[key])
    return dA