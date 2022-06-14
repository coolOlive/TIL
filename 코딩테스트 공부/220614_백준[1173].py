import sys
input=sys.stdin.readline

# 구현,시뮬레이션_운동/브론즈2

N,m,M,T,R=map(int,input().split())
mec=m
cnt=0

while N>0:
    if m+T>M:
        cnt=-1
        break
    if mec+T<=M:
        N-=1
        mec+=T
    else:
        mec=max(m,mec-R)
    cnt+=1

print(cnt)