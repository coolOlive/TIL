import sys
input = sys.stdin.readline

# 소수판정/최대공약수/실버1

n = int(input())
nnums = list(map(int,input().split()))
m = int(input())
mnums = list(map(int,input().split()))
a,b = 1,1

def gcd(x,y):
  while y>0:
    tmp = x%y
    x = y
    y = tmp
  return x

for nn in nnums:
  a *= nn

for mn in mnums:
  b*= mn

ans = str(gcd(a,b))[-9:]
print(ans)
