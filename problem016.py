__author__ = 'Paul'

n = 1000
sum = 0

for c in str(2**n):
    sum += int(c)

print(sum)