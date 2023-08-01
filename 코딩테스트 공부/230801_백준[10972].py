# 수학,조합론/다음 순열/실버3

n = int(input())
nums = list(map(int, input().split()))

for i in range(n-1, 0, -1):
  if nums[i-1] < nums[i]:
    for j in range(n-1, 0, -1):
      if nums[i-1] < nums[j]:
        nums[i-1], nums[j] = nums[j], nums[i-1]
        nums = nums[:i] + sorted(nums[i:])
        print(" ".join(map(str, nums)))
        flg = 1
        break
    if flg:
      break
else:
  print(-1)
