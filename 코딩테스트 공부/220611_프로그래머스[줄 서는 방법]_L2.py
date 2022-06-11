def solution(n, k):
    ans = []
    nums=[i for i in range(1,n+1)]
    facto=[1]
    cnt=1
    
    for i in range(1,n):
        cnt*=i
        facto.append(cnt)

    while (n!=0):
        tmp=facto[n-1]
        idx=k//tmp
        k%=tmp
        if k==0:
            ans.append(nums.pop(idx-1))
        else:
            ans.append(nums.pop(idx))
            
        n-=1
        
    return ans