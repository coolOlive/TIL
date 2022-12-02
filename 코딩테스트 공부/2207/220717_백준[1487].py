import sys
input = sys.stdin.readline

# 브루트포스_물건 팔기/실버4
# 계속 시간초과나서 결국 검색해서 품

n = int(input())
person = [list(map(int, input().split())) for _ in range(n)]
person.sort()

max_profit = 0
ans = []
for i in range(n):
    tmp=0
    for j in range(i, n):
        cost = person[i][0] - person[j][1]
        if cost > 0:
            tmp+=cost
    if max_profit < tmp:
        ans = []
        max_profit = tmp
        ans.append(person[i][0])
print(min(ans) if ans else 0)