i = 2500
k = 200
found = False

while found is False:
    if all(i % n == 0 for n in reversed(range(2,k))):
        found = True
    else:
        i += k

print(i)
