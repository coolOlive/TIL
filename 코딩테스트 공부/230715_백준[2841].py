import sys
input=sys.stdin.readline

# 자료구조/외계인의 기타 연주/실버1

n,p = map(int, input().split())
line = [[] for _ in range(6)]
move = 0

for i in range(n):
  a,b = map(int, input().split())
  if not line[a-1]:
    line[a-1].append(b)
    move += 1
  else:
    while line[a-1] and b < line[a-1][-1]:
      line[a-1].pop()
      move += 1
    if not line[a-1] or b > line[a-1][-1]:
      line[a-1].append(b)
      move += 1

print(move)
