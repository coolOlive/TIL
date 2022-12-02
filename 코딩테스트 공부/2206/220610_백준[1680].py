# 구현,시뮬레이션_쓰레기 수거/실버4

t=int(input())

for _ in range(t):
    w,n=map(int,input().split())
    x_i=[0]
    w_i=[]
    w_tmp=0
    dist=0
    
    for i in range(n):
        a,b=map(int,input().split())
        x_i.append(a)
        w_i.append(b)

    for j in range(n):

        if j==n-1:
            dist+=x_i[j+1]
            
        if w_tmp+w_i[j]<w:
            w_tmp+=w_i[j]
            dist+=x_i[j+1]-x_i[j]
        elif w_tmp+w_i[j]==w:
            w_tmp=0
            dist+=(x_i[j+1]-x_i[j])+x_i[j+1]*2
            if j==n-1:
                dist-=x_i[j+1]*2
        else:
            w_tmp=w_i[j]
            dist+=(x_i[j+1]-x_i[j])+x_i[j+1]*2        
    print(dist)