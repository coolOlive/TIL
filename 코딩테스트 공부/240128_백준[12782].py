import sys
input=sys.stdin.readline

# 그리디/비트 우정지수/실버4

t = int(input())

for _ in range(t):
  n, m = input().split()
  one = 0
  zero = 0
  for i in range(len(n)):
    if n[i] != m[i]:
      if m[i] == '1':
        one += 1
      else:
        zero += 1

  print(max(one,zero))
