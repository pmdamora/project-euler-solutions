# Determines whether a number (or string) is a palindrome
def isPalindrome(x):
    return str(x) == str(x)[::-1]
        
# Define variables
max = 111111 # We know there is a palindrome larger than 
p = 0

for i in range(999, 100, -1):
    if max >= i * 999:
        break
    for j in range(999, i, -1):
        p = i * j
        if max < p and isPalindrome(p):
            max = p
print(max)
