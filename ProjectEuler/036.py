import math

def decToBinary(n):
    if n == 1:
        return '1'

    eval = math.log(n,2)
    if eval == int(eval):
        digits = int(eval)+1
    else:
         digits = int(math.ceil(eval))
    s = ""
    for i in reversed(range(digits)):
        if n&(2**i) != 0:
            s = s + '1'
        else:
            s = s + '0'
    return s

def binaryToDec(n):
    s = str(n)[::-1]
    num = 0
    for i in range(len(s)):
        num += (int(s[i])*(2**i))
    return int(num)

def isPalindrome(n):
    s = str(n)
    s_rev = s[::-1]
    return s == s_rev

def search():
    sum = 0
    for i in range(1,1000000):
        if isPalindrome(i) and isPalindrome(decToBinary(i)):
            sum += i
    return sum

print(search()) # 872187
