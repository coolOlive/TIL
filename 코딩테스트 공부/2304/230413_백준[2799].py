import sys
input=sys.stdin.readline

# 구현/블라인드/실버4

n,m= map(int,input().split())
blind = [0,0,0,0,0]

for k in range(5*n+1):
  windows = input().strip()
  if k == 0:
    wincnt = [0]*m
    continue
  for i in range(1,5*m,5):
    if windows[i] == '#':
      for w in wincnt:
        blind[w] += 1
      wincnt = [0]*m
      break
    if windows[i] == '*':
      wincnt[abs(m-((m*5+1)-i)//5)] += 1
          
print(*blind)
