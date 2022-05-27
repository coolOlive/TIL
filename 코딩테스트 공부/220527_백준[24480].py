import sys
from collections import deque
input=sys.stdin.readline

# dfs_알고리즘 수업 - 깊이 우선 탐색 2/실버2

n,m,r=map(int,input().split())

visited=[False]*(n+1)
num=[[] for _ in range(n+1)]
node_cnt=[0 for _ in range(n+1)]
cnt=1

for i in range(m):
    a,b=map(int,input().split())
    num[a].append(b)
    num[b].append(a)

for i in range(n+1):
    num[i].sort()

stack=deque()
stack.append(r)

while stack:
    tmp=stack.pop()
    visited[tmp]=True
    if node_cnt[tmp]==0:
        node_cnt[tmp]=cnt
        cnt+=1
    for x in num[tmp]:
        if not visited[x]:
            stack.append(x)


for cnt in node_cnt[1:]:
    print(cnt)