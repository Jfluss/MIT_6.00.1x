# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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