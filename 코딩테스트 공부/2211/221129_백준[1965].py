import sys
input=sys.stdin.readline

# dp/상자넣기/실버2

n = int(input())
s = list(map(int, input().split()))
dp = [1]

for i in range(1, n):
    tmp = []
    for j in range(i):
        if s[i] > s[j]:
            tmp.append(dp[j] + 1)
    if not tmp:
        dp.append(1)
    else:
        dp.append(max(tmp))
        
print(max(dp))
