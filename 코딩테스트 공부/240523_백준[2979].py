import sys
input=sys.stdin.readline

# 구현/트럭 주차/브론즈2

a,b,c = map(int,input().split())
time = [0]*100
ans = 0

for _ in range(3):
  start,end = map(int,input().split())
  for i in range(start,end):
    time[i]+=1

for j in time:
  if j==0:
    ans+=0
  elif j==1:
    ans+=a
  elif j==2:
    ans+=(b*2)
  elif j==3:
    ans+=(c*3)

print(ans)
