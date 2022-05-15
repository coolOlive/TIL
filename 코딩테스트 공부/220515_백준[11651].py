import sys
input=sys.stdin.readline

# 정렬_좌표 정렬하기 2/실버5

n=int(input())

xy=[tuple(map(int,input().split())) for _ in range(n)]
xy.sort(key = lambda loca: (loca[1], loca[0]))

for i in range(n):
    print(xy[i][0],xy[i][1])