# 기본수학1_ACM호텔

t=int(input())

for _ in range(t):
    h,w,n=map(int,input().split())
    a=n%h
    b=n//h
    if a==0:
        print(h*100+b)

    else:
        print(a*100+b+1)
