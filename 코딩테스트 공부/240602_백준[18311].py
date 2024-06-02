# 구현/왕복/실버5

n,k = map(int,input().split())
m1 = list(map(int,input().split()))
m = m1+m1[::-1]

for i in range(n*2):
  k -=m[i]
  if k<0:
    if i>n:
      print((n*2)-i)
      break
    print(i+1)
    break
