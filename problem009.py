__author__ = 'Paul'


def findc(x, y):
    return (x**2 + y**2)**0.5


def findabc(n):
    for i in range(1, n):
        for j in range(1, n):
            if i + j + findc(i, j) == n:
                product = i * j * findc(i, j)
                return product

n = 1000
print(findabc(n))