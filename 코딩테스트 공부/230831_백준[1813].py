import sys
input=sys.stdin.readline

# 애드 혹/논리학 교수/브론즈1

n = int(input())
nums = list(map(int,input().split()))
arr = [0]*51

for num in nums:
  arr[num] += 1

for i in range(50,-1,-1):
  if arr[i] == i:
    print(i)
    break
else:
  print(-1)
