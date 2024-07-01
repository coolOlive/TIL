import sys
input = sys.stdin.readline

# 수학/고층 건물/골드4

n = int(input())
building = list(map(int,input().split()))
ans = [0]*n

for i in range(n-1) :
  tmp = -1000000001
  for j in range(i+1, n) :
    L = (building[j]-building[i]) / (j-i)
    if L <= tmp :
      continue
    tmp = max(tmp, L)
    ans[i] += 1
    ans[j] += 1

print(max(ans))
