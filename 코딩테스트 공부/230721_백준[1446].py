import sys
input=sys.stdin.readline

# dp,데이크스트라/지름길/실버1

n,d = map(int,input().split())
road = [list(map(int,input().split())) for _ in range(n)]
dis = [i for i in range(d+1)]

for i in range(d+1):
  dis[i] = min(dis[i],dis[i-1]+1)

  for start,end,L in road:
    if i==start and end<=d and dis[i]+L<dis[end]:
      dis[end] = dis[i]+L
    
print(dis[d])
