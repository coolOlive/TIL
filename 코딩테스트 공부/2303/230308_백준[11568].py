# dp,가장긴증가하는부분수열/민균이의 계략/실버2

n = int(input())
cards = list(map(int,input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    large = 0
    for j in range(i):
        if cards[j] < cards[i]:
            large = max(dp[j],large)
    dp[i] = large + 1

print(max(dp))
