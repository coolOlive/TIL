import sys
input=sys.stdin.readline

# 구현,정렬/키 큰 사람/실버5

t = int(input())
while t != 0:
  ans = list()
  height = 0
  
  for _ in range(t):
    name,h = map(str,input().split())
    h = float(h)
    
    if h>height:
      ans = [name]
      height = h
    elif h == height:
      ans.append(name)
  print(*ans)
  t = int(input())
