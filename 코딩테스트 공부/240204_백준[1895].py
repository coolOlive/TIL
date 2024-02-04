import sys
input=sys.stdin.readline

# 구현/필터/실버4

r,c = map(int,input().split())
img =  [list(map(int,input().split())) for _ in range(r)]
t = int(input())
ans = 0

def filt(i,j):
  filt = sorted([img[i][j],img[i][j+1],img[i][j+2],
          img[i+1][j],img[i+1][j+1],img[i+1][j+2],
          img[i+2][j],img[i+2][j+1],img[i+2][j+2]])
  if filt[4]>= t:
    return 1
  return 0
          

for i in range(r-2):
  for j in range(c-2):
    ans += filt(i,j)
    
print(ans)
