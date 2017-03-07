# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 19:20:07 2017

@author: Josh
MIT 6.00.1x Week 1 Problem 3
"""

s = 'zndotvlinsoms'
count = 1
index = 0
text = s[0]
for index in range(1, len(s)):
        if ord(s[index])>=ord(s[index-1]):
            count+=1
            if len(s)==(index+1) and len(text) < count:
                text = s[index-count+1:]
                count = 1
        else:
            if len(text) < count:
                text = s[index-count:index]
            count = 1
        index +=1
print('Longest substring in alphabetical order is: ' + str(text))