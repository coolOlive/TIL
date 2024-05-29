# 구현/숫자/브론즈2

n,m = map(int,input().split())
a = min(n,m)
b = max(n,m)
diff = b-a-1

if diff<1:
  diff = 0

print(diff)
for i in range(a+1,b):
  print(i,end = ' ')
