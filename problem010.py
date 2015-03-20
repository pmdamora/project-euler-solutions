# Find the sum of all primes below 2 million
# https://projecteuler.net/problem=10
# Uses the Sieve of Eratosthenes

from math import sqrt


def sum_primes(limit):
    sieve = list(range(limit+1))  # Create list of every number from 0 to limit + 1
    sieve[1] = 0  # 1 cannot be prime, so set it to 0
    for n in range(2, int(sqrt(limit))+1):  # For all n not exceeding sqrt(limit)
        if sieve[n] > 0:  # Find the next number not crossed out
            for i in range(n*n, limit+1, n):  # We are deleting the multiples of n
                sieve[i] = 0
    return sum(sieve)

print(sum_primes(100))