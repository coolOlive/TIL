# 그리디/팩토리얼 분해/실버5

n = int(input())
f = [1, 1]
hap = 0
ans = 'NO'

for i in range(2, 21):
  f.append(f[i-1]*i)

for i in range(20, -1, -1):
  tmp = hap+f[i]
  if tmp < n:
    hap = tmp
  elif tmp == n:
    ans = 'YES'
    break

print(ans)