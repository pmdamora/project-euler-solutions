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

number = 600851475143
factors = []
i = 2
max = 0
factoring = True


while factoring:
    if isPrime(int(number)):
        factors.append(number)
        factoring = False
    elif isPrime(i):
        if number % i == 0:
            number = number / i
            factors.append(i)
            i = 2
        else:
            i += 1
    else:
        i += 1
        
for factor in factors:
    if factor > max:
        max = factor

print(max)
    
