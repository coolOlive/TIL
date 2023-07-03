import sys
input=sys.stdin.readline

# 수학,그리디/수 고르기/실버3

n,k = map(int,input().split())
nums = sorted(list(map(int,input().split())))
ans = 0

for i in range(1,k+1):
  ans+=nums[-i]-i+1

print(ans)
