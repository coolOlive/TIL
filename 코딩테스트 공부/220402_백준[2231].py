# 브루트 포스_분해합/브론즈2

n=int(input())

def divsum(n):
    for i in range(1,n+1):
        num=sum(map(int,str(i)))
        tmp=num+i
        if tmp==n:
            return i
        if i==n:
            return 0

print(divsum(n))
