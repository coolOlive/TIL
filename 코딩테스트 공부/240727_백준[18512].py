# 구현/점프 점프/브론즈1
# 으아악 

x,y,a,b = map(int,input().split())
ans, cnt = 0, 0

while 1:
  if cnt>1000:
    ans=-1
    break
  if a==b:
    ans=a
    break
  if a>b:
    b+=y
  elif a<b:
    a+=x
  cnt+=1
print(ans)
