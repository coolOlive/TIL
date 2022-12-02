import sys
input=sys.stdin.readline

# 구현, 브루트포스_마인크래프트/실버2
# 파이썬으로는 시간초과 계속 나서 pypy3으로 제출함

n,m,b=map(int,input().split())

land=[list(map(int,input().split())) for _ in range(n)]

min_time=100000000000000000
height=0

for i in range(257):
    bot,top=0,0
    for j in range(n):
        for k in range(m):
            if land[j][k] >= i:
                top +=land[j][k]-i
            else:
                bot += i-land[j][k]

    if top+b >= bot:
        time=(top*2)+bot

        if time <= min_time:
            min_time=time
            height=i

print(min_time,height)