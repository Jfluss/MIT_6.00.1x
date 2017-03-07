# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 19:19:58 2017

@author: Josh
MIT 6.00.1x Week 1 Problem 2
"""

count = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count+=1
print('Number of vowels: ' + str(count))