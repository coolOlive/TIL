import sys
input = sys.stdin.readline

# 애드 혹/증가 배열 만들기/실버5

n,m,k = map(int,input().split())
nums = []

for i in range(n):
  tmp = []
  for j in range(m):
    tmp.append(i+j+1)
  nums.append(tmp)

if nums[n-1][m-1] <= k:
  print("YES")
  for num in nums:
    print(*num)
else:
  print("NO")
