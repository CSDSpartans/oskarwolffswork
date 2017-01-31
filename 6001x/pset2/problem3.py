'''
same as problem 2, but calculating to the nearest cent using bisection search

the margin of error needs to be played with when submitting because if too
small, the code takes too long to run on their servers
'''

balance = 320000
annualInterestRate = 0.2



def remaining_balance_calc(balance, annualInterestRate, monthlyPayment, months):
    '''
    this function returns the remaining balance given those variables you can
    see above this
    '''
    balance -= monthlyPayment
    balance += (annualInterestRate / 12) * balance

    if months == 1:
        return balance
    else:
        return remaining_balance_calc(balance, annualInterestRate, monthlyPayment, months - 1)


def payment_finder_bisection(balance, annualInterestRate):
    bottom = balance / 12
    top = (balance * (1 + annualInterestRate / 12) ** 12) / 12
    monthlyPayment = (top + bottom) / 2

    remaining_balance = remaining_balance_calc(balance, annualInterestRate, monthlyPayment, 12)

    while abs(remaining_balance) > .2:
        remaining_balance = remaining_balance_calc(balance, annualInterestRate, monthlyPayment, 12)
        if remaining_balance < 0:
            top = monthlyPayment
        elif remaining_balance > 0:
            bottom = monthlyPayment

        monthlyPayment = round((top + bottom) / 2, 2)

    return monthlyPayment

print(payment_finder_bisection(balance, annualInterestRate))
