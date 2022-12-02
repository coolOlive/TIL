import sys
input=sys.stdin.readline

# 이분 탐색, 매개 변수 탐색_랜선 자르기/실버3

k,n=map(int,input().split())

lan=[int(input()) for _ in range(k)]

start,end=1,max(lan)

while start<=end:
    mid=(start+end)//2
    lan_cnt=0
    for i in lan:
        lan_cnt+=i//mid
    if lan_cnt>=n:
        start=mid+1
    else:
        end=mid-1

print(end)