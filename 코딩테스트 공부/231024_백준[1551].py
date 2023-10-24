# 구현,문자열/수열의 변화/브론즈1
# 시험기간이라 한동안 쉬운 문제 풀 예정

n, k = map(int, input().split())
nums = list(map(int, input().split(',')))

for _ in range(k):
  tmp = []
  for i in range(len(nums)-1):
    tmp.append(nums[i+1]-nums[i])
  nums = tmp

print(*nums, sep=',')
