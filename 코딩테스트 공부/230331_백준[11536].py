import sys
input=sys.stdin.readline

# 정렬/줄 세우기/실버5

n = int(input())
names = [input().strip() for _ in range(n)]
increName = sorted(names)
decreName = sorted(names,reverse = True)

if names == increName:
  print('INCREASING')
elif names == decreName:
  print('DECREASING')
else:
  print('NEITHER')
