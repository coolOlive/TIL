import sys
input = sys.stdin.readline

# 수학/베스킨라빈스 31/실버4

n = int(input())

for i in range(1, n+1):
  tmp = i+1
  
  if 30 % tmp == 0:
    print(i)
