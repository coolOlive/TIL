import sys
input=sys.stdin.readline

# 정렬_좌표 정렬하기/실버5

n=int(input())

num=[list(map(int,input().split())) for _ in range(n)]

for a in sorted(num):
    print(a[0],a[1])