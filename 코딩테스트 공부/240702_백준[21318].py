import sys
input = sys.stdin.readline

# 누적합/피아노 체조/실버1

n = int(input())
level = list(map(int,input().split()))
q = int(input())
s = [0] * n

for i in range(1, n):
  if level[i-1]>level[i]:
    s[i] = s[i-1]+1
    continue
  s[i] = s[i-1]
  
for _ in range(q):
  x,y = map(int,input().split())
  print(s[y-1]-s[x-1])
