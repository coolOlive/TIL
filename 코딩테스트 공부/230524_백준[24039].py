# 수학,소수판정/2021은 무엇이 특별할까?/실버5

n = int(input())

check=[False]+[True]*103
prime=[]
special=[]

for i in range(2,104):
  if check[i]:
    prime.append(i)
    for j in range(2*i,104,i):
      check[j]=False

for i in range(1,len(prime)):
  special.append(prime[i]*prime[i-1])

for i in special:
  if i>n:
    print(i)
    break
