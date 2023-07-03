import sys
input=sys.stdin.readline

# 그리디/뒤집기 II/실버2

n,m = map(int,input().split())
coin = [list(map(int, list(input().strip()))) for _ in range(n)]
ans = 0

for i in range(n - 1, -1, -1):
  for j in range(m - 1, -1, -1):
    if coin[i][j]:
      ans += 1
      for a in range(i+1):
        for b in range(j+1):
          coin[a][b] ^= 1

print(ans)
