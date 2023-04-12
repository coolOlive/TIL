import sys
input=sys.stdin.readline

# 구현,그리디/짐 챙기는 숌/실버5

n,m= map(int,input().split())

if n == 0:
    ans = 0
else:
    books = list(map(int,input().split()))
    box = 0
    ans = 1

for i in range(n):
    if box+books[i] <= m:
        box += books[i]
    else:
        box = books[i]
        ans += 1

print(ans)
