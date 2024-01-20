import sys
input=sys.stdin.readline

# 수학/준석이의 수학 숙제/브론즈1

t = int(input())
nums = list(map(int,input().split()))

dp = [0] * 80001
tmp = 0

for i in range(3,80001):
  if i % 3 == 0 or i % 7 == 0:
    tmp += i
  dp[i] = tmp

for n in nums:
  print(dp[n])
