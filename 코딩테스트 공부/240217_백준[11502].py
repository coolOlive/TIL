import sys
input=sys.stdin.readline

# 수학,에라토스테네스의체/세 개의 소수 문제/실버4

t = int(input())
nums = [int(input()) for _ in range(t)]

erato = []
visited = [False,False] + [True]*1000

for i in range(2,1000):
  if visited[i]:
    erato.append(i)
    for j in range(i,1000,i):
      visited[j] = False

def cal(n):
  global erato
  
  for i in erato:
    for j in erato:
      for k in erato:
        if i+j+k == n:
          print(i,j,k)
          return

for n in nums:
  cal(n) 
