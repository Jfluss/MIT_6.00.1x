# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 20:56:30 2017

@author: Josh
"""
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    inc = [L[0]]
    dec = [L[0]]
    run = []
#   find increasing series
    for i in range(1,len(L)):
        if L[i]>=L[i-1]:
            if i-1 == 0:
                pass
            elif L[i-1]<L[i-2]:
                inc = [L[i-1]]
            inc.append(L[i])
            if len(inc)>len(run):
                run = inc
#   find decreasing series
        if L[i]<=L[i-1]:
            if i-1 == 0:
                pass
            elif L[i-1]>L[i-2]:
                dec = [L[i-1]]
            dec.append(L[i])
            if len(dec)>len(run):
                run = dec
    return sum(run)