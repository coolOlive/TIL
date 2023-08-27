import sys
input=sys.stdin.readline

# 그리디,구현/A와 B/골드5

s = list(input().strip())
t = list(input().strip())
flg = 0

while t:
  if t[-1] == 'A':
    t.pop()
  elif t[-1] == 'B':
    t.pop()
    t.reverse()
  if s==t:
    flg = 1
    break

print(flg)
