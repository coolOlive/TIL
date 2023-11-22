# 수학/삼각형만들기/실버5
# 시간초과때문에 결국 pypy3로 제출함..

n=int(input())
ans = 0

for i in range(1,n+1):
  for j in range(i,n+1):
    tmp = n-(i+j)
    if i<(j+tmp) and tmp <(i+j) and j <=tmp:
      ans+=1
      if j>tmp:
        break

print(ans)
