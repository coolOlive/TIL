import sys
input=sys.stdin.readline

# 구현/첼시를 도와줘!/브론즈2

t = int(input())

for _ in range(t):
  n = int(input())
  large = 0
  name = ''
  
  for i in range(n):
    a,b = map(str,input().split())
    a = int(a)
    if a>large:
      large = a
      name = b
      continue

  print(name)
