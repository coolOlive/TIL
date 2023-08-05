# 정렬/역원소 정렬/실버5

n, *nums = input().split()
ans = []

while len(nums) < int(n):
  nums.extend(input().split())

for num in nums:
  ans.append(int(num[::-1]))
ans.sort()

print(*ans, sep="\n")
