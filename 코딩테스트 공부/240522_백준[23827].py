import sys
input=sys.stdin.readline

# 수학,누적합/수열 (Easy)/실버4

n=int(input())
nums=list(map(int,input().split()))
hap=sum(nums)
ans=0

for i in nums:
  hap -= i
  ans = (ans+i*hap)%1000000007

print(ans)
