import sys
input=sys.stdin.readline

# 구현/복붙의 달인/실버5

t = int(input())

for _ in range(t):
  s, p = map(str, input().split())

  same = s.count(p)
  change = s.replace(p,'')
  
  print(same + len(change))
