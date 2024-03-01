import sys
input = sys.stdin.readline

# 정렬/스텔라(STELLA)가 치킨을 선물했어요/실버5

n = int(input())
info = [list(map(int,input().split())) for _ in range(n)]
info.sort(key = lambda x : [-x[0],x[1]])
ans = 0

for i in range(n):
  if info[i][0] == info[4][0] and info[i][1]>info[4][1]:
    ans += 1

print(ans)
