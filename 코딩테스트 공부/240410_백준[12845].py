import sys
input = sys.stdin.readline

# 그리디/모두의 마블/실버3

n = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
lv = nums[0]
ans = 0

for i in range(1,n):
  ans += lv+nums[i]
  if lv < nums[i]:
    lv = nums[i]

print(ans)
