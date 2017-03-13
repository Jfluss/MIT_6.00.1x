# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 20:25:01 2017

@author: Josh
"""

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    num = int(us_num)
    
    ones = str(num%10)
    tens = str(num//10)
    
    if num<11:
        return trans[us_num]
    elif num<20:
        return (trans['10']+ ' ' + trans[ones])
    else:
        answer = (trans[tens] + ' '+ trans['10'])
        if ones == '0':
            return answer
        else:
            return (answer + ' ' + trans[ones])

       