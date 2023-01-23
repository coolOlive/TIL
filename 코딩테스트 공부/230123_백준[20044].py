import sys
input=sys.stdin.readline

# 그리디,정렬/Project Teams/실버4

n = int(input())
skill = list(map(int,input().split()))

skill.sort()
ans = 200001

for i in range(n):
    ans = min(ans,skill[i]+skill[2*n-i-1])

print(ans)
