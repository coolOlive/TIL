import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

# dfs/숫자고르기/골드5

n=int(input())
graph=[0]+[int(input()) for _ in range(n)]
ans=[]

def dfs(v,i):
  tmp=graph[v]
  visit[v]=True
  if not visit[tmp]:
    dfs(tmp,i)
  elif tmp==i:
    ans.append(tmp)

for i in range(1,n+1):
  visit = [False]*(n+1)
  dfs(i,i)
  
print(len(ans))

ans.sort()
for i in ans:
  print(i)
