import sys
input = sys.stdin.readline

# 유클리드호제법/공약수/골드5

g, l = map(int, input().split())
div = l // g

def gcd(x,y):
  if x % y == 0:
    return y

  return gcd(y, x % y)

for i in range(int(div**0.5), 0, -1):
  if div%i == 0:
    x = g*i
    y = g*(div//i)
    
    if gcd(x,y) == g:
      print(x,y)
      break
