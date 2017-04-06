def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    best_power = int()
    previous_difference = num
    power = -1

    while True:
        power += 1
        product = base ** power
        distance = abs(product - num)

        if distance < previous_difference:
            previous_difference = distance
        else:
            return power - 1

# Test cases:
print(closest_power(3, 12))  # returns 2
print(closest_power(4, 12))  # returns 2
print(closest_power(10, 99))  # returns 0
