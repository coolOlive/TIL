# 수학,구현_분산처리/브론즈2

t=int(input())
nums_last=[[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],
           [8,4,2,6],[9,1],[10]]

for _ in range(t):
    a,b=map(int,input().split())
    aa=a%10
    tmp=nums_last[aa-1]
    print(tmp[b%len(tmp)-1])