import sys
input=sys.stdin.readline

# 정렬/종이자르기/실버5

w,h = map(int, input().split())
n = int(input())
width = [0, w]
height = [0, h]
ans = 0

for _ in range(n):
  a,b = map(int, input().split())
  if a == 0:
    height.append(b)
  elif a == 1:
    width.append(b)

width.sort()
height.sort()

for i in range(len(width)-1):
  for j in range(len(height)-1):
    x = width[i+1] - width[i]
    y = height[j+1] - height[j]
    ans = max(ans, x*y)

print(ans)
