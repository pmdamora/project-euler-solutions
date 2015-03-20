__author__ = 'Paul'

import time

start = time.clock()

def nextcol(n):
    if n%2 == 0:
        return n/2
    else:
        return (n * 3) + 1


def collatz(x):
    term = x
    i = 0
    while term != 1:
        term = nextcol(term)
        i += 1
    return i + 1

k = 1000000
chain = (0, k)

for n in range (k, k//2, -1):
    if collatz(n) > chain[0]:
        chain = (collatz(n), n)

print(chain[1])

end = time.clock()
print( end - start, " seconds")