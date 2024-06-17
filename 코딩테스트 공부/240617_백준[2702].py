import sys
input=sys.stdin.readline

# 수학/초6 수학/브론즈2

def lcm(a,b):
  return int((a*b) / gcd(a,b))

def gcd(a,b):
  if a == 0:
    return b
  else:
    return gcd(b % a, a)

t = int(input())

for i in range(t):
  a, b = map(int, input().split())
  print(lcm(a,b), gcd(a,b))
