from itertools import permutations

# 조합,브루트포스,문자열/크면서 작은 수/실버3

n = list(input())
num = ''.join(n)
per = list(permutations(num,len(num)))
per = sorted(per,reverse = True)
flg = False
ans = 0

for i in range(len(per)):
  tmp = ''.join(per[i])
  if tmp>num:
    flg = True
    ans = tmp

print(ans)
