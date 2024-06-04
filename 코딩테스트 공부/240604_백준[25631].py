import sys
input=sys.stdin.readline

# 정렬,자료구조/마트료시카 합치기/실버5

n = int(input())
nums = list(map(int,input().split()))
ans = 0

while len(nums) > 0:
  tmp = set(sorted(nums))
  for t in tmp:
    del nums[nums.index(t)]
  ans += 1

print(ans)
