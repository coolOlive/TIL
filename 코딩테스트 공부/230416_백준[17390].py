import sys
input=sys.stdin.readline

# 누적합/이건 꼭 풀어야 해!/실버3

n,q = map(int,input().split())
nums = sorted(list(map(int,input().split())))
hap = [0]

for i in range(n):
  hap.append(hap[-1]+nums[i])

for _ in range(q):
  l,r = map(int,input().split())
  print(hap[r]-hap[l-1])
