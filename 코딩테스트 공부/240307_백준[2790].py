import sys
input = sys.stdin.readline

# 그리디/F7/실버2

n = int(input())
score = [int(input()) for _ in range(n)]
score.sort()

for i in range(len(score)):
  score[i]+=n
  n-=1

maxS = max(score)
ans = 0

for i in range(len(score)-1):
  if score[i] >= maxS:
    ans += 1
  n += 1
  score[i+1] += n

if score[-1]>maxS:
  print(ans+1)
else:
  print(ans)
