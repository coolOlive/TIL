import sys
input = sys.stdin.readline

# 슬라이딩윈도우/블로그/실버3

n,x = map(int,input().split())
visit = list(map(int,input().split()))
hap = sum(visit[:x])
maxCnt = hap
cnt = 1
    
for i in range(x,n):
  hap += visit[i]
  hap -= visit[i-x]
  if hap > maxCnt:
    maxCnt = hap
    cnt = 1
  elif hap == maxCnt:
    cnt += 1

if max(visit) == 0:
  print('SAD')
else:
  print(maxCnt)
  print(cnt)
