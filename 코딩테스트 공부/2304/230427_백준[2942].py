import sys
input=sys.stdin.readline

# 유클리드호제법/퍼거슨과 사과/실버2

r,g = map(int, input().split())

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

tmp = gcd(r,g)
last = int(tmp**0.5)

for i in range(1, last+1):
  if tmp % i == 0:
    print(i,r//i,g//i)
    x= tmp // i
    if x == i:
      continue
    print(x,r//x,g//x)
