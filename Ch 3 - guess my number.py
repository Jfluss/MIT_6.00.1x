# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 12:07:52 2017

@author: Josh
"""

high = 100
low = 0
ans = int((high+low)/2)
x = ''    
print('Please think of a number between 0 and 100!')

while x!=('c'):
    ans = int((high+low)/2)
    print('Is your secret number ' + str(ans) + '?')    
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the \
              guess is too low. Enter 'c' to indicate I guessed correctly. ", )
    if x is 'l':
        low = ans
    elif x is 'h' :
        high = ans
    elif x is 'c' :
        print('Game over. Your secret number was: ' + str(ans))
    else:
        print('Sorry, I did not understand your input.')
