import sys
input = sys.stdin.readline

# 수학,정수론/거의 소수/골드5

a,b=map(int,input().split())
prime=[False,False]+([True]*(int(b**0.5)-1))
cnt=0

for i in range(2,int(b**0.5)+1):
  ib = int(b**0.5)
  if prime[i]:
    if i*i > ib:
      break
    for j in range(2*i,ib+1,i):
      prime[j] = False

for i in range(2,len(prime)):
  if prime[i]:
    tmp = i*i
    while True:
      if tmp < a:
        tmp *= i
        continue
      if tmp > b:
        break
      tmp *= i
      cnt += 1
          
print(cnt)
