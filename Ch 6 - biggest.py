# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 12:22:53 2017

@author: Josh
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result= ''
    myDict = {}
    for i in aDict.keys():
        myDict[i] = len(aDict[i])
    for i in myDict.keys():    
        if myDict[i] == max(myDict.values()):
            result = result + i
    if len(aDict.keys())== 0:
        result = None
    return result