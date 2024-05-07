import sys
input=sys.stdin.readline

# 구현/유니대전 퀴즈쇼/브론즈1

n,s=map(str,input().split())
n=int(n)
info=[]
ans,cnt='',0

for _ in range(n):
  a,b=input().split()
  if a == s:
    ans = b
  info.append((a,b))

for i in range(len(info)):
  if info[i][1] == ans:
    if info[i][0] != s:
      cnt += 1
  if info[i][0] == s:
    print(cnt);
    break
