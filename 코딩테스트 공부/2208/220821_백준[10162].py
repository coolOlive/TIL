# 수학,그리디/전자레인지/브론즈3

n=int(input())
time=[300,60,10]
ans=[]

for t in time:
    ans.append(str(n//t))
    n%=t
    
print(' '.join(ans)) if n==0 else print(-1)
