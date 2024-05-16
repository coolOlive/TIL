import sys
input = sys.stdin.readline

# 구현,정렬/중간고사 채점/실버5

n,m = map(int,input().split())
score = list(map(int,input().split()))
hap,minstu = 0,100001

for i in range(m):
  tmp = list(input().split())
  cnt = 0
  for j in range(1,n+1):
    if tmp[j]=='O':
      cnt+=int(score[j-1])
  if hap<cnt:
    hap=cnt
    minstu = int(tmp[0])
  elif hap==cnt:
    minstu = min(minstu,int(tmp[0]))

print(minstu,hap)
