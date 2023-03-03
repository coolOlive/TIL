import sys
input=sys.stdin.readline

# 정수론,수학/조합 0의 개수/실버2

n,m = map(int,input().split())

def count(a,b):
    cnt = 0
    while a:
        a //= b
        cnt += a
    return cnt

five = count(n,5) - count(m,5) - count(n-m,5)
two = count(n,2) - count(m,2) - count(n-m,2)

ans = min(five,two)
print(ans)
