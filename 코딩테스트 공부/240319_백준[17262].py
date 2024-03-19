import sys
input = sys.stdin.readline

# 그리디/팬덤이 넘쳐흘러/실버4

n = int(input())
f = [list(map(int ,input().split())) for _ in range(n)]

a = sorted(f, key=lambda x: x[0])
b = sorted(f, key=lambda x: x[1])
ans = a[-1][0] - b[0][1]

if ans <= 0 :
  print(0)
else :
  print(ans)
