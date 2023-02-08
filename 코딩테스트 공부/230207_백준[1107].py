import sys
input=sys.stdin.readline

# 브루트포스/리모컨/골드5
# 골드 문제.. 어렵다

n = int(input())
m = int(input())
btn = list(map(str,input().split()))
ans = abs(100-n)

for i in range(1000001):
    tmp = str(i)
    for num in tmp:
        if num in btn:
            break
    else:
        ans = min(ans, abs(i - n) + len(tmp))

print(ans)
