# 그리디/배수 스위치/실버4

n = ['N']+list(input())
ans = 0

for i in range(1,len(n)):
  if n[i]=='N':
    continue
  for j in range(i,len(n),i):
    if n[j]=='Y':
      n[j]='N'
    else:
      n[j] = 'Y'
  ans += 1

print(ans)
