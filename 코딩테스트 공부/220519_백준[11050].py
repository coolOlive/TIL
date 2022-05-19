# 수학,구현,조합론_이항계수 1/브론즈1

def bino(n,k):
    if k==0 or n==k:
        return 1
    return bino(n-1,k)+bino(n-1,k-1)


n,k=map(int,input().split())
print(bino(n,k))