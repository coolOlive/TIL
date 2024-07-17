import sys
input = sys.stdin.readline

# 구현/사탕 게임/실버2

n = int(input())
b = [list(input().strip()) for _ in range(n)]
max_len = 1

def chk_len(b, n):
  m = 1
  for i in range(n):
    r, c = 1, 1
    for j in range(1, n):
      if b[i][j] == b[i][j-1]:
        r += 1
      else:
        r = 1
      m = max(m, r)

      if b[j][i] == b[j-1][i]:
        c += 1
      else:
        c = 1
      m = max(m, c)
  return m

for i in range(n):
  for j in range(n):
    if j + 1 < n:
      b[i][j], b[i][j+1] = b[i][j+1], b[i][j]
      max_len = max(max_len, chk_len(b, n))
      b[i][j], b[i][j+1] = b[i][j+1], b[i][j]
    
    if i + 1 < n:
      b[i][j], b[i+1][j] = b[i+1][j], b[i][j]
      max_len = max(max_len, chk_len(b, n))
      b[i][j], b[i+1][j] = b[i+1][j], b[i][j]

print(max_len)
