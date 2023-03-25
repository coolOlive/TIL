# dp/피보나치 수의 확장/실버3

n = int(input())
dp = [0, 1]

for i in range(2, abs(n) + 1):
    dp.append((dp[-1] + dp[-2]) % 1000000000)

if n<0 and n%2 == 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)

print(dp[abs(n)])