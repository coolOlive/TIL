import sys
input = sys.stdin.readline

# 트리,dfs/트리/골드5
# 트리는 dfs로 풀자!

n = int(input().strip())
tree = list(map(int,input().split()))
delete = int(input())
ans = 0

def dfs(delete):
  tree[delete] = -2
  for i in range(n):
    if tree[i] == delete:
      dfs(i)

dfs(delete)


for i in range(n):
  if i not in tree and tree[i] !=-2:
    ans+=1

print(ans)
