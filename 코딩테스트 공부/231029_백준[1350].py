import sys
input=sys.stdin.readline

# 수학/진짜 공간/브론즈2

n = int(input())
data = list(map(int, input().split()))
cluster = int(input())
ans = 0

for d in data :
  ans += d // cluster
  if d% cluster > 0:
    ans += 1

print(cluster * ans)
