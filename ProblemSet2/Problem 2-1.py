# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 15:11:37 2017

@author: Josh
"""
balance = 42
annualInterestRate = .2
monthlyPaymentRate = .04

def credit(balance, annualInterestRate, monthlyPaymentRate, n=12):
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
        ubalance = credit(balance, annualInterestRate, monthlyPaymentRate, n-1) \
            -(monthlyPaymentRate*credit(balance, annualInterestRate, monthlyPaymentRate, n-1))
        ans = ubalance + ubalance*(annualInterestRate/12)
        return round(ans,2)
   
print('Remaining balance: ' + str(credit(balance, annualInterestRate, monthlyPaymentRate)))