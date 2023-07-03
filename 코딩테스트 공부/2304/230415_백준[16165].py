import sys
input=sys.stdin.readline

# 자료구조,해시/걸그룹 마스터 준석이/실버3

n,m= map(int,input().split())
team = dict()
member = dict()

for _ in range(n):
  teamName = input().strip()
  team[teamName] = []
  k = int(input())
  for i in range(k):
      memberName = input().strip()
      team[teamName].append(memberName)
      member[memberName] = teamName

for _ in range(m):
  q = input().strip()
  qType = int(input())
  if qType == 0:
      print(*sorted(team[q]),sep='\n')
  else:
      print(member[q])
