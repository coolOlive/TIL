import sys
input=sys.stdin.readline

# 두포인터/겹치는 건 싫어/실버1

n,k = map(int, input().split())
nums = list(map(int, input().split()))
cnt = [0] * (max(nums) + 1)
start, end, ans = 0, 0, 0

while end < n:
  if cnt[nums[end]] < k:
    cnt[nums[end]] += 1
    end += 1
  else:
    cnt[nums[start]] -= 1
    start += 1
  ans = max(ans, end - start)

print(ans)
