import sys
input = sys.stdin.readline

# 백트래킹/1, 2, 3 더하기 2/실버1
# 어려웠음..

n, k = map(int, input().split())
cnt = 0

def dfs(num, ans):
  global cnt
  if num > n:
    return
  if n == num:
    cnt += 1
    if cnt == k:
        print(ans[:-1])
        exit()
  for i in (1, 2, 3):
    dfs(num + i, ans+str(i)+'+')

dfs(0, '')
print(-1)
