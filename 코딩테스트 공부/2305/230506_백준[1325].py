from collections import deque
import sys
input = sys.stdin.readline

# bfs/효율적인 해킹/실버1
# 시간초과때문에 결국 pypy로 제출

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
maxCnt = 1
ans = []

for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

def bfs(start):
    cnt = 1
    que = deque([start])
    visit = [False for _ in range(n+1)]
    visit[start] = True
    
    while que:
      tmp = que.popleft()

      for g in graph[tmp]:
        if not visit[g]:
          cnt += 1
          visit[g] = True
          que.append(g)
		
    return cnt


for i in range(1,n+1):
  cnt = bfs(i)
  if cnt > maxCnt:
    maxCnt = cnt
    ans = [i]
  elif cnt == maxCnt:
    ans.append(i)

print(*ans)
