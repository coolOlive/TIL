import sys
input=sys.stdin.readline

# 에라토스테네스의체/골드바흐 파티션/실버2

t = int(input())
prime = []
visit = [0]*1000001
visit[0] = 1
visit[1] = 1

for i in range(2,1000001):
  if visit[i] == 0:
    prime.append(i)
    for j in range(i*2,1000001,i):
      visit[j] =1

for _ in range(t):
  ans = 0
  n = int(input())
  for i in prime:
    if i >= n:
      break
    if visit[n-i] == 0 and i <= n-i:
      ans += 1
  print(ans)
