import sys
input=sys.stdin.readline

# 수학,누적합/귀찮아 (SIB)/실버5

n = int(input())
nums = list(map(int, input().split()))
hap,ans = 0,0

for i in range(len(nums)-1,0,-1):
  hap += nums[i]
  ans += hap*nums[i-1]

print(ans)
