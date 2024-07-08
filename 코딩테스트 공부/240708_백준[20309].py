import sys
input = sys.stdin.readline

# 수학/트리플 소트/실버3

n = int(input())
nums = list(map(int,input().split()))
ans = 'YES'

for i in range(n):
  if i % 2:
    if nums[i] % 2:
      ans = 'NO'
          
print(ans)
