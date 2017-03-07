# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:44:25 2017

@author: Josh
"""
def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    listC = []
    for i in range(0, len(listA)):
        listC.append(listA[i]*listB[i])
    return sum(listC)