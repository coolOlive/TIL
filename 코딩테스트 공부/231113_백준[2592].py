# 구현/대표값/브론즈2

nums = [int(input()) for _ in range(10)]
cnt = [0]*(1001)

for num in nums:
  cnt[num]+=1

print(sum(nums)//10)
print(cnt.index(max(cnt)))
