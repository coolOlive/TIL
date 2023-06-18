import sys
input = sys.stdin.readline

# 그리디,정렬/귀찮음/실버5

n = int(input())
stick = sorted(list(map(int, input().split())))
total = sum(stick)
ans  = 0

for st in stick:
  total -= st
  ans += st * total

print(ans)
