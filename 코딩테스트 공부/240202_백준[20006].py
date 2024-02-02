import sys
input=sys.stdin.readline

# 구현/랭킹전 대기열/실버2

p,m = map(int,input().split())
rooms = list()

for _ in range(p):
  l,n = map(str,input().split())
  l = int(l)
  flg = 0
  
  for room in rooms:
    if abs(l-room[0][0])<=10 and len(room)<m:
      room.append((l,n))
      flg = 1
      break

  if not flg:
    rooms.append([(l,n)])


for room in rooms:
  room.sort(key = lambda x:x[1])
  
for room in rooms:
  if len(room)==m:
    print('Started!')
  else:
    print('Waiting!')
  
  for ll,nn in room:
    print(ll,nn)
