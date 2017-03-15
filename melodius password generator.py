#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 09:32:36 2017

@author: joshfluss
"""

vowels = 'aeiou'
consonents = 'bcdfghjklmnpqrstvwxz'
answers = []
n=3
for i in consonents:
    answers.append(i)
for i in vowels:
    answers.append(i)
#flag = True
#for i in answers:
#    print(i)
count=1
temp = answers[:]
while count<n:
    temp2=[]
    for i in temp:
        if i[-1] in consonents:
            for k in vowels:
                temp2.append(i+k)             
            
        if i[-1] in vowels:
            for k in consonents:
                temp2.append(i+k)
    temp=temp2[:]
    for i in temp:
        answers.append(i)
    count+=1
                    
                
for i in answers:
    print(i)
    

    