import sys
input = sys.stdin.readline

# 이분탐색/파닭파닭/실버2

s, c = map(int,input().split())
L = [int(input()) for _ in range(s)]

start = 1
end = max(L)

chicken = 0

while start<=end:
  mid = (start+end) // 2
  cnt = sum(l//mid for l in L)
  
  if cnt >= c:
    chicken = max(chicken,mid)
    start = mid+1
  else:
    end = mid -1

print(sum(L) - (c * chicken))
