import sys
input=sys.stdin.readline

# 정렬/KCPC/실버2

t = int(input().strip())

for _ in range(t):
  n,k,me,m = map(int,input().split())
  teamInfo = [[0]*k for a in range(n)]
  cnt = [0]*n
  time = [0]*n
  tmp = []
  
  for i in range(m):
    team,j,s = map(int,input().split())
    teamInfo[team-1][j-1] = max(teamInfo[team-1][j-1],s)
    cnt[team-1] += 1
    time[team-1] = i
  
  for idx in range(n):
    tmp.append([sum(teamInfo[idx]), cnt[idx], time[idx], idx])
  tmp.sort(key = lambda x:(-x[0], x[1], x[2]))

  for rank in range(n):
    if tmp[rank][3] == me-1:
      print(rank+1)
      break
