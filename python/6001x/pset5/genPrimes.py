'''
Write a generator, genPrimes, that returns the sequence of prime numbers on
successive calls to its next() method: 2, 3, 5, 7, 11, ...

Have the generator keep a list of the primes it's generated.
A candidate number x is prime if (x % p) != 0 for all earlier primes p.
'''


def genPrimes():
    past_primes = []
    count = 2

    while True:
        is_prime = True
        for prime in past_primes:
            if count % prime == 0:
                is_prime = False
                break
        if is_prime:
            yield count
            past_primes.append(count)
        count += 1


primes = genPrimes()

for x in primes:
    print(x)
