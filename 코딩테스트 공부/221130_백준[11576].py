from collections import deque

# 수학,구현/Base Conversion/실버5

a,b = map(int,input().split())
m = int(input())
arr = list(map(int,input().split()))
arr.reverse()

ten = 0

for i in range(m):
    ten += arr[i]*(a**i)

result = deque()
while ten:
    result.appendleft(ten%b)
    ten = ten//b

print(' '.join(map(str,result)))