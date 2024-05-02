# 구현/긴급 회의/브론즈1

n = int(input())
nums = list(map(int, input().split()))
cnt = [0] * n

for num in nums :
  if num!=0:
    cnt[num-1] += 1

tmp = max(cnt)
if cnt.count(tmp) >= 2 or tmp == 0 :
  print('skipped')
else :
  print(cnt.index(tmp) + 1)