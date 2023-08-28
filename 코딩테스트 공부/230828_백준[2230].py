import sys
input=sys.stdin.readline

# 이분탐색/수 고르기/골드5

n, m = map(int, input().split())
s, e = 0, 0
ans = int(2e9)
nums = []

for _ in range(n):
  nums.append(int(input()))
nums.sort()

while s <= e and e < n:
  if nums[e]-nums[s] < m:
    e += 1
  else:
    ans = min(ans, nums[e]-nums[s])
    s += 1

print(ans)
