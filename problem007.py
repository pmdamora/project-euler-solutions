__author__ = "Paul D'Amora"

def isPrime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    else:
        for div in range(2, x):
            if x % div == 0:
                return False
        return True

numPrimes = 0
i = 1
while numPrimes < 10001:
    i += 1
    if isPrime(i):
        numPrimes += 1


print(i)