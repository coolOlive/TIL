# 브루트포스/적어도 대부분의 배수/브론즈1
# 시험기간, 너무 바쁘다;;;

nums = list(map(int, input().split()))
n = min(nums)

while True:
  cnt = 0
  for i in range(5):
    if n % nums[i] == 0:
      cnt += 1
  if cnt > 2:
    print(n)
    break
  n += 1
