# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 19:20:07 2017

@author: Josh
MIT 6.00.1x Week 1 Problem 2
"""

s='bobot'
count = 0
index = 0
for index in range(0, len(s)):
    if s[index:index+3] == 'bob':
        count+=1
    index +=1
print('Number of times bob occurs is: ' + str(count))