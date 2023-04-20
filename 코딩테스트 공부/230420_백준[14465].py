import sys
input=sys.stdin.readline

# 누적합,슬라이딩윈도우/소가 길을 건너간 이유 5/실버2

n,k,b = map(int,input().split())
light = [0 for i in range(n)]

for _ in range(b):
  light[int(input())-1] = 1

tmp = sum(light[:k])
ans = tmp

for i in range(1,n-k+1):
  tmp = tmp - light[i-1] + light[i+k-1]
  ans = min(tmp,ans)

print(ans)
