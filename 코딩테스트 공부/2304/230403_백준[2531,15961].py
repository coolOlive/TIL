from collections import defaultdict
import sys
input=sys.stdin.readline

# 슬라이딩윈도우,투포인터/회전 초밥/실버1,골드4

n,d,k,c = map(int,input().split())
susi = [int(input()) for _ in range(n)]
dic = defaultdict(int)
start,end = 0,k-1
dic[c] += 1

for i in range(k):
  dic[susi[i]] += 1

ans = -int(1e9)

while start < n:
  ans = max(len(dic),ans)
  dic[susi[start]] -= 1

  if dic[susi[start]] == 0:
      del dic[susi[start]]

  start += 1
  end += 1
  dic[susi[end%n]] += 1

print(ans)
