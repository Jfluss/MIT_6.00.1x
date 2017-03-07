# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 15:58:04 2017

@author: Josh
"""
balance = 3926
annualInterestRate = .2

def credit(balance, annualInterestRate, minPayment, n=12):
        '''
        balance - outstanding balance on the credit card
        annualInterestRate - annual interest rate as a decimal
        monthlyPaymentRate - minimum monthly payment rate as a decimal
        n - int number of months >0 in calculation
        Output - total balance after n months
        '''
        if n == 0:
            ans = balance
            return round(ans,2)
        else: 
            ubalance = credit(balance, annualInterestRate, minPayment, n-1) - minPayment 
            ans = ubalance + ubalance*(annualInterestRate/12)
            return round(ans,2)
        
def minpay(balance, annualInterestRate, count = 1):
    '''
    takes credit and determines minimum monthly payments
    '''
    minPayment = 10
    if balance == 0:
        return 0
    while (credit(balance, annualInterestRate, minPayment, 12))>=0:
        minPayment += 10
    return minPayment

print('Lowest Payment: ' +str(minpay(balance, annualInterestRate)))  
