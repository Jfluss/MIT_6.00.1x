# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 12:49:03 2017

@author: Josh
"""

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
            