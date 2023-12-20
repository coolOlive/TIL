import sys
input = sys.stdin.readline

# 구현/동방 프로젝트 (Small)/실버4

n = int(input())
m = int(input())
rooms = [0] * n
ans = n

for _ in range(m):
  x, y = map(int, input().split())
  for i in range(x-1, y-1):
    rooms[i] = 1

print(ans - sum(rooms))
