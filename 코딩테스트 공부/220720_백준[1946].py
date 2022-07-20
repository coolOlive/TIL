import sys
input=sys.stdin.readline

# 그리디,정렬_신입 사원/실버1

t=int(input())

for _ in range(t):
    n=int(input())
    score=[list(map(int,input().split())) for _ in range(n)]

    score.sort()
    
    meet_s=score[0][1]
    hire=1

    for i in range(1,n):
        if score[i][1]<meet_s:
            meet_s=score[i][1]
            hire+=1
    print(hire)