import sys
input = sys.stdin.readline

# 구현/임시 반장 정하기/브론즈1

n = int(input())
boss = {i:set([]) for i in range(1,n+1)}
students = [list(map(int,input().split())) for _ in range(n)]
ans, large = 1, 1

for i in range(5):
  classs = {i:[] for i in range(1,10)}
  for j in range(n):
    classs[students[j][i]].append(j+1)

  for cl in classs.values():
    for c in cl:
      boss[c].update(cl)

for stu,same in boss.items():
  if len(same)>large:
    large = len(same)
    ans = stu

print(ans)
