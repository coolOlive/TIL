import sys
input=sys.stdin.readline

# 구현,문자열/준오는 조류혐오야!!/브론즈1

n,m = map(int,input().split())
nums = [list(map(str,input().split())) for _ in range(n)]
rnine = [0 for _ in range(n)]
cnine = [0 for _ in range(m)]

for i in range(n):
  for num in nums[i]:
    rnine[i] += num.count('9')

for i in range(m):
  for j in range(n):
    cnine[i] += nums[j][i].count('9')


rMax = max(rnine)
cMax = max(cnine)

print(sum(rnine) - max(rMax,cMax))
