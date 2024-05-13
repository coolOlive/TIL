import sys
input = sys.stdin.readline

# 구현,문자열/앵무새/실버2

n = int(input())
bird = [list(map(str,input().split())) for _ in range(n)]
talk = list(map(str,input().split()))
tmp = 0

for t in talk:
  flg = False
  for i in range(n):
    if len(bird[i]) != 0:
      if t == bird[i][0]:
        flg=True
        bird[i].pop(0)
        break
  if not flg:
    break

for b in bird:
  tmp += len(b)
if flg and tmp==0:
  print("Possible")
else:
  print("Impossible")
