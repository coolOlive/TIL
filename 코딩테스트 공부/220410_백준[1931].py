# 그리디 알고리즘_ 회의실 배정/실버2

n=int(input())
time=[list(map(int,input().split())) for i in range(n)]
time.sort(key=lambda x: [x[1], x[0]])

ans=0
end_time=0

for a,b in time:
    if a >= end_time:
        ans+=1
        end_time=b

print(ans)