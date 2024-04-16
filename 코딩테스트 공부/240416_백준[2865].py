import sys
input = sys.stdin.readline

# 그리디,정렬/나는 위대한 슈퍼스타K/실버4

n,m,k = map(int, input().split())
skill = {i+1:0 for i in range(n)}

for _ in range(m):
  genre = list(map(float, input().split()))
  for j in range(0,n*2,2):
    skill[genre[j]] = max(genre[j+1],skill[genre[j]])

score = sorted(list(skill.values()), reverse=True)
ans = sum(score[:k])

print('%.1f' %ans)
