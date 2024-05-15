import sys
input = sys.stdin.readline

# 그리디,정렬/5차 전직/실버2

n, k = map(int,input().split())
stone = list(map(int,input().split()))
stone.sort()
cnt,ans = 0,0

for i in range(n):
  ans += stone[i]*cnt
  if cnt < k:
    cnt += 1

print(ans)
