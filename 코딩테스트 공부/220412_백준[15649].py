# 백트래킹_N과 M(1)/실버3
# **DFS 공부하기**

n,m=map(int,input().split())
s=[]

def backt():
    if len(s)==m:
        print(*s)
        return
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            backt()
            s.pop()
    
backt()