import math
import sys
input=sys.stdin.readline

# dp,그리디/Four Squares/실버3
# 시간초과, 메모리 초과로 고생함.. dp로는 나중에 더 해보자.

def fourSquares(n) :
    if math.sqrt(n).is_integer():
        return 1
    for i in range(1, int(math.sqrt(n)) + 1):
        if math.sqrt(n - i**2).is_integer():
            return 2
    for i in range(1, int(n**0.5)+1):
        for j in range(1, int((n-i*i)**0.5)+1):
            if ((n-i*i-j*j)**0.5).is_integer():
                return 3
    return 4
 
n = int(input())
print(fourSquares(n))