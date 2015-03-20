nextTerm = lastTerm = 1 
temp = 0
sum = 0

while(nextTerm < 4000000):
     temp = nextTerm
     nextTerm = nextTerm + lastTerm
     lastTerm = temp

     if nextTerm % 2 == 0:
         sum = sum + nextTerm

print(sum)
