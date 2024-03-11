import sys
input=sys.stdin.readline

# 수학/謎紛芥索紀 (Small)/실버5

n = int(input())
ans = 0

for i in range(n):
  c,k = map(int,input().split())
  ans += c*k

print(ans)
