__author__ = 'Paul'

import functools

def find_divisors(n):
    return len(set(functools.reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

found = False
i = 1
triangle = 0
k = 5

while not found:
    triangle += i
    if find_divisors(triangle) > k:
        found = True

    i += 1

print(triangle)