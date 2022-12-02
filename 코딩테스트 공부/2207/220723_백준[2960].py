# 구현,수학,소수판정,에라토스테네스_에라토스테네스의 체/실버4

n,k=map(int,input().split())

def era(n,k,cnt):
    erato=[0,0,1]+[1 for _ in range(n-2)]
    
    for i in range(2,n+1):
        if erato[i]==1:
            for j in range(i,n+1,i):
                if erato[j]==1:
                    if cnt==k:
                        return j
                    erato[j]=0
                    cnt+=1
    
print(era(n,k,1))