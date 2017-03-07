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
    def flatten_int(aList):
        for i in range(0, len(aList)):
            if type(aList[i]) == list:
                flatten_int(aList[i])
            else:    
                    cList.append(aList[i])
            print(cList)    
            return cList        
    return flatten_int(aList)