 # 수학,그리디/수들의 합/실버5

s=int(input())
n=1
while n*(n+1)/2<=s:
    n+=1
    
print(n-1)