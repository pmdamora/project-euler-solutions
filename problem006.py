def sumofsquares(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    return sum

def squareofsum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum**2

k = 100
difference = squareofsum(k) - sumofsquares(k)
print(difference)
