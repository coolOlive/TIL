import sys
input=sys.stdin.readline

# 수학,이분탐색/캠프가는 영식/실버4

n,t = map(int,input().split())
bus = []

for _ in range(n):
    s,i,c = map(int,input().split())
    busTime = [s+i*j for j in range(c)]
    if busTime[-1] < t:
        continue
    start,end = 0, c-1
    tmp = 0
    while start <= end:
        midIndex = (start+end)//2
        if busTime[midIndex] >= t:
            end = midIndex - 1
            tmp = midIndex
        else:
            start = midIndex + 1

    bus.append(busTime[tmp]-t)

if bus:
    print(min(bus))
else:
    print(-1)

