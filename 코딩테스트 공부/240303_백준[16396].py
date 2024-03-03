import sys
input = sys.stdin.readline

# 구현/선 그리기/브론즈1

n = int(input())
y = [0]*10001

for _ in range(n):
  a,b = map(int,input().split())
  for i in range(a,b):
    y[i] = 1

print(sum(y))
