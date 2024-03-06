# 수학/시그마/브론즈2

a,b = map(int,input().split())

if a>b:
  a,b=b,a

print(b*(b+1)//2-a*(a-1)//2)
