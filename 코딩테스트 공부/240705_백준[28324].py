import sys
input = sys.stdin.readline

# 그리디/스케이트 연습/실버4

n = int(input())
v = tuple(map(int, input().split()))
tmp,ans = 0,0

for i in range(n-1,-1,-1):
  if v[i] > tmp:
    tmp += 1
  else:
    tmp = v[i]
  ans += tmp

print(ans)
