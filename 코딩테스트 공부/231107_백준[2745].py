# 구현,수학/진법 변환/브론즈2

nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = input().split()
ans = 0

for i, num in enumerate(n[::-1]):
  ans += int(b) ** i * nums.index(num)

print(ans)
