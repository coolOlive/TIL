import sys
input = sys.stdin.readline
from functools import reduce

# 구현,브루트포스/벚꽃이 정보섬에 피어난 이유/실버5

n = int(input())
flowers = list(map(int,input().split()))
flowers.append(1) 
ans = 0

def mul(a,b):
  return a*b

def group(i,j,k):
  global flowers
  total = reduce(mul,flowers[:i+1]) + reduce(mul,flowers[i+1:j+1])+ reduce(mul,flowers[j+1:k+1]) + reduce(mul,flowers[k+1:])
  return total

for i in range(n-3):
  for j in range(i+1,n-2):
    for k in range(j+1,n-1):
      ans = max(ans,group(i,j,k))

print(ans)
