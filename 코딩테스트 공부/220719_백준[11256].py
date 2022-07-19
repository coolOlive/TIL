# 그리디_사탕/실버5

t=int(input())

for _ in range(t):
    j,n=map(int,input().split())

    boxs=[list(map(int,input().split())) for _ in range(n)]
    sizes=sorted([boxs[i][0]*boxs[i][1] for i in range(n)],reverse=True)
    cnt=0
    for s in sizes:
        if j<=0:
            break
        cnt+=1
        j-=s
    print(cnt)