import sys
input=sys.stdin.readline

# 구현/후보 추천하기/실버1

n = int(input())
st_n = int(input())
st= list(map(int,input().split()))

pic = dict()

for i in range(st_n):
  if st[i] in pic:
    pic[st[i]][0] += 1
    continue
  if len(pic)<n:
    pic[st[i]] = [1,0]
  else:
    tmp = sorted(pic.items(),key = lambda x:(x[1][0],x[1][1]))        
    del pic[tmp[0][0]]
    pic[st[i]] = [1,0]

ans = list(sorted(pic.keys()))
print(*ans)
