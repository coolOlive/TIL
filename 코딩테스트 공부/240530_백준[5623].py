# 수학/수열의 합/실버4

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

if n == 2:
  print(1, 1)
else:
  ans = [(nums[0][1]+nums[0][2]-nums[1][2]) // 2]
  for i in range(1, n):
    ans.append(nums[0][i]-ans[0])
  print(*ans)
