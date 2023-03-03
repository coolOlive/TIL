# 브루트포스/암호코드/골드5
# 어렵다. 차근차근 공부할 필요성 있음!

code = list(map(int,input()))
l = len(code)
dp = [0 for _ in range(l+1)]
dp[0] =dp[1] = 1

def decode():
    for i in range(2,l+1):
        if code[i] > 0:
            dp[i] += dp[i-1]
        tmp = code[i-1] * 10 + code[i]
        if tmp >= 10 and tmp <= 26:
            dp[i] += dp[i-2]

if code[0] == 0:
    print(0)
else:
    code = [0] + code
    decode()
    print(dp[l]%1000000)
