import sys
input=sys.stdin.readline

# 중국인의 나머지 정리/카잉 달력/실버1

def kaing(m, n, x, y):
    while x <= (m * n):
        if (x - y) % n == 0:
            return x
        x += m
    return -1

t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    print(kaing(m, n, x, y))
