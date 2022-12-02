import sys
input=sys.stdin.readline

# 그리디/게임을 만든 동준이/실버4

n=int(input())
score = [int(input()) for _ in range(n)]
cnt=0

for i in range(n-1,0,-1):
    if score[i]<=score[i-1]:
        cnt+=(score[i-1]-score[i]+1)
        score[i-1]=score[i]-1

print(cnt)