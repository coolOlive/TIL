# 백트래킹,소수판정/신기한 소수/골드5

n = int(input())
check = [2,3,5,7]

def era(num):
  for i in range(2,int(num**0.5)+1):
    if num%i==0:
      return False
  return True

def dfs(num):
  if len(str(num))==n:
    print(num)
  else:
    for j in range(10):
      tmp = num*10+j
      if era(tmp)==True:
        dfs(tmp)

for k in check:
  dfs(k)
