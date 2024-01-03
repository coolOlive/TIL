# 정렬/콘서트/브론즈1

n = int(input())
nums = sorted(list(map(int, input().split())))
flg = 1

for i in range(n):
  if i+1 != nums[i]:
    print(i + 1)
    flg = 0
    break
if flg:
  print(n+1)
