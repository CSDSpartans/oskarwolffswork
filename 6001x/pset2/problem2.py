#!/usr/bin/env python3
'''
calculate the minimum monthly payment to pay off credit card debt within a
year, given the balance and annual interest rate

monthly payment must be a multiple of 10
'''

balance = 3329
annualInterestRate = 0.2


def interest_calc(balance, annualInterestRate, monthlyPayment, months):
    '''
    this function returns the remaining balance given those variables you can
    see above this
    '''
    balance -= monthlyPayment
    balance += (annualInterestRate / 12) * balance

    if months == 1:
        return balance
    else:
        return interest_calc(balance, annualInterestRate, monthlyPayment, months - 1)


def payment_tester(balance, annualInterestRate, monthlyPayment):
    '''
    this function returns True if monthly payment is sufficient
    '''
    balance = interest_calc(balance, annualInterestRate, monthlyPayment, months=12)

    if balance <= 0:
        return True
    else:
        return False

monthlyPayment = 0
sufficientPayment = False

while not sufficientPayment:
    monthlyPayment += 10
    sufficientPayment = payment_tester(balance, annualInterestRate, monthlyPayment)

print(monthlyPayment)
