import sys
input=sys.stdin.readline
from collections import deque

# dp/연속합 2/골드5
## 처음에 가장 작은 음수 지우려 했는데
## 같은 수가 여러개이면 둘 중 무엇을 지워야 하는지 문제 생김

n = int(input())
nums = list(map(int,input().split()))
left = [nums[0]]+[0]*(n-1)
right = [0]*(n-1)+[nums[n-1]]

for i in range(1,n):
  left[i] = max(nums[i],left[i-1]+nums[i])
  

for j in range(n-2,-1,-1):
  right[j] = max(nums[j],right[j+1]+nums[j])

ans = max(right)
for i in range(1,n-1):
  ans = max(ans,left[i-1]+right[i+1])

print(ans)
