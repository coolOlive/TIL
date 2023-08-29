import sys
input=sys.stdin.readline

# 그리디,정렬/센서/골드5

n = int(input())
k = int(input())
loca = list(map(int,input().split()))
loca.sort()
ans = []

for i in range(n-1):
  ans.append(loca[i+1] - loca[i])
ans.sort()

print(sum(ans[:n-k]))
