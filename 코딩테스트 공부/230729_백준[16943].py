from itertools import permutations

# 조합,브루트포스/숫자 재배치/실버1

a, b = input().split()
b = int(b)
per = []
ans = -1

for nums in permutations(a):
  per.append(''.join(nums))

for num in per:
  if num[0] == '0':
    continue
  num = int(num)
  if num < b:
    ans = max(ans, num)

print(ans)
