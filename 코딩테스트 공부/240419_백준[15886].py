import sys
input = sys.stdin.readline

# 그래프,문자열/내 선물을 받아줘 2/실버3

n = int(input())
graph = input().strip()
ans = 1

for i in range(1,n):
  if graph[i:i+2]=='WE':
    ans += 1

print(ans)
