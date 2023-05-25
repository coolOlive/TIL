# 구현,이분탐색,스위핑/어두운 굴다리/실버4

n = int(input())
m = int(input())
loca = list(map(int,input().split()))
ans = max(loca[0],n-loca[-1])

for i in range(1,m):
  tmp = loca[i]-loca[i-1]
  if tmp%2:
    ans=max(ans,tmp//2+1)
  else:
    ans = max(ans,tmp//2)

print(ans)
