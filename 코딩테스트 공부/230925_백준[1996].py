import sys
input=sys.stdin.readline

# 구현/지뢰 찾기/실버5

n = int(input())
graph = [list(map(str,input().strip())) for _ in range(n)]
ans = [[0]*(n+2) for _ in range(n+2)]
final = []
move = [[-1,-1],[-1,0],[-1,1],[0,1],[0,-1],[1,1],[1,0],[1,-1]]
rock = []

for i in range(n):
  for j in range(n):
    if str.isdigit(graph[i][j]):
      rock.append([i,j])
      for k in range(8):
        mx = move[k][0]
        my = move[k][1]
        ans[i+mx+1][j+my+1] += int(graph[i][j])
              

for i in range(1,n+1):
  tmp = []
  for j in range(1,n+1):
    if ans[i][j] >= 10:
      tmp.append('M')
    else:
      tmp.append(str(ans[i][j]))
  final.append(tmp)

for r in rock:
  x = r[0]
  y = r[1]
  final[x][y] = '*'

for f in final:
  print(*f,sep='')

