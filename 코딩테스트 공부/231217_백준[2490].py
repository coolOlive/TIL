# 구현/윷놀이/브론즈3

for _ in range(3):
  game = list(map(int,input().split()))
  cnt = sum(game)
  if cnt == 3:
    print('A')
    continue
  if cnt == 2:
    print('B')
    continue
  if cnt == 1:
    print('C')
    continue
  if cnt == 0:
    print('D')
    continue
  print('E')
