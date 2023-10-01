# 브루트포스/부분수열의 합/실버1

n = int(input())
nums = list(map(int,input().split()))
nums.sort()
ans = 0

for num in nums:
  if ans+1<num:
    break
  ans += num

print(ans+1)
