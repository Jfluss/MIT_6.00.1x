# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 19:59:05 2017

@author: Josh
"""

from math import *
          
def polysum(n,s):
    """
    input n=number of sides
    s=side length
    output sum of area and square of perimeter
    """
    area = (.25*n*(s**2))/(tan(pi/n))
    perim = n*s
    x = round((area + (perim**2)),4)
    return x

polysum(12,13)
