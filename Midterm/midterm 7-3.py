# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:13:02 2017

@author: Josh
"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
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
    def difference(d1, d2):
        '''
    d1, d2 are dictionaries.
    returns a dctionary dB with key-value pairs for keys which are not in both d1 and d2.
        '''
        dB={}
        copy1 = d1.copy()
        copy2 = d2.copy()
        for key in d1:
            if key not in d2:
                dB[key] = copy1[key]
        for key in d2:
            if key not in d1:
                dB[key] = copy2[key]
        return dB  
    
    dC = (intersect(d1,d2), difference(d1,d2))
    return dC
            