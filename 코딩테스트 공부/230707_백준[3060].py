import sys
input = sys.stdin.readline

# 구현,수학/욕심쟁이 돼지/실버5

t = int(input())

for _ in range(t):
  n = int(input())
  eat = sum(list(map(int,input().split())))
  ans = 1
  while n >= eat:
    ans += 1
    eat *= 4
  print(ans)
