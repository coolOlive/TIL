# 수학/최대 곱/실버2

s,k = map(int,input().split())
ans = 1

for i in range(k):
  if i < s%k:
    ans *= s//k+1
  else:
    ans *= s//k

print(ans)
