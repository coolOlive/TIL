# 그리디,정렬/통나무 건너뛰기/실버1

t = int(input())

for _ in range(t):
  n = int(input())
  trees = sorted(list(map(int,input().split())))
  ans = 0

  for i in range(2,n):
    ans = max(ans,abs(trees[i]-trees[i-2]))
  print(ans)
