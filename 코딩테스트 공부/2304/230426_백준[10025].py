import sys
input = sys.stdin.readline

# 슬라이딩윈도우/게으른 백곰/실버3

n, k = map(int,input().split())
ice = [0]*1000001
lastLoca = 0

for _ in range(n):
  g,x = map(int,input().split())
  ice[x] = g
  lastLoca = max(lastLoca,x)
  
gap = (2*k)+1
window = sum(ice[:gap])
ans = window

for i in range(gap,lastLoca+1):
  window = window - ice[i-gap] + ice[i]
  ans = max(ans,window)

print(ans)
