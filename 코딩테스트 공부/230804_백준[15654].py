# 백트래킹/N과 M (5)/실버3

n,m = map(int, input().split())
L = sorted(list(map(int, input().split())))
visited = [False]*n
tmp = []

def nm(depth,n,m):
  if depth == m:
    print(' '.join(map(str,tmp)))
    return
  for i in range(n):
    if not visited[i]:
      visited[i] = True
      tmp.append(L[i])
      nm(depth+1,n,m)
      tmp.pop()
      visited[i] = False

nm(0,n,m)
