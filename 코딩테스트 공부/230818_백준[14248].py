import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# dfs/점프 점프/실버2
# 재귀호출의 최대치 늘리기 빼먹었었다.

n=int(input())
move=list(map(int, input().split()))
start=int(input())
visited=[0]*n
cnt=1

def dfs(x):
  global cnt
  for nx in (x+move[x], x-move[x]):
    if 0<=nx<n and visited[nx]==0:
      cnt+=1
      visited[nx]=1
      dfs(nx)

dfs(start-1)

print(cnt)
