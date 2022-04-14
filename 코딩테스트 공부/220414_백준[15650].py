# 백트래킹_N과 M(2)/실버3

n,m=map(int,input().split())
s=[]

def dfs():
    if len(s)==m and sorted(s)==s:
        print(*s)
        return
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
    
dfs()