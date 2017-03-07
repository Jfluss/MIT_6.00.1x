# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 15:58:04 2017

@author: Josh
"""
balance = 999999
annualInterestRate = .18

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
            return ans
        else: 
            ubalance = credit(balance, annualInterestRate, minPayment, n-1) - minPayment 
            ans = ubalance + ubalance*(annualInterestRate/12)
            return ans
        
def minpay(balance, annualInterestRate):
    '''
    takes credit and determines minimum monthly payments
    '''
    low = balance/12
    high = (credit(balance, annualInterestRate, 0, 12))/12
    minPayment = (low+high)/2
    if balance == 0:
        return 0
    while abs(credit(balance, annualInterestRate, minPayment, 12)) > 0.01:    
        if credit(balance, annualInterestRate, minPayment, 12)>0:
            low = minPayment
        else:
            high = minPayment
        minPayment = (low+high)/2    
    return round(minPayment,2)

print('Lowest Payment: ' +str(minpay(balance, annualInterestRate)))