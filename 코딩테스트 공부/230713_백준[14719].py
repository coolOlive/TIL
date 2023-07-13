import sys
input=sys.stdin.readline

# 구현/빗물/골드5

h,w = map(int,input().split())
block = list(map(int,input().split()))
ans = 0

for i in range(1,w-1):
  left = max(block[:i])
  right = max(block[i+1:])
  water = min(left,right)

  if block[i]<water:
    ans += water-block[i]

print(ans)
