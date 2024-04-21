import sys
input = sys.stdin.readline

# 구현/The candy war/실버5

t = int(input())

def same(candy):
  for i in range(len(candy)):
    if candy[i]%2==1:
      candy[i]+=1
  return len(set(candy))==1

def play(n,candy):
  cnt = [0]*n
  for i in range(n):
    if candy[i]%2==1:
      candy[i]+=1
    candy[i]//=2
    cnt[(i+1)%n] += candy[i]

  for j in range(n):
    candy[j] += cnt[j]
  

for _ in range(t):
  n = int(input())
  candy = list(map(int,input().split()))
  ans = 0
  
  while not same(candy):
    play(n,candy)
    ans += 1
  print(ans)
