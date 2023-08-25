import sys
input = sys.stdin.readline
from collections import deque

# bfs,소수판정/소수 경로/골드4

t = int(input())

def isPrime(num):
  if num == 1:
    return False
  for i in range(2, int(num**0.5)+1):
    if num % i == 0:
      return False
  return True

prime = [False]
for i in range(1,10000):
  prime.append(isPrime(i))

def bfs(a,b):
  que = deque()
  que.append((a,0))
  while que:
    pw, count = que.popleft()
    if pw == b:
      print(count)
      return
    for i in range(4):
      for j in range(10):
        change = list(str(pw))
        change[i] = str(j)
        change = int(''.join(change))
        if 1000<=change and not visited[change] and prime[change]:
          visited[change] = 1
          que.append((change, count+1))
              

for _ in range(t):
  tmp1,tmp2 = map(int, input().split())
  visited = [0]*10000
  visited[tmp1] = 1
  bfs(tmp1,tmp2)
