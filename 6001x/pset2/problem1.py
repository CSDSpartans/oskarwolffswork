'''
recursive interest calculator

if you only pay the minimum amount on your credit card each month, what is your
outstanding balance after a year?
'''
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def interest_calc(balance, annualInterestRate, monthlyPaymentRate, months):
    '''
    this function returns the remaining balance given those variables you can
    see above this
    '''
    balance -= balance * monthlyPaymentRate
    balance += (annualInterestRate / 12) * balance

    if months == 1:
        return balance
    else:
        return interest_calc(balance, annualInterestRate, monthlyPaymentRate, months - 1)


print(round(interest_calc(balance, annualInterestRate, monthlyPaymentRate, 12), 2))
