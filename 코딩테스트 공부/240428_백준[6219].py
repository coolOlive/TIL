# 에라토스테네스의체,소수판정/소수의 자격/실버3

a,b,d = map(int,input().split())
visit = [1] * (b+1)
prime = 0

for i in range(2,int(b**0.5)+1):
  if visit[i]:
    for j in range(i+i,b+1,i):
      visit[j] = 0

for i in range(a,b+1):
  if visit[i]:
    if str(d) in str(i):
      prime += 1

print(prime)
