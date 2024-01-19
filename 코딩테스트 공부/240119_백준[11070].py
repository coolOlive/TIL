import sys
input=sys.stdin.readline

# 구현/피타고라스 기댓값/브론즈1

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  score = [[0, 0] for _ in range(n)]
  ans = []
  
  for i in range(m):
    a, b, p, q = map(int, input().split())
    score[a - 1][0] += p
    score[a - 1][1] += q
    score[b - 1][0] += q
    score[b - 1][1] += p
  
  for j in range(n):
    if score[j][0] == 0 and score[j][1] == 0:
      ans.append(0)
    else:
      ans.append(1000 * score[j][0] ** 2 / (score[j][0] ** 2 + score[j][1] ** 2))

  print(int(max(ans)))
  print(int(min(ans)))
