import sys
input=sys.stdin.readline

# 에라토스테네스의 체/K-세준수/실버5

n = int(input())
m = int(input())
se = [0 for i in range(n+1)]
ans = 0

for i in range(2,n+1):
  if se[i] == 0:
    for j in range(i,n+1,i):
      if j%i == 0:
        se[j] = max(se[j],i)

for i in se:
  if i <= m:
    ans += 1

print(ans-1)
