# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 12:00:23 2017

@author: Josh
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    cList = []
    for i in aList:
        if type(aList[i]) == list:
            cList.append(flatten(aList[i]))
        else:    
            cList.append(aList[[i]])
        print(cList)    
    return cList        