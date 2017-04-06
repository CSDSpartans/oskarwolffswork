def general_poly(L):
    """
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    """

    def inner(x):
        count = len(L) - 1
        total = 0
        for num in L:
            total += num * x ** count
            count -= 1
        return total

    return inner


print(general_poly([1, 2, 3, 4])(10))
