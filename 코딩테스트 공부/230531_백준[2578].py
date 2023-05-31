import sys
input = sys.stdin.readline

# 구현/빙고/실버4

bingo1 = [list(map(int,input().split()))for i in range(5)]
bingo2 = list(map(list,zip(*bingo1)))
talk = []
for i in range(5) :
    talk += list(map(int,input().split()))
bingo = bingo1+bingo2
cnt = [0]*12
ans = 0
flg = True

cross1,cross2 = [],[]
for i in range(5) :
  cross1.append(bingo1[i][i])
  cross2.append(bingo2[i][4-i])
bingo.append(cross1)
bingo.append(cross2)

for t in talk:
  cnt = 0
  ans +=1
  for b in bingo:
    if t in b :
      b.remove(t)
    if b == []:
      cnt +=1
  if cnt >= 3:
    break
    
print(ans)
