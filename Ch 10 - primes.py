# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 12:34:50 2017

@author: Josh
"""

def genPrimes():
    i=1
    primes = []
    while True:
        i+=1
        primeNum = True
        for num in primes:
            if i%num == 0:
#                primeNum = False
                break
#        if primeNum == True:
        else:    
            primes.append(i)
            yield(i)
        