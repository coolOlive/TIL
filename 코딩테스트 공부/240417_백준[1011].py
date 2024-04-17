import sys
input=sys.stdin.readline

# 수학/Fly me to the Alpha Centauri/골드5
# 풀이 찾아서 해결함..

t = int(input())

for _ in range(t):
  x, y = map(int,input().split())
  distance = y - x
  cnt,total,move = 0,0,1
  
  while total < distance:
    cnt += 1
    total += move
    if cnt % 2 == 0:
      move += 1
          
  print(cnt)
