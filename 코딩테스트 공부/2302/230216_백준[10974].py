# 브루트포스,bfs,백트래킹/모든 순열/실버3

n = int(input())
ans = []

def dfs():
    if len(ans) == n:
        print(*ans)
        return
    for i in range(1, n+1):
        if i not in ans:
            ans.append(i)
            dfs()
            ans.pop()
dfs()
