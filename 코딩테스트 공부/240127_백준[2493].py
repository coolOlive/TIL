import sys
input=sys.stdin.readline

# 스택/탑/골드5

n = int(input())
height = list(map(int,input().split()))
stack = []
ans = [0]*n

for i in range(n-1,-1,-1):
  while stack and height[i] > height[stack[-1]]:
    ans[stack.pop()] = i+1
  stack.append(i)

print(*ans)
